
from flask import Flask
from flask import request
from flask import render_template
from json import loads, dumps
import json
import daten



app = Flask("Geschenkidee")



"""
Meine main.py Datei setzt die Hilfsfunktionen vom daten.py zusammen. So ist es mir möglich, 
die Übersicht zu bewahren, weil alle Details im daten.py file behandelt werden. Es werden nur von hier
@app.routen gemacht. Die daten.py wird oben importiert, danach spreche ich die einzelnen Funktionen jeweils mit daten. an. 
"""

""" 
Überlegung:
Auf der Home Seite befindet sich ein Barchart, er soll anzeigen, welche Hashtags
wie oft vorkommen. Dazu brauche ich Plotly, den Code finde ich auf deren Webseite.

Funktionsbeschreibung:
Ich bekomme ein mit dem Counter gezähltes Dictionary zurück, welches ich mit der 
for Schleife trenne und die Key und Values in separate Listen speichere.
Diese Listen übergebe ich, um den Barchart darzustellen. 
Das ganze wird als viz_div Variable dem index.html übergeben.
"""

@app.route('/geschenkidee')
def home():
    
    anzahl = daten.anzeige_hashtags()
    
    y_hashtag = []
    x_hashtag = []
    for hashtag, zahl in anzahl.items():
        x_hashtag.append(hashtag)
        y_hashtag.append(zahl)

    div = daten.barchart(x_hashtag, y_hashtag, "Anzahl Geschenkideen pro Hashtag")

    return render_template('index.html', viz_div=div)



"""
Überlegungen: 
Ich möchte eine Eingabe, in der der User die Werte Person, Idee, Beschreibung und einen Hashtag angibt.
Dazu benötige ich ein Formular von Bootstrap, welches im html mit den values erfasst werden muss, um von meinem
main.py erkannt zu werden, dazu benötige ich Flask. Die erfassten Strings sollen in einem Json gespeichert werden.

Funktionsbeschreibung:
Das Formular nimmt neue Einträge entgegen und speichert diese im Json ab.
Dafür werden die Eingaben mit request entgegengenommen. Da die Felder Person und Hashtag bei der Suche
wiederverwendet werden, werden sie mit einem grossen Anfangsbuchstaben abgespeichert. So werden doppelte 
Einträge durch Gross- Kleinschreibung verhindert. Bei der Idee und Beschreibung habe ich das nicht gemacht,
da diese nicht zusammen verglichen werden.
Wenn aus Versehen ein leerer Eintrag gespeichert wird, wird dieser nicht gespeichert und auf die entsprechende Meldung weitergeleitet

Die Felder Person und Idee werden mit den bestehenden Einträgen abgeglichen, damit wird verhindert, dass die 
selbe Idee zwei Mal gespeichert werden kann. Diese Hilfsfunktion wird im daten.py abgerufen.
Wenn das nicht der Fall ist, wird der Eintrag der Json Datei hinzugefügt. Dazu wird der neue Inhalt der Funktion 
dem daten.py übergeben und gespeichert.
Als Bestätigung, dass der Eintrag gespeichert wurde, wird das html erfolgreich_gespeichert.html zurückgegeben,
darin werden die Details nochmals aufgelistet.
Damit die geschenk_erfassen.html Seite angezeigt wird, ist sie im return geschrieben, alle oben erwähnten
Schritte sind in einer if Bedingung und werden deshalb erst ausgeführt wenn etwas erfasst wird (mit dem submit Button).
"""
  
@app.route("/geschenk_erfassen", methods=['GET', 'POST'])
def formular_neuer_eintrag():
    if request.method == 'POST':
        person = request.form["person"].capitalize()
        idee = request.form["idee"]
        beschreibung = request.form["beschreibung"]
        hashtag = request.form["hashtag"].capitalize()
        inhalt = daten.json_lesen("geschenk_idee_formular.json")
        neuer_eintrag = {
            "person" : person,
            "idee" : idee,
            "beschreibung" : beschreibung,
            "hashtag" : hashtag
        }
        if person == "" and idee == "" and beschreibung == "" and hashtag == "":
            return render_template('leerer_eintrag.html')
        if daten.idee_bereits_vorhanden(person, idee):
            return render_template('bereits_vorhandene_geschenkidee.html', person=person, idee=idee, beschreibung=beschreibung, hashtag=hashtag)
        inhalt.append(neuer_eintrag)
        daten.json_speichern("geschenk_idee_formular.json", inhalt)
        return render_template('erfolgreich_gespeichert.html', person=person, idee=idee, beschreibung=beschreibung, hashtag=hashtag)

    return render_template("geschenk_erfassen.html")



"""
Überlegung:
Ich brauche einerseits eine Suchseite als Formular, und andererseits müssen die Eingaben verglichen
werden, um nur die gewünschten als Ergebnis auszugeben. Als Suchmöglichkeiten definiere ich die Personen und 
die Hashtags, diese werden in einzelnen Funktionen abgearbeitet.

Funktionsbeschreibung:
Ausserhalb der if Bedingung, werden die Personen und Hashtags angezeigt, dazu werden 
dem geschenk_suchen.html die beiden Variablen mitgegeben, damit sie Flask an das Html übermitteln kann.
Sobald eine Eingabe erfolgt, wird die if Bedingung ausgeführt. Es besteht die Möglichkeit, nach einer Person 
oder Hashtags zu suchen, diese werden durch request.get entgegengenommen. Da es bei den Hashtags möglich ist, 
mehrere anzuwählen, brauche ich eine Liste, damit sie separiert werden. Für den Fall, dass keine Person angegeben
wird, habe ich das Feld Person auswählen auf einen leeren String gesetzt, denn in der Hilfsfunktion werden nur
Strings mit inhalt berücksichtigt. Da die Variable personen_name im geschenk_ergebnis_person.html verwendet wird,
musste ich diese if Bedingung im main.py machen und nicht im daten.py. So wird mir bei der Ergebnis Anzeige kein Titel angezeigt.

Der personen_name wird der Hilfsfunktion mitgegeben, zurück bekomme ich alle Einträge die mit 
dem key person im Json file übereinstimmen.
Als nächstes prüfe ich, ob es für die ausgewählte Person Geschenke mit den ausgewählten Hashtags gibt. Wenn ja, 
werden diese in der Variable geschenke gespeichert.
Die Ergebnisse werden im geschenk_ergebnis_person.html angezeigt, dafür brauche ich im html die beiden Variablen geschenke und
personen_name.
"""

@app.route("/geschenk_suchen", methods=['GET', 'POST'])
def geschenk_suchen():
    personen = daten.personen_anzeigen()
    hashtags = daten.hashtags_anzeigen()
    
    if request.method == 'POST':
        personen_name = request.form.get("person")
        ausgewaehlte_hashtags = request.form.getlist("hashtag")
        if personen_name == "Person auswählen":
            personen_name = ""
        inhalt = daten.geschenke_anzeigen_fuer_person(personen_name)
        geschenke = daten.geschenke_mit_hashtags(inhalt, ausgewaehlte_hashtags)
        return render_template('geschenk_ergebnis_person.html', geschenk_ideen= geschenke, name= personen_name)
    return render_template('geschenk_suchen.html', hashtags=hashtags, personen=personen)



    
if __name__ == "__main__":
    app.run(debug=True, port=5000)