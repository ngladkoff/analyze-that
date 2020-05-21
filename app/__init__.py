from flask import Flask

app = Flask(__name__)
from app import views
from . import admin_views
app.register_blueprint(admin_views.bp)
