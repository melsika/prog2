
from flask import Flask
from flask import request
from flask import render_template
from json import loads, dumps
import daten

app = Flask("Geschenkidee")
app = Flask("Daten")

"""
@app.route('/hello/')
@app.route("/hello/<name>")
def begruessung(name=False):
    if name:
        return "Hallo " + name + "!"
    else:
        return "Not Hallo World again…"

"""

@app.route('/geschenkidee')
def home():
    return render_template('index.html', name="Melanie")



@app.route("/geschenkidee_erfassen")
def geschenk_erfassen():
  return render_template('geschenk_erfassen.html')



@app.route("/geschenkidee_suchen")
def geschenk_suchen():
    return render_template('geschenk_suchen.html')


@app.route("/speichern_ich")
def json_speichern():
    geschenk_idee = [{'name': 'Maja', 'tel': 123}]

    with open ('geschenk_idee_1.json', 'w') as open_file:
        json_als_string = dumps(geschenk_idee)
        open_file.write(json_als_string)

    return render_template("ergebnis.html", liste = geschenk_idee)
    
    """json_als_string = dumps(geschenk_idee)
    geschenk_idee = loads(json_als_string)
""" 

@app.route("/einlesen")
def json_einlesen():
    with open('geschenk_idee.json') as open_file:
        json_als_string = open_file.read()
        mein_eingelesenes_dict = loads(json_als_string)

    return mein_eingelesenes_dict



"""---------------------------------------------------"""






@app.route("/speichern/<aktivitaet>")
def speichern(aktivitaet):
    zeitpunkt, aktivitaet = daten.aktivitaet_speichern(aktivitaet)

    return "Gespeichert: " + aktivitaet + " um " + str(zeitpunkt)


@app.route("/liste")
def auflisten():
    aktivitaeten = daten.aktivitaeten_laden()

    aktivitaeten_liste = ""
    for key, value in aktivitaeten.items():
        zeile = str(key) + ": " + value + "<br>"
        aktivitaeten_liste += zeile

    return aktivitaeten_liste


"""
@app.route("/helloo/", methods=['GET', 'POST'])
def hallo():
    if request.method == 'POST':
        ziel_person = request.form['vorname']
        rueckgabe_string = "Hello " + ziel_person + "!"
        return rueckgabe_string

    return render_template("index.html")
"""
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
