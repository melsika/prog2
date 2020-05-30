
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






"""braucht es diese Route zu ergebnis überhaupt?"""
@app.route("/geschenk_ergebnis")
def geschenk_ergebnis_person():
    return render_template('geschenk_ergebnis_person.html')


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
            return render_template('bereits_vorhandene_geschenkidee.html', person=person, beschreibung=beschreibung, idee=idee, hashtag=hashtag)
        inhalt.append(neuer_eintrag)
        daten.json_speichern("geschenk_idee_formular.json", inhalt)
        return render_template('erfolgreich_gespeichert.html', person=person, beschreibung=beschreibung, idee=idee, hashtag=hashtag)

    return render_template("geschenk_erfassen.html")


@app.route("/geschenk_suchen", methods=['GET', 'POST'])
def geschenk_suchen():
    hashtags = daten.hashtags_anzeigen()


    if request.method == 'POST':
        personen_name = request.form["person"]
        ausgewaehlte_hashtags = request.form.getlist("hashtag")
        print(ausgewaehlte_hashtags)
        inhalt = daten.geschenke_anzeigen_fuer_person(personen_name)
        geschenke = daten.geschenke_mit_hashtags(inhalt, ausgewaehlte_hashtags)
        return render_template('geschenk_ergebnis_person.html', geschenk_ideen= geschenke, name= personen_name)
    return render_template('geschenk_suchen.html', hashtags=hashtags)





""" SICHERUNG ZUM LÖSCHEN WENNS FUNKTIONIERT
@app.route("/geschenk_suchen", methods=['GET', 'POST'])
def geschenk_eintrag_suchen():
    if request.method == 'POST':
        personen_name = request.form["person"]
        inhalt = daten.geschenke_anzeigen_fuer_person(personen_name)
    return render_template('geschenk_ergebnis_person.html', geschenk_ideen= inhalt, name= personen_name)
"""


    
if __name__ == "__main__":
    app.run(debug=True, port=5000)