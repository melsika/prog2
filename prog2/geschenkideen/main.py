
from flask import Flask
from flask import request
from flask import render_template
from json import loads, dumps
import daten

app = Flask("Geschenkidee")
app = Flask("Daten")

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



@app.route("/geschenkidee_erfassen")
def geschenk_erfassen():
  return render_template('geschenk_erfassen.html')



@app.route("/geschenkidee_suchen")
def geschenk_suchen():
    return render_template('geschenk_suchen.html')


@app.route("/ergebnis")
def ergebnis():
    return render_template('ergebnis.html')

"""--------------------------------------------"""
"""json"""
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
        open_file.write("erstes doku\n")
        open_file.write("zweite zeile\n")
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
    
    """json_als_string = dumps(geschenk_idee)
    geschenk_idee = loads(json_als_string)
""" 

@app.route("/einlesen")
def json_einlesen():
    with open('geschenk_idee.json') as open_file:
        json_als_string = open_file.read()
        mein_eingelesenes_dict = loads(json_als_string)

    return render_template("ergebnis.html", mein_eingelesenes_dict)



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
