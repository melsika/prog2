
import json
import plotly.graph_objects as go
from plotly.offline import plot
import plotly
from collections import Counter


"""
Die daten.py Datei beinhaltet alle Hilfsfunktionen, die im main.py gebraucht werden.
"""




"""
Das sind meine allgemeinen Speicher- und Lesefunktionen von Json Dateien
"""
def json_lesen(datei_name):
    try:
        with open(datei_name) as open_file:
            return json.load(open_file)
    except Exception:
        return []

def json_speichern(datei_name, datei_inhalt):
    with open(datei_name, "w") as open_file:
        json.dump(datei_inhalt, open_file, indent=4)




"""
Einer Person kann nicht 2x die gleiche Geschenkidee hinterlegt werden, 
dazu vergleiche ich den personen_name und die idee.
Ich gehe am Anfang davon aus, dass die Idee noch nicht vorhanden ist, 
deshalb False. Sobald der personen_name und die idee bereits vorhanden sind,
welchselt der Status auf True. Nun wird also die if Bedingung war, und somit ausgeführt.
"""
def idee_bereits_vorhanden(personen_name, idee):
    inhalt = json_lesen("geschenk_idee_formular.json")
    bereits_vorhanden = False
    for eintrag in inhalt:
        if eintrag["person"]== personen_name and eintrag["idee"] == idee:
            bereits_vorhanden = True
    return bereits_vorhanden


"""
überlegung:
Ich möchte alle hashtags und personen anzeigen.

Funktionsbeschreibung:
Zuerst brauche ich die aktuelle json Datei. Zurückgeben möchte ich eine Liste,
diese ist vorerst leer. In der for Schleife gehe ich alle Einträge durch, und speichere
alle values, die unter hashtag gespeichert sind und kein leerer String sind heraus. Ich 
speichere sie jeweils in der resultat Liste. Damit keine doppelten angezeigt werden mache ich eine
set liste, also alles nur einmal und für die Benutzerfreundlichkeit sortiere ich sie alphabetisch. 
"""
def hashtags_anzeigen():
    inhalt = json_lesen("geschenk_idee_formular.json")
    resultat = []
    for eintrag in inhalt:
        if eintrag["hashtag"] != "":
            resultat.append(eintrag["hashtag"])
    return sorted(list(set(resultat)))


def personen_anzeigen():
    inhalt = json_lesen("geschenk_idee_formular.json")
    resultat = []
    for eintrag in inhalt:
        if eintrag["person"] != "":
            resultat.append(eintrag["person"])
    return sorted(list(set(resultat)))




"""
Überlegung:
Ich möchte alle Einträge zurückgeben, die mit dem vom User angewählten
personen_name übereinstimmen.

Funktionsbeschreibung:
Wenn der personen_name kein leerer String ist, werden alle Einträge vom json
durchgegangen und sobald ein Value mit dem des personen_name übereinstimmt,
wird er der anfangs leeren Liste hinzugefügt, diese wird zurückgegeben.
Wenn kein personen_name übergeben wird, wird der gesamte Inhalt der json Datei zurückgegeben.
"""
def geschenke_anzeigen_fuer_person(personen_name):
    inhalt = json_lesen("geschenk_idee_formular.json")
    if personen_name != "":
        resultat = []
        for eintrag in inhalt:
            if eintrag["person"]== personen_name:
                resultat.append(eintrag)
        return resultat
    return inhalt



"""
Überlegung:
Alle ausgewählten Personen und ausgewählten Hashtags sollen zurückgegeben werden.
Es soll auch möglich sein nichts anzuwählen.

Funktionsbeschreibung:
Ich brauche dafür die Einträge der person, wenn nun im Wert hashtags (der aus den 
ausgewählten Hashtags besteht) etwas gespeichert ist, werden die Einträge durchgegangen.
Wenn ein Value mit einem der hashtags matcht, dann wird er in der resultat Liste gespeichert 
und diese zurückgeben.
Wenn in hashtags nichts gespeichert ist, werden die Einträge in person zurückgegeben.
"""
def geschenke_mit_hashtags(person, hashtags):
    if len(hashtags) > 0:
        resultat = []
        for eintrag in person:
            if eintrag["hashtag"] in hashtags:
                resultat.append(eintrag)
        return resultat
    return person



"""
Zählen, wie oft die Hashtags vorkommen
"""

def anzeige_hashtags():
    inhalt = json_lesen("geschenk_idee_formular.json")
    resultat = []
    for eintrag in inhalt:
        if eintrag["hashtag"] != "":
            resultat.append(eintrag["hashtag"])
    count = Counter(resultat)
    return count


"""
Darstellung des Barcharts
"""

def barchart(x_daten, y_daten, titel):
    fig = go.Figure(
        data=[go.Bar(x=x_daten, y=y_daten)],
        layout_title_text=titel
        )
    return plotly.offline.plot(fig, output_type="div")