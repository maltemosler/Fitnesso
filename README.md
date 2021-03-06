# Fitnesso 1.0

## Dokumentation:

**Table of Contents**

- [Entwurf eines Prototypen (Prototyp + Informationsarchitektur) aus den Personas und den User Storys](#Prototyp)
- [Kommentierung der Prototypen mit Gestaltgesetzen und Infos zu menschlichen Wahrnehmung](#Gestaltgesetze)
- [Kommentierung der Umsetzung des Prototypen mittels Entwurfsmuster](#Entwurfsmuster)
- [Erstellung eines Usability-Testkonzept für die Anwendung](#Usability-Testkonzept)


- [Framework](#framework)
- [Installation](#installation)
  * [Setup](#setup)
- [Unit-Tests](#unit-tests)
  * [Backend](#backend)
  * [Frontend](#frontend)
- [Ursprüngliche Backend Präsentation](#Präsentation)

# Prototyp

### Entwurf eines Prototypen (Prototyp + Informationsarchitektur) aus den Personas und den User Storys

Da Github die Bilder runter skaliert sind die Kommentare auf dem Bildern jeweils unter den Bildern aufgeführt.

## Prototype:

![prototype-1](Kommentare/pics/prototype/Index.png)
Die Login-Seite ist relative minimalistisch gestaltet, da der
Benutzer beim Besuchen der Webseite nicht mit
Informationen überladen werden soll.

Im Hintergrund läuft ein Fitnessvideo das als "Eyecatcher"
dient und dem Benutzer direkt vermittelt, dass es sich hierbei
um eine Fitness Webseite handelt.

Der Benutzer gibt bei dem Username seine E-Mail-Adresse
und das Passwort, welches er von dem Trainer erhalten hat,
ein. Danach wird er weiter auf die Seite mit den Zielen
geleitet.

Der Trainer loggt sich über die gleiche Seite ein. Hierbei wird
durch das Backend überprüft, ob es sich um einen Trainer oder
Nutzer handelt. Der Trainer wird danach auf die
Nutzerübersicht weitergeleitet. 
![prototype-2](Kommentare/pics/prototype/User-anzeigen.png)
Die Nutzerverwaltung bietet dem Trainer die Möglichkeit
eine Übersicht über alle Nutzer zu erhalten. Diese
Verwaltung dient als zentrale Seite für den Trainer.
Hierüber kann der Trainer die Stammdaten der Benutzer
sehen, den aktuellen Trainings Fortschritt, auf die Ziele der
Benutzer zugreifen, das Passwort ändern und den
Benutzer löschen.

Eine Suchfunktion erlaubt es dem Trainer Benutzer schnell
zu finden. Hierbei wird der Nutzer, auf den das
Suchkriterium zutrifft markiert, sodass der Trainer den
Nutzer schnell finden kann.

Die Ziele und die Passwortändern-Funktion können über
einen Knopf aufgerufen werden, wodurch der Trainer auf
die entsprechende Seite weitergeleitet wird.

Drückt der Trainer auf den Löschen-Knopf wird ein PopUp eingeblendet. In diesem PopUp wird der Trainer
erneut gefragt, ob er den Benutzer mit anzeige von vor,- und Nachnamen wirklich löschen möchte. Durch zwei
Knöpfe kann der Trainer die Löschung bestätigen oder
abbrechen. Dies dient zur Sicherheit, dass der Trainer
nicht aus Versehen einen Benutzer löscht.
![prototype-3](Kommentare/pics/prototype/Useranzeige-Löschen.png)
![prototype-4](Kommentare/pics/prototype/User-Passwort-zurücksetzen.png)
Eine der Hauptaufgaben, die der Trainer hat, ist es neue
Benutzer anzulegen.
Hierfür muss der Trainer den Vornamen, Nachnamen, die E-Mail und zweimal das
Passwort eingeben. Dabei wird überprüft, ob es sich bei der E-Mail um eine gültige E-Mail
(richtige Formation xxx@xxx.xx) handelt und ob das Passwort
den Anforderungen
 entspricht (8 Zeichen, mindestens ein Zeichen von jeder
Gruppe, Sonderzeichen,
Großbuchstaben, Zahlen und Kleinbuchstaben).

Sollte bei der Eingabe ein Fehler auftreten (Feld nicht
ausgefüllt, Eingabe entspricht nicht
den Anforderungen) wird dies dem Trainer angezeigt und die
Felder werden rot markiert.

Bei dem Passwort Feld wird zusätzlich der Hinweis
eingeblendet, welche Kriterien erfüllt
werden müssen. Sollte das eingeben Passwort vom Trainer
nicht mit diesen übereinstimmen.
![prototype-5](Kommentare/pics/prototype/User-anlegen.png)
Der Trainer muss die Möglichkeit haben das Passwort
vom Benutzer zurückzusetzen. Um auf diese Ansicht
zu kommen, muss der Trainer über die
Nutzerverwaltung auf Passwort zurücksetzen, bei
dem entsprechenden Benutzer, klicken. Danach wird
er auf diese Seite weitergeleitet. Dem Trainer wird
dabei angezeigt, um welchen Nutzer es sich handelt.
Dies dient zur Sicherheit, dass der Trainer nicht aus Versehen das falsche Passwort ändert.

Der Trainer gibt über diese Seite das neue Passwort
für den Benutzer ein. Hierbei greifen die gleichen
Passwortkriterien wie bei der Erstellung des Nutzer (8
Zeichen mit jeweils einem Zeichen aus einer
Zeichengruppe).

Sobald der Trainer auf Passwort zurücksetzen klickt, ist
das Passwort geändert und der Nutzer kann sich mit
dem neuen Passwort anmelden.
![prototype-6](Kommentare/pics/prototype/Ziele-Adminansicht.png)
Über der Benutzeransicht kann der Trainer
direkt die Ziele der einzelnen Benutzer
einsehen.

Hierbei wird dem Trainer angezeigt, um welchen Zielen von welchem Benutzer es sich handelt.
Der Trainer sieht immer die aktuell Stand der
jeweiligen Ziele des Benutzers und kann diese
genau so bearbeiten wie der Nutzer es tut.
Der Trainer kann neue Hauptziele erstellen und
dort unterziele mittels Eingabefeld erstellen.

Der Trainer kann durch verschiedene Buttons
Unterziele als erledigt markieren oder löschen.
Hauptziele lassen sich nur löschen. Unterhalb
der Box für das Hauptziel wird ein
Fortschrittsbalken angezeigt. Dieser füllt bzw.
senkt sich automatisch, sobald Unterziele
erledigt wurden oder hinzugefügt wurden.

Die Ansicht des Benutzers entspricht der
gleichen wie des Trainers nur mit dem
Unterschied das der Benutzer nicht seinen
eigenen Namen angezeigt bekommt und nur
auf seine Ziele zugriff hat.
![prototype-7](Kommentare/pics/prototype/Ziele-Useransicht.png)
Über der Benutzeransicht kann der Trainer
direkt die Ziele der einzelnen Benutzer
einsehen.

Hierbei wird dem Trainer angezeigt, um welche
Ziele von welchem Benutzer es sich handelt.
Der Trainer sieht immer die aktuell Stand der
jeweiligen Ziele des Benutzers und kann diese
genau so bearbeiten wie der Nutzer es tut.
Der Trainer kann neue Hauptziele erstellen und
dort unterziele mittels Eingabefeld erstellen.

Der Trainer kann durch verschiedene Buttons
Unterziele als erledigt markieren oder löschen.
Hauptziele lassen sich nur löschen. Unterhalb
der Box für das Hauptziel wird ein
Fortschrittsbalken angezeigt. Dieser füllt bzw.
senkt sich automatisch, sobald Unterziele
erledigt wurden oder hinzugefügt wurden.
Die Ansicht des Benutzers entspricht der
gleichen wie des Trainers nur mit dem
Unterschied das der Benutzer nicht seinen
eigenen Namen angezeigt bekommt und nur
auf seine Ziele zugriff hat.

## Informationsarchitektur:

![img_6.png](Kommentare/pics/img_6.png)

# Gestaltgesetze
### Kommentierung der Prototypen mit Gestaltgesetzen und Information zu menschlichen Wahrnehmung

Gestaltgesetz der Ähnlichkeit: Ziele sind immer gleich aufgebaut und haben die gleichen Funktionen

![img_10.png](Kommentare/pics/img_10.png)

Gestaltgesetz der Ähnlichkeit: Alle input Felder sind gleich aufgebaut und funktionieren gleich.

![img_8.png](Kommentare/pics/img_8.png)

##### Gestaltgesetze Symmetrie: 
Alle Anzeigen auf der Website sind zentriert.

##### Gestaltgesetze der Nähe: 
Die input Felder sind nah untereinander angeordnet da diese zusammengehören und auch als solches empfunden werden sollen. Dieses Gestaltungsgesetz wird durch das Gestaltungsgesetz der Gemeinsamen Region unterstützt bzw. verstärkt.

##### Gestaltgesetze Gemeinsame Region: 
Ziele und Forms sind mit einem Kasten umrundet. Die Webseite ist nach dem bekannten Kachel-Design aufgebaut.
Fitts‘ Gesetz: Alle Knöpfe und Eingabefelder sind leicht zu treffen.

##### Millersche Gesetz / Hickesches Gesetz:  
Die beiden Gesetze beziehen sich auf die Aufmerksamkeit der User. Die Website wurde so aufgebaut, dass nicht zu viel angezeigt wird und der User auch nur die Optionen hat, die er auch wirklich braucht.
Gestaltgesetz verbundene Elemente: Bei der User Verwaltung wird das Gesetz der verbundenen Elemente in Form einer Tabelle benutzt. In jeder Zeile steht ein User und die Einträge in der Zeile sind genau dem User zugeordnet.

![img_11.png](Kommentare/pics/img_11.png)

## ISO 9241 
##### Aufgabenangemessenheit: 
Die Aufgabe der Webseite, anhand der User Stories, ist es das der Trainer einfach Nutzer hinzufügen kann und deren Fortschritt leicht kontrollieren und anpassen kann.  

##### Selbstbeschreibungsfähigkeit: 
Dem Nutzer wird durch eine Überschrift angezeigt, in welchem Dialog er sich befindet. Zusätzlich wurde die Handlung die der Nutzer in den eigenen Dialogen vornehmen kann auf das minimalste reduziert, um den Nutzer nicht zu "verwirren".

##### Steuerbarkeit: 
Sobald der Nutzer einen Dialog z.B. Nutzer anlegen öffnet, kann der Nutzer jederzeit diesen Dialog beenden und die Geschwindigkeit hängt von den Eingaben des Nutzers ab. Es gibt kein Zeitlimit für die Eingabe.

##### Erwartungskonformität: 
Sämtliche Eingabefelder, Menüpunkte und Button verhalten sich so wie man es gewohnt ist (z. B. Login Seite). 

##### Fehlertoleranz: 
Wenn der Nutzer eine fehlerhafte Eingabe bei einem input Feld macht, wird dieses Rot angezeigt. Der Nutzer muss dann lediglich das Eingabefeld mit dem fehlerhaften Eintrag korrigieren, die richtigen Einträge werden gespeichert und müssen nicht nochmal eingegeben werden.

##### Individualisierbarkeit: 
Das System ist zu einem gewissen Grad individualisierbar, der Nutzer kann über den Freitext der Ziele die Darstellung von Informationen ändern und somit an seine individuellen Fähigkeiten und Bedürfnisse anpassen.


# Entwurfsmuster
### Kommentierung der Umsetzung des Prototypen mittels Entwurfsmuster

Ein wichtiges Design Pattern ist der Decorator. Der Decorator ist ein Strukturmuster, welches einen ermöglicht, Objekten dynamisch neue Verhaltensweisen hinzuzufügen. 
In unserem Fall werden diese Decorator benutzt:

    @require_http_methods(["POST"])
    @transaction.atomic
    @validate_goal_user_rights

Der erste decorator limitiert Methoden auf bestimmte request Methoden, in diesem Fall darf die Methode nur mittels POST request aufgerufen werden.
Der zweite decorator gibt an, das alles in der Methode eine transaction ist, also wenn etwas schiefgeht wird die Datenbank auf den Ursprungszustand zurückgesetzt.
Der dritte decorator ist selber geschrieben, und wird für alle Aktionen der Ziele genutzt. 
Dort wird geprüft, ob der Antragsteller der Änderung entweder der Besitzer der Ziele ist oder ob es ein Trainer war.

# Usability-Testkonzept
### Erstellen ein Usability-Testkonzept für die Anwendung

Das Testkonzept ist relativ simpel. Wir erklären den Nutzer nichts, sondern lassen ihn selber die Webseite erkunden. Dabei wird getrackt, wie lange er für bestimmte Aufgaben braucht. Sobald bei dem Nutzer frustation aufkommt oder er aus unserer Sicht zu lange für eine Aufgabe braucht, wurden A/B Tests erstellt, also Variationen zur Ursprungsversion. Sollte die neue Version die erkannten Probleme beheben bzw. beschleunigen, dann wird diese eingebaut.

### A/B-Tests

## Test 1
![img_3.png](Kommentare/pics/img_3.png)
Beim Testen mit anderen Nutzern ist aufgefallen, dass das Erkennen der Fehler beim Registrieren zu lange dauert. Dabei wurde die Concurrent Think Aloud (CTA) verwendet: Nutzer haben nach dem sie den Button „Nutzer anlegen“ gedrückt haben sich gefragt, woran es liegt, weil es nicht offensichtlich war.
Aus diesem Grund wurde hier eine Variation mit roter Schrift erstellt. Beide Tests wurden mit 10 Personen durchgeführt, wovon 5 mit A und 5 mit B angefangen haben. 
Dabei hat sich herausgestellt, dass A im Durchschnitt eine Zeit von 51,3 Sekunden gedauert hat und B im Durchschnitt 44,9 Sekunden. Das bedeutet, B ist um 6,4 Sekunden (~13 %) schneller.

![img_5.png](Kommentare/pics/img_5.png)

## Test 2
![img_4.png](Kommentare/pics/img_4.png)
Auch hier ist erst beim Start der ersten Tests aufgefallen, das etwas fehlt. Eine Suchleiste. 
Sollten mal viele Nutzer existieren ist diese erforderlich. Ohne einen Test analysieren zu müssen, ist hier klar das B schneller ist. Wurde dennoch in der Entwicklung vergessen und ist erst bei den Usability-Tests aufgefallen.

# Dokumentation

## Framework:

Als Framework wird Django3 (3.13) verwendet.

### Warum Django?

Das Framework bringt standardmäßig eine SQLite Datenbank mit. Diese Datenbank lässt sich in Python erstellen (`API/models.py`) und das Framework ist zuständig für die Verwaltung / Übersetzung.

![django_model_view.png](Kommentare/pics/django_model_view.png)

Kurzbeschreibung der Grafik: Bei einem Request wird der Python Code (view) aufgerufen und die benötigten Daten werden aus der Datenbank geladen.

Aufgrund der Möglichkeit zur schnellen und effizienten Umsetzung von Projekten, wird das Django-Webframework häufig als "Das Webframework für Perfektionisten mit Deadlines" bezeichnet.
(https://www.hosteurope.de/blog/8-gruende-warum-sie-das-quelloffene-django-webframework-nutzen-sollten/)

Aus welchen Gründen wird das Framework so bezeichnet?
  
  - Standardisierte Struktur
  - Eingebaute Sicherheitskonzepte (Standardmäßig sicher)
  - REST Framework (API)
  - Projekte aufteilbar in Teilprojekte (Django Apps)
  - Abwärtskompatibel

Mögliche Nachteile:

  - Entwicklung des Frameworks erfolgt langsam, aufgrund der Abwärtskompatibilität


Dank Django lassen sich zusätzlich im HTML Code *schleifen* und *if* abfragen erstellen, was den Arbeitsaufwand um einiges reduziert.
So muss man nicht beim Laden der Seite noch zusätzlich die Daten via Javascript laden lassen. 

Beispiel if:

    {% if not request.user.is_authenticated %}
      You need to login
    {% endif %}


Beispiel Schleife:

    {% for ziel in ziele %}
      Ziel: {{ ziel.ziel }}
      Status: {{ ziel.status }}
    {% endfor %}

Ansonsten wird normales Javascript + HTML verwendet und ist deshalb auch das Framework für dieses Projekt.

Zum Erstellen, Löschen (…) eines Ziels wird beispielsweise ein POST request (AJAX) an den Webserver gesendet. 

Alle Schnittstellen sind bei `Fitnesso/urls.py` zu finden.
Alle HTML Templates sind bei `API/templates/`
Javascript + CSS ist bei `static/js/` und `static/css/`.

Django Docs:
https://docs.djangoproject.com/en/3.1/

### Zusätzliche Abhängigkeiten: 

##### Fontawesome (https://fontawesome.com/):

Hier wurden die Vector Icons für die Webseite geholt. Wieso Vector? Vector Grafiken sind skalierbar, sehen auf jeder größe also gut aus.

##### JQuery (https://jquery.com/):

Dank JQuery lassen sich AJAX anfragen an den Webserver stellen und es lässt sich sehr einfach auf Elemente zugreifen: `$("#register-email").val()`
mit diesem kurzen Befehl bekommt man den Wert eines Input Feldes.

## Installation


Python 3.9 wurde in der Entwicklung verwendet, weswegen diese Version empfohlen wird.
Python 3.6 oder höher wird benötigt um diese Anwendung ausführen zu können.

Nachdem Python installiert wurde, können Sie die unten stehenden Befehle ausführen:

#### Setup

    pip install django -U
    
    python manage.py makemigrations API
    python manage.py migrate 
  
    # Please write your email when the command below ask for the username
    python manage.py createsuperuser 
    

Run:

    python manage.py runserver

Aufgerufen kann die Webseite dann standardmäßig mit: http://127.0.0.1:8000/

Getestete Browser:
  - Chrome
  - Firefox
  - Edge

Bei allen Browsern funktioniert die Webseite ohne nennenswerte Probleme. 
In Firefox ist es bei der Login Seite möglich das hintergrund Video zu minimieren, ist jedoch unserer Auffassung nach nicht relevant, da keine Funktionalitäten einschränkt werden. 

## Unit-Tests:

Unser Testkonzept sieht Backend und Frontend tests vor. 

#### Backend:

Um die Schnittstellen zu testen, werden Daten benötigt. 
Aus diesem Grund wird eine Datenbank "gemockt", also eine temporäre Datenbank erstellt, welche Test Daten enthält und nur während des Tests verfügbar ist.

Jede Schnittstellen wird mit mindestens zwei Tests getestet. Ein Test, welcher falsche Daten sendet und damit ein ServerError hervorruft und einer, welcher richtige Daten sendet und somit schaut ob der HTTP Response Code 200 ist.

Die Tests sind zu finden bei: `API/tests.py`


#### Frontend:

Da die Schnittstellen bereits im Backend getestet werden, wird nur getestet, ob die Javascript Validation erfolgreich ist oder nicht.

Da hier nur dummy Werte eingesetzt werden, wird die antwort des Servers ignoriert.

Die tests sind zu finden bei: `static/js/tests.js`


URL: http://127.0.0.1:8000/tests/-1

Die -1 in der URL ist eine DummyID. Jeder User hat eine eindeutige positive ID. Somit lassen sich die Javascript tests durchführen,
ohne einen richtigen User zu nehmen.

# Ursprüngliche Backend Präsentation

Hier die alte Präsentation, welche auf das Backend (PROTOTYPE + Vorstellung der Webseite fehlte noch) einging, is auch nutzbar für die Doku, sollte einen guten Gesamtüberblick über das Backend geben:

![img.png](Kommentare/pics/pp/imgthumb.png)
![img_1.png](Kommentare/pics/pp/img_1.png)
![img_2.png](Kommentare/pics/pp/img_2.png)
![img_3.png](Kommentare/pics/pp/img_3.png)
![img_4.png](Kommentare/pics/pp/img_4.png)
![img_5.png](Kommentare/pics/pp/img_5.png)
![img_6.png](Kommentare/pics/pp/img_6.png)
![img_7.png](Kommentare/pics/pp/img_7.png)
![img_8.png](Kommentare/pics/pp/img_8.png)
![img_9.png](Kommentare/pics/pp/img_9.png)
![img_10.png](Kommentare/pics/pp/img_10.png)
![img_11.png](Kommentare/pics/pp/img_11.png)
