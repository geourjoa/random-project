from flask import Blueprint, render_template

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return render_template("index.html")


@main.route("/classifications")
def classifications():
    return render_template("classifications.html")


@main.route("/search-by-tag")
def search_by_tag():
    return render_template("search_by_tag.html")


