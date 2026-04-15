import sqlite3

from flask import Blueprint, current_app, render_template

main = Blueprint("main", __name__)


def get_db():
    db_path = current_app.config["DATABASE_PATH"]
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


@main.route("/")
def index():
    return render_template("index.html")


@main.route("/classifications")
def classifications():
    conn = get_db()
    rows = conn.execute(
        "SELECT id, element_id, class_name, state, confidence "
        "FROM classification LIMIT 10"
    ).fetchall()
    conn.close()
    return render_template("classifications.html", classifications=rows)


@main.route("/search-by-tag")
def search_by_tag():
    return render_template("search_by_tag.html")


