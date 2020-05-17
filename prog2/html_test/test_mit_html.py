from flask import Flask 
from flask import render_template

app = Flask("blocks")

@app.route('/')
def start():    
    return render_template("start.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":    
    app.run(debug=True, port=5000)