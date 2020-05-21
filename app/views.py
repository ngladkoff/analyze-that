from app import app

@app.route("/") 
def index(): 
	return "<h1>Bienvenido a Analyze That</h1>"

@app.route("/about")
def about():
    return "<h1>About Analyze That</h1>"
