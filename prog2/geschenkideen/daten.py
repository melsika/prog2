
import json

# Das sind meine allgemeinen Speichern- und Lesefunktionen von Json Dateien
def json_speichern(datei_name, datei_inhalt):
    with open(datei_name, "w") as open_file:
        json.dump(datei_inhalt, open_file, indent=4)

def json_lesen(datei_name):
    try:
        with open(datei_name) as open_file:
            return json.load(open_file)
    except Exception:
        return []


"""
Einer Person kann nicht 2x die gleiche Geschenkidee hinterlegt werden, 
dazu vergleiche ich den namen und die idee.
Ich gehe am Anfang davon aus, dass die Idee noch nicht vorhanden ist, 
deshalb False, dann prüfe ich und gebe zurück, dass das nicht möglich ist.
"""
def idee_bereits_vorhanden(personen_name, idee):
    inhalt = json_lesen("geschenk_idee_formular.json")
    bereits_vorhanden = False
    for eintrag in inhalt:
        if eintrag["person"]== personen_name and eintrag["idee"] == idee:
            bereits_vorhanden = True
    return bereits_vorhanden 
    #WIESO hier bereits_vorhanden? im return?
            

"""
In meine leere resultat Liste werden die gesuchten Personen hinzugefügt 
"""
def geschenke_anzeigen_fuer_person(personen_name):
    inhalt = json_lesen("geschenk_idee_formular.json")
    if personen_name != "":
        resultat_person = []
        for eintrag in inhalt:
            if eintrag["person"]== personen_name:
                resultat_person.append(eintrag)
        return resultat_person
    return inhalt



"""
Hier suche ich nach allen Einträgen, die diesen hashtag gespeichert haben.
"""
def hashtags_anzeigen():
    inhalt = json_lesen("geschenk_idee_formular.json")
    resultat = []
    for eintrag in inhalt:
        resultat.append(eintrag["hashtag"])
    return list(set(resultat))


def geschenke_mit_hashtags(geschenke, hashtags):
    if len(hashtags) > 0:
        resultat = []
        for eintrag in geschenke:
            if eintrag["hashtag"] in hashtags:
                resultat.append(eintrag)
        return resultat
    return geschenke