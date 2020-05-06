
from flask import Flask
from flask import request
from flask import render_template

app = Flask("Geschenkidee")

"""
@app.route('/hello/')
@app.route("/hello/<name>")
def begruessung(name=False):
    if name:
        return "Hallo " + name + "!"
    else:
        return "Not Hallo World again…"

"""



@app.route("/hello/", methods=['GET', 'POST'])
def hallo():
    if request.method == 'POST':
        ziel_person = request.form['vorname']
        rueckgabe_string = "Hello " + ziel_person + "!"
        return rueckgabe_string

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)

"""

if __nachname__ == "__main__":    
	app.run(debug=True, port=5000)

if __strasse__ == "__main__":    
	app.run(debug=True, port=5000)

if __zahl__ == "__main__":    
	app.run(debug=True, port=5000)
"""
