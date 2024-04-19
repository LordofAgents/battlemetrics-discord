# battlemetrics-discord
Dieses Skript ist ein Discord-Bot, der den Status von Servern für das Spiel "Hell Let Loose" überwacht und die Spieleranzahl in einem Discord-Textkanal anzeigt.

Einrichtung
Installieren Sie Python (falls noch nicht installiert).
Klonen Sie dieses Repository oder laden Sie die bot.py-Datei herunter.
Erstellen Sie eine .env-Datei im selben Verzeichnis wie das Skript und fügen Sie die folgenden Umgebungsvariablen hinzu:
plaintext
Copy code
DISCORD_TOKEN=your_discord_bot_token
CHANNEL_ID=your_discord_channel_id
COUNTRY_ID=desired_country_code
RED_ON_PLAYERS=0
YELLOW_ON_PLAYERS=5
GREEN_ON_PLAYERS=50
DISCORD_TOKEN: Das Token Ihres Discord-Bots, das Sie im Discord Developer Portal erhalten haben.
CHANNEL_ID: Die ID des Discord-Textkanals, in dem die Serverinformationen angezeigt werden sollen.
COUNTRY_ID: Der Ländercode der Server, die überwacht werden sollen.
RED_ON_PLAYERS: Die Spieleranzahl, ab der der Server als rot markiert werden soll.
YELLOW_ON_PLAYERS: Die Spieleranzahl, ab der der Server als gelb markiert werden soll.
GREEN_ON_PLAYERS: Die Spieleranzahl, ab der der Server als grün markiert werden soll.
Installieren Sie die erforderlichen Python-Pakete, indem Sie pip install -r requirements.txt in Ihrer Befehlszeile oder Ihrem Terminal ausführen.
Starten Sie den Bot, indem Sie python bot.py in Ihrer Befehlszeile oder Ihrem Terminal ausführen.
Verwendung
Sobald der Bot gestartet ist, überwacht er automatisch die Server und aktualisiert die Spieleranzahl im angegebenen Discord-Textkanal.
Der Bot zeigt die Server nach Farben an: Rot für voll, Gelb für fast voll und Grün für verfügbar.
Hinweise
Stellen Sie sicher, dass der Bot über ausreichende Berechtigungen verfügt, um Nachrichten in den angegebenen Kanal zu senden und zu bearbeiten.
Überprüfen Sie die Konsole auf etwaige Fehlermeldungen während des Betriebs des Bots.
Lizenz
Dieses Projekt ist unter der MIT-Lizenz lizenziert. Weitere Informationen finden Sie in der Lizenzdatei.

Einrichtung des Discord-Bots
Um diesen Discord-Bot einzurichten, folgen Sie bitte diesen Schritten:

1. Erstellen eines Discord-Bots:
Öffnen Sie den Discord Developer Portal.
Klicken Sie auf "New Application" und geben Sie Ihrem Bot einen Namen.
Navigieren Sie zur Registerkarte "Bot" und klicken Sie auf "Add Bot".
Kopieren Sie das Token Ihres Bots, das unter dem Bot-Namen angezeigt wird. Dieses Token wird später benötigt, um den Bot auszuführen und mit Discord zu verbinden.
2. Konfiguration der Umgebungsvariablen:
Erstellen Sie eine Datei mit dem Namen .env im selben Verzeichnis wie das Skript bot.py.
Fügen Sie die folgenden Umgebungsvariablen in die .env-Datei ein und ersetzen Sie die Platzhalter durch Ihre eigenen Werte:
plaintext
Copy code
DISCORD_TOKEN=your_discord_bot_token
CHANNEL_ID=your_discord_channel_id
COUNTRY_ID=desired_country_code
RED_ON_PLAYERS=0
YELLOW_ON_PLAYERS=5
GREEN_ON_PLAYERS=50
DISCORD_TOKEN: Das Token Ihres Discord-Bots, das Sie im Discord Developer Portal erhalten haben.
CHANNEL_ID: Die ID des Discord-Textkanals, in dem die Serverinformationen angezeigt werden sollen.
COUNTRY_ID: Der Ländercode der Server, die überwacht werden sollen.
RED_ON_PLAYERS: Die Spieleranzahl, ab der der Server als rot markiert werden soll.
YELLOW_ON_PLAYERS: Die Spieleranzahl, ab der der Server als gelb markiert werden soll.
GREEN_ON_PLAYERS: Die Spieleranzahl, ab der der Server als grün markiert werden soll.
3. Ausführen des Discord-Bots:
Stellen Sie sicher, dass Sie Python installiert haben.
Installieren Sie die erforderlichen Python-Pakete, indem Sie pip install -r requirements.txt in Ihrer Befehlszeile oder Ihrem Terminal ausführen.
Starten Sie den Bot, indem Sie python bot.py in Ihrer Befehlszeile oder Ihrem Terminal ausführen.
4. Überprüfung der Funktionalität:
Überprüfen Sie die Konsole auf etwaige Fehlermeldungen und stellen Sie sicher, dass der Bot gestartet wurde.
Gehen Sie zu Ihrem Discord-Server und überprüfen Sie den angegebenen Textkanal. Der Bot sollte die Serverinformationen aktualisiert haben und die Spieleranzahl entsprechend anzeigen.
Nachdem Sie diese Schritte abgeschlossen haben, ist Ihr Discord-Bot einsatzbereit und überwacht die Spieleranzahl auf den angegebenen Servern.
