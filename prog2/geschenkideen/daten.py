from datetime import datetime
import json


def speichern(person, idee, beschreibung, hashtag):
    try:
        with open('./geschenk_idee_formular.json') as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    #datei_inhalt[person][zeitpunkt] = {"Geschenkidee": idee, "Beschreibung": beschreibung, "Hashtag": hashtag}

    
    datei_inhalt[str(key)] = value

    
    print(datei_inhalt)

    with open('./geschenk_idee_formular.json', "w") as open_file:
        json.dump(datei_inhalt, open_file)


def formular_speichern(person, idee, beschreibung, hashtag):
    datei_name = "geschenk_idee_formular.json"
    zeitpunkt = datetime.now()
    speichern(person, idee, beschreibung, hashtag)
    return person, idee, beschreibung, hashtag 


def formular_laden():
    datei_name = "geschenk_idee_formular.json"

    try:
        with open(datei_name) as open_file:
            datei_inhalt = json.load(open_file)
    except FileNotFoundError:
        datei_inhalt = {}

    return datei_inhalt