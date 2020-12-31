# Fitnesso 1.0

## Dokumentation (Englisch + Deutsch (Denglisch))

### Installation

You need to install Python 3.6 or higher to run this application. 
After installing python you can follow the steps below

#### Setup

    pip install django -U
    
    python manage.py makemigrations API
    python manage.py migrate 

    python manage.py createsuperuser 
    

Run:

    python manage.py runserver localhost:8080

## Testkonzept:

Unser Testkonzept sieht Backend und Frontend tests vor. 

#### Backend:

Um die Schnitstellen zu testen werden Daten benötigt. 
Aus diesem Grund wird eine Datenbank "gemockt", also eine temporäre Datenbank erstellt welche Test Daten enthält und nur während des tests verfügbar ist.

Jede Schnittstellen wird mit mindestens zwei tests getestet. Ein Test welcher falsche daten sendet und damit ein ServerError hervorruft und einer welcher richtige Daten sendet und somit schaut ob der HTTP Response Code 200 ist.

Die tests sind zu finden bei: API/tests.py


#### Frontend:

Die tests sind zu finden bei: static/js/tests.js