# Fitnesso 1.0

Kann removed werden wenn in Readme aufgenommen:

##### Entwurf eines Prototypen (Prototyp + Informationsarchitektur) aus den Personas und den User Storys:

    ./Kommentare/Entwurf

##### Kommentierung der Prototypen mit Gestaltgesetzen und Infos zu menschlichen Wahrnehmung:

    ./Kommentare/Kommentierung-Prototypen

##### Kommentierung der Umsetzung des Prototypen mittels Entwurfsmuster:

    ./Kommentare/Kommentierung-Umsetzung

##### Erstellen ein Usability-Testkonzept für die Anwendung:

    ./Kommentare/Usability-Testkonzept

## Dokumentation:

**Table of Contents**

- [Entwurf eines Prototypen (Prototyp + Informationsarchitektur) aus den Personas und den User Storys](#todo)
- [Kommentierung der Prototypen mit Gestaltgesetzen und Infos zu menschlichen Wahrnehmung](#todo)
- [Kommentierung der Umsetzung des Prototypen mittels Entwurfsmuster](#todo)
- [Erstellen ein Usability-Testkonzept für die Anwendung](#todo)


- [Framework](#framework)
- [Installation](#installation)
  * [Setup](#setup)
- [Unit-Tests](#unit-tests)
  * [Backend](#backend)
  * [Frontend](#frontend)
- [Wie funktioniert der Code?](#sourcecode)


## Framework:

Als Framework wird Django3 (3.13) verwendet.

### Warum Django?

Das Framework bringt standardmäßig eine SQLite Datenbank mit. Diese Datenbank lässt sich in Python erstellen (`API/models.py`) und das Framework kümmert sich um die Verwaltung / Übersetzung.
Bei einem Request wird der Python Code aufgerufen und die benötigten Daten aus der Datenbank geladen.

Dank Django lassen sich zusätzlich im HTML Code "schleifen" und "if" abfragen erstellen, was den Arbeitsaufwand um einiges reduziert.
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

Ansonsten wird normales Javascript und HTML verwendet und ist deshalb auch das Framework für dieses Projekt.

Zum Erstellen, Löschen (...) eines Ziels wird beispielsweise ein POST request (AJAX) an den Webserver gesendet. 

Alle Schnittstellen sind bei `Fitnesso/urls.py` zu finden.
Alle HTML Templates sind bei `API/templates/`
Javascript und CSS ist bei `static/js/` und `static/css/`.

Django Docs:
https://docs.djangoproject.com/en/3.1/


## Installation

You need to install Python 3.6 or higher to run this application. 
After installing python you can follow the steps below

#### Setup

    pip install django -U
    
    python manage.py makemigrations API
    python manage.py migrate 

    python manage.py createsuperuser 
    

Run:

    python manage.py runserver localhost:8080



## Unit-Tests:

Unser Testkonzept sieht Backend und Frontend tests vor. 

#### Backend:

Um die Schnitstellen zu testen werden Daten benötigt. 
Aus diesem Grund wird eine Datenbank "gemockt", also eine temporäre Datenbank erstellt welche Test Daten enthält und nur während des Tests verfügbar ist.

Jede Schnittstellen wird mit mindestens zwei tests getestet. Ein Test welcher falsche Daten sendet und damit ein ServerError hervorruft und einer welcher richtige Daten sendet und somit schaut ob der HTTP Response Code 200 ist.

Die tests sind zu finden bei: `API/tests.py`


#### Frontend:

Da die Schnittstellen bereits im Backend getestet werden, wird nur getestet, ob die Javascript Validation erfolgreich ist oder nicht.

Da hier nur dummy Werte eingesetzt werden, wird die antwort des Servers ignoriert.

Die tests sind zu finden bei: `static/js/tests.js`

http://127.0.0.1:8000/tests/-1

## Sourcecode:

...


Formatting:

https://gist.githubusercontent.com/jonschlinkert/ac5d8122bfaaa394f896/raw/bd1106691cf344e972f575c49ba3cf281beeb9b3/markdown-toc_repeated-headings.md