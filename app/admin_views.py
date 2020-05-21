from app import app
from flask import render_template, Blueprint

bp= Blueprint('admin', __name__, url_prefix='/admin')

@bp.route('/dashboard')
def admin_dashboard():
    return render_template("admin/dashboard.html")

@bp.route('/profile')
def admin_profile():
    return "Admin profile"

