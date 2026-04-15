from arkindex_export.models import Classification, Element, Image, database
from flask import Blueprint, current_app, render_template, request, abort
from peewee import fn

main = Blueprint("main", __name__)


def open_db():
    db_path = current_app.config["DATABASE_PATH"]
    database.init(db_path)


@main.route("/")
def index():
    return render_template("index.html")


@main.route("/classifications")
def classifications():
    open_db()
    image_count = fn.COUNT(Element.image.distinct()).alias("image_count")
    rows = (
        Classification.select(
            Classification.class_name,
            image_count,
        )
        .join(Element, on=(Classification.element == Element.id))
        .where(Element.type == "photograph")
        .group_by(Classification.class_name)
        .having(fn.COUNT(Element.image.distinct()) >= 10)
        .order_by(fn.COUNT(Element.image.distinct()).desc())
    )
    return render_template("classifications.html", classifications=rows)


@main.route("/search-by-tag")
def search_by_tag():
    query = request.args.get("q", "").strip()
    elements = []
    if query:
        open_db()
        elements = (
            Classification.select(Classification, Element, Image)
            .join(Element, on=(Classification.element == Element.id))
            .join(Image, on=(Element.image == Image.id))
            .where(
                (Classification.class_name == query)
                & (Element.type == "photograph")
            )
            .order_by(Classification.confidence.desc())
        )
    return render_template("search_by_tag.html", query=query, elements=elements)


@main.route("/image/<image_id>")
def image_detail(image_id):
    open_db()
    try:
        image = Image.get_by_id(image_id)
    except Image.DoesNotExist:
        abort(404)

    classifications = (
        Classification.select(
            Classification.class_name,
            Classification.confidence,
            Classification.state,
            Element.name.alias("element_name"),
            Element.type.alias("element_type"),
            Element.id.alias("element_id"),
        )
        .join(Element, on=(Classification.element == Element.id))
        .where((Element.image == image_id) & (Element.type == "photograph"))
        .order_by(Classification.confidence.desc())
    )

    return render_template(
        "image_detail.html",
        image=image,
        classifications=classifications,
    )


