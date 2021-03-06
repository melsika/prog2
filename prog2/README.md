# Projekt Idee
**Geschenkideen speichern**


## Ausgangslage
Ganz oft kommt es vor, dass ich vor Weihnachten oder einem Geburtstag keine Geschenkidee habe. Es wäre deshalb super, während des Jahres mögliche Ideen zu speichern, um diese vor dem Event abrufen zu können.

## Funktion / Projektidee
Die Webapplikation soll Geschenke erfassen und es erlauben, nach diesen zu suchen. Die Suchmöglichkeit soll für den Namen und Hashtags möglich sein.


## Installationsanleitung
Für die korrekte Ausführung der Webapplikation muss Flask und Plotly installiert werden. Nachdem der Ordner von Github heruntergeladen wurde, kann man ihn ativieren mit activate prog2. Danach findet man im Ordner Geschenkideen die main.py Datei. Diese kann mit dem Befehl python main.py gestartet werden.


## Workflow
**Erfassen einer Geschenkidee**
- Erfassen der Person
- Notieren der Geschenkidee
- Hinzufügen einer Beschreibung
- Aufführen eines Hashtags

**Suchen einer Geschenkidee**
- Auswählen einer Person
- Ankreuzen der Hashtags


### Dateneingabe
Einem neuen Eintrag können folgende Merkmale hinzugefügt werden.
- Person
- Geschenkidee
- Beschreibung
- Hashtag

### Datenverarbeitung / Speicherung
Es wird mit zwei Python Dateien gearbeitet, in der daten.py sind alle Hilfsfunktionen gespeichert, während das main.py diese verlinkt und zusammensetzt.
Alle Einträge werden mit Json abgespeichert, die Struktur ist hier zu erkennen.
![Image](./json_struktur.png)

### Datenausgabe
Die gespeicherten Einträge werden aus dem Json ausgelesen und ausgegeben.

## Flussdiagramm
Als User hat man die Möglichkeit, Geschenkideen zu Erfassen und nach ihnen zu Suchen. 

![Diagramm](./flussdiagramm.png)

## Datenflussdiagramm
Wie hier zu sehen ist, ist die Json Datei sehr zentral. Alle Seiten der Webapplikation greifen auf diese zu. Sei dies beim Speichern eines neuen Eintrages, beim Suchen nach einer Geschenkidee oder für die Anzeige des Barchart auf der Homeseite.

![Daten](./datenflussdiagramm.png)
