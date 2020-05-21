from datetime import datetime
import json
def json_speichern(datei_name, datei_inhalt):
    with open(datei_name, "w") as open_file:
        json.dump(datei_inhalt, open_file, indent=4)

def json_lesen(datei_name):
    try:
        with open(datei_name) as open_file:
            return json.load(open_file)
    except Exception:
        return []

def idee_bereits_vorhanden(personen_name, idee):
    inhalt = json_lesen("geschenk_idee_formular.json")
    bereits_vorhanden = False
    for eintrag in inhalt:
        if eintrag["person"]== personen_name and eintrag["idee"] == idee:
            bereits_vorhanden = True
    return bereits_vorhanden
            

def geschenke_anzeigen_fuer_person(personen_name):
    inhalt = json_lesen("geschenk_idee_formular.json")
    resultat = []
    for eintrag in inhalt:
        if eintrag["person"]== personen_name:
            resultat.append(eintrag)
    return resultat
    
 