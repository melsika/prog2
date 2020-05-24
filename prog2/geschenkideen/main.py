
from flask import Flask
from flask import request
from flask import redirect
from flask import render_template
from json import loads, dumps
import json
import daten


app = Flask("Geschenkidee")
app = Flask("Daten")
app = Flask("templates")



"""alle Seitenverlinkungen"""

@app.route('/geschenkidee')
def home():
    return render_template('index.html')


@app.route("/geschenk_erfassen")
def geschenk_erfassen():
    return render_template('geschenk_erfassen.html')



@app.route("/geschenkidee_suchen/")
def geschenk_suchen():
    return render_template('geschenk_suchen.html')



@app.route("/ergebnis/<personen_name>")
def ergebnis(personen_name):
    inhalt = daten.geschenke_anzeigen_fuer_person(personen_name)
    return render_template('ergebnis_person.html', geschenk_ideen= inhalt)



@app.route("/hashtags")
def hashtags():
    resultat = {
    "test1key" : daten.hashtags_anzeigen()
    }
    return render_template('ergebnis_hashtag.html', resultat=resultat)

"""
@app.route("/ergebnis/<personen_name>")
def ergebnis(personen_name):
    inhalt = daten.geschenke_anzeigen_fuer_person(personen_name)
    return render_template('ergebnis_person.html', geschenk_ideen= inhalt)



@app.route("/hashtags")
def hashtags():
    resultat = {
    "test1key" : daten.hashtags_anzeigen()
    }
    return resultat
"""

"""---------------------------------------------------"""


"""
Beim Formular nehme ich die neuen Einträge mit request entgegen und forme direkt das json
Jede Idee kann nur einmal vorkommen, ich rufe die Hilfsfunktion dazu im daten.py auf.
Der json_speichern funktion gebe ich als variable an welches dokument und die andere variable ist der Inhalt,
in diese habe ich zuvor den aktuellen Inhalt geladen und den neuen Eintrag hinzugefügt, so wird der neue Inhalt nun gespeichert.
"""
  
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


@app.route("/geschenkidee_suchen/", methods=['GET', 'POST'])
def formular_eintrag_suchen():
    if request.method == 'POST':
        personen_name = request.form["person"]
        return personen_name

"""
@app.route("/hello/", methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        ziel_person = request.form['vorname']
        rueckgabe_string = "Hello " + ziel_person + "!"
        return rueckgabe_string

    return render_template("index.html")
  """ 
"""

@app.route("/ergebnis/<personen_name>")
def ergebnis(personen_name):
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

"""Loris
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
"""