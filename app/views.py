from app import app
from flask import render_template


@app.route("/") 
def index(): 
	return render_template("public/index.html")

@app.route("/about")
def about():
    return render_template("public/about.html")
