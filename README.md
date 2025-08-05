# # QR-Generator

# So funktioniert's in der Praxis <- Muss nur das erste mal gemacht werden.
```bash
# 1. Projektordner anlegen
mkdir mein_projekt
cd mein_projekt

# 2. Virtuelle Umgebung erstellen
python3 -m venv venv

# 3. Aktivieren
source venv/bin/activate

# 4. Abhängigkeiten installieren
pip install -r requirements.txt

# Falls requirements.txt noch nicht existiert, kannst du sie selbst erstellen oder mit pip freeze generieren:
pip freeze > requirements.txt  
```

# Verwendung: <- bei jeder Verwendung
### Anfang:
```bash
- cd mein_projekt
# source venv/bin/activate       # auf der bash-shell
- source venv/bin/activate.fish  # auf der fish-shell
- python main.py
```

### Ende:
```bash
- deactivate
```

# Mit VS-Code:
```bash
# in das Verzeichniss wechseln
cd mein_projekt

# die .py mit VS-Code öffnen, es wird dann in VS-Code rechts unten automatisch die venv angezeigt

## Beenden des Programms, beendet auch die venv.
```
