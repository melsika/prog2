
from flask import Flask
from flask import request
from flask import render_template
from json import loads, dumps
import daten
from datetime import datetime
import json


app = Flask("Geschenkidee")
app = Flask("Daten")
app = Flask("templates")

geschenk_idee_json = "./geschenk_idee.json"

"""
@app.route('/hello/')
@app.route("/hello/<name>")
def begruessung(name=False):
    if name:
        return "Hallo " + name + "!"
    else:
        return "Not Hallo World again…"

"""

"""alle Seitenverlinkungen"""

@app.route('/geschenkidee')
def home():
    geschenk = "hallotestgeklappt"
    return render_template('index.html', name="Melanie", geschenk="geklappt" )


@app.route("/geschenk_erfassen")
def geschenk_erfassen():
    return render_template('geschenk_erfassen.html')



@app.route("/geschenkidee_suchen")
def geschenk_suchen():
    return render_template('geschenk_suchen.html')


@app.route("/ergebnis/<personen_name>")
def ergebnis(personen_name):
    inhalt = daten.geschenke_anzeigen_fuer_person(personen_name)
    return render_template('ergebnis.html', geschenk_ideen= inhalt)


@app.route("/geschenk_idee")
def index():
    return "Willkommen zu unsere App."

"""--------------------------------------------"""
"""json mit Internet"""
"""
try:
    open_file = open("text.txt", encoding = 'utf-8')
except Exception as f:
    raise
else:
    pass
finally:
    open_file.close()


def doku_test_schreiben():
    with open('text.txt','w', encoding = 'utf-8') as open_file:
        open_file.write("erstes dokun")
        open_file.write("zweite zeile")
        open_file.write("letzte")

def doku_test_lesen():
    open_file = open("text.txt", 'r', encoding = 'utf-8')
    open_file.read(4)


@app.route("/json_test")
def json_test():
    
    with open('geschenk_idee.json') as open_file:
        data = json.load(                                     open)
    return print(data)


@app.route("/speichern_ich")
def json_speichern():
    geschenk_idee = [{'name': 'Maja', 'tel': 123}]

    with open ('geschenk_idee_1.json', 'w') as open_file:
        json_als_string = dumps(geschenk_idee)
        open_file.write(json_als_string)

    return render_template("ergebnis.html", liste = geschenk_idee)
    

@app.route("/einlesen")
def json_einlesen():
    with open('geschenk_idee.json') as open_file:
        json_als_string = open_file.read()
        mein_eingelesenes_dict = loads(json_als_string)

    return render_template("ergebnis.html", mein_eingelesenes_dict)

"""

"""---------------------------------------------------"""

"""Loris"""
def eintrag_speichern(pd, id, datum, symp1, symp2, symp3, symp4, symp5, symp6, symp7, symp8):
    pd = dic_laden()
    if id in pd:
        pd[id][datum] = {"Sodbrennen": symp1,}


@app.route("/neuereintrag", methods= ["GET", "POST"])
def neuereintrag():
    if request.method == "POST":
        pd = {}
        id = request.form["id"]
        datum = request.form["datum"]
        symp1 = request.form["symp1"]
        symp2 = request.form["symp2"]
        symp3 = request.form["symp3"]
        symp4 = request.form["symp4"]
        symp5 = request.form["symp5"]
        symp6 = request.form["symp6"]
        symp7 = request.form["symp7"]
        symp8 = request.form["symp8"]

        eintrag_speichern(pd, id, datum, symp1, symp2, symp3, symp4, symp5, symp6, symp7, symp8)

    return render_template("neuereintrag.html")


def dic_laden():
    try:
        with open('./templates/json/test.json', "r") as json_file:
            pd = json.load(json_file)
        return pd
    except Exception:
        return {}

def eintrag_speichern(pd, id, datum, symp1, symp2, symp3, symp4, symp5, symp6, symp7, symp8):
    pd = dic_laden()
    if id in pd:
        pd[id][datum] = {"Sodbrennen": symp1, "Rückfluss von Flüssigkeit oder Nahrung in den Mund": symp2, "Schmerzen im Oberbauch": symp3, "Beschwerden beim Schlucken der Nahrung": symp4, "Heiserkeit": symp5, "Halsschmerzen": symp6, "Mundbrennen": symp7, "Völlegefühl im Oberbauch": symp8}

    else:
        pd[id] = {datum: {"Sodbrennen": symp1, "Rückfluss von Flüssigkeit oder Nahrung in den Mund": symp2, "Schmerzen im Oberbauch": symp3, "Beschwerden beim Schlucken der Nahrung": symp4, "Heiserkeit": symp5, "Halsschmerzen": symp6, "Mundbrennen": symp7, "Völlegefühl im Oberbauch": symp8}}
    with open("./templates/json/test.json", "w", encoding='utf-8') as open_file:
            json.dump(pd, open_file, indent = 4)

"""______--------------------------------------------------"""


"""Odoni Github"""


  
@app.route("/geschenk_erfassen", methods=['GET', 'POST'])
def formular_neuer_eintrag():
    if request.method == 'POST':
        idee = request.form["idee"]
        beschreibung = request.form["beschreibung"]
        person = request.form["person"]
        hashtag = request.form["hashtag"]
        inhalt = daten.json_lesen("geschenk_idee_formular.json")
        neuer_eintrag = {
            "person" : person,
            "idee" : idee,
            "beschreibung" : beschreibung,
            "hashtag" : hashtag
        }
        if daten.idee_bereits_vorhanden(person, idee):
            return "Eintrag bereits vorhanden, da kann ich noch was anderes"
        inhalt.append(neuer_eintrag)
        daten.json_speichern("geschenk_idee_formular.json", inhalt)
        return "speichern erfolgreich"

    return render_template("geschenk_erfassen.html")

   


@app.route("/liste")
def auflisten():
    formular = daten.formular_laden()

    formular_liste = ""
    for key, value in geschenk_idee_formular.items():
        zeile = str(key) + ": " + value + "<br>"
        formular_liste += zeile

    return formular_liste






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
