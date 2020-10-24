from flask import render_template, Blueprint, session, redirect
from functools import wraps

BP = Blueprint('root', __name__)


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'profile' not in session:
            return redirect('/login')
        return f(*args, **kwargs)
    return decorated


def get_blueprint():
    return BP


@BP.route("/")
@requires_auth
def index():
    return render_template("public/index.html")


@BP.route("/about")
def about():
    return render_template("public/about.html")
