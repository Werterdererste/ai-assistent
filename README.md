# AI ASSISTENT

Dieses Project ist im Rahmen einer schulaufgaben entstanden.

Zielsetzung dieses projektes ist es ein Ai Assistent, zu erstellen mit dem man Sprächen kann.
In etwa wie Alexa, Siri oder Googel.
Jedoch offline mittels einer local laufenden LLM (aktuell noch google speach to text).
Zudem gibt es auch einen text chat im terminal und eine web interface.


Es ist möglich sich das auch auf einen eigenen raspberry pi zu installieren und zu benutzen.
Hierzu folgende anleitung lesen und beachten.

# Benötigt
1. Raspberry pi
entwickelt und getestet auf einem Raspberry pi 4 2gb
jedoch ist ein besseres raspberry empfehlenswert.
2. Aktive Kühlung
wehrend des betriebs wird der raspberry zwangsläufig sehr heiß daher ist eine kühlung **NOTWENDIG**.
3. Headset
    alternative auch
   - Lautsprecher
   - Microphone
5. RGB LED
6. 3 * Wiederstände 220Ohm (je nach led)
7. 1 * Wiederstand (button)


# Einrichtung
## Installation
```bash
chmod o+x ./install.sh
./install.sh

virtual venv
source venv/bin/activate
pip install -r requirements.txt

python3 main.py --help
```

## Verdrahtung
Schließe eine RGB led an den raspberry pi an mit massenden Vorweideständen.
Ebenfalls einen button. Geb die Pins, falls es nicht die standard (R = 22, G = 24, B = 26, Button = 37) pins sind  beim Ausführen als argumente an.

22-W-LedR-|
24-W-LedG-|-G
26-W-LedB-|

37-W-Button-G

Auf ein steckbrett oder verlöten.

# Benutzung
nachdem alles so weit Verdrahtet und installiert wurde kann man auch schon anfangen.
Hier sind ein paar beispiele für die minimale bedienung.

### sprach assistent
```bash
python3 main.py -s
```

### web assistent
```bash
python3 main.py -w
```

### web assistent
```bash
python3 main.py -c
```

### get help
```bash
python3 main.py --help
```

# Fehler oder Verbesserung vorschläge
Sollten sie irgendwelche fehler, bugs Sicherheitslücken finden oder verbesserungsvorschläge haben würde ich mich über eine rückmeldung in den Issues sehr freuen. 


