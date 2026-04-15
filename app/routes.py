from arkindex_export.models import Classification, Element, database
from flask import Blueprint, current_app, render_template, request
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
    element_count = fn.COUNT(Classification.element.distinct()).alias("element_count")
    rows = (
        Classification.select(
            Classification.class_name,
            element_count,
        )
        .group_by(Classification.class_name)
        .having(fn.COUNT(Classification.element.distinct()) >= 10)
        .order_by(fn.COUNT(Classification.element.distinct()).desc())
    )
    return render_template("classifications.html", classifications=rows)


@main.route("/search-by-tag")
def search_by_tag():
    query = request.args.get("q", "").strip()
    elements = []
    if query:
        open_db()
        elements = (
            Classification.select(
                Element.id.alias("element_id"),
                Element.name.alias("element_name"),
                Element.type.alias("element_type"),
                Classification.confidence,
            )
            .join(Element, on=(Classification.element == Element.id))
            .where(Classification.class_name == query)
            .order_by(Classification.confidence.desc())
        )
    return render_template("search_by_tag.html", query=query, elements=elements)


