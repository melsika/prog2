from flask import Flask
from flask import render_template
from flask import request

app = Flask("Hello World")

@app.route("/hello")
def hello_world():  
    return render_template("index.html", name ="Melanie")

@app.route("/test")
def test():
    return "success"
"""
@app.route("/hoi")
@app.route("/hoi/<vorname>")
def halloo(vorname=False):
    if vorname:
        return "Hallo " + vorname + "!"
    else:
        return "Not Hallo World again..."
"""

@app.route("/hello", methods=["GET", "POST"])
def hallo():
    if request.method == "POST":
        ziel_person = request.form["nachname"]
        rueckgabe_string = "Hello " + ziel_person + "!"
        return rueckgabe_string

    return render_template("index.html")

@app.route("/helloo")
def liste():
    return render_template("index.html", dinger=["Eins", "Zwei", "Drei"])

@app.route("/helloh")
def zahlen():
    return render_template("index.html", zahl=6)

if __name__ == "__main__":
    app.run(debug=True, port=5000)