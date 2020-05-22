from flask import render_template, Blueprint

BP = Blueprint('root', __name__)


def get_blueprint():
    return BP


@BP.route("/")
def index():
    return render_template("public/index.html")


@BP.route("/about")
def about():
    return render_template("public/about.html")
