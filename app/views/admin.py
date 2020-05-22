from flask import render_template, Blueprint

BP = Blueprint('admin', __name__, url_prefix='/admin')


def get_blueprint():
    return BP


@BP.route('/dashboard')
def admin_dashboard():
    return render_template("admin/dashboard.html")


@BP.route('/profile')
def admin_profile():
    return "Admin profile"
