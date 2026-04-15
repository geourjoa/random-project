from arkindex_export.models import Classification, Element, database
from flask import Blueprint, current_app, render_template

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
    rows = (
        Classification.select(
            Classification.id,
            Classification.class_name,
            Classification.state,
            Classification.confidence,
            Element.name.alias("element_name"),
        )
        .join(Element, on=(Classification.element == Element.id))
        .limit(10)
    )
    return render_template("classifications.html", classifications=rows)


@main.route("/search-by-tag")
def search_by_tag():
    return render_template("search_by_tag.html")


