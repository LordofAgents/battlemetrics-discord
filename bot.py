import discord
from discord.ext import commands, tasks
import requests
from dotenv import load_dotenv
import os
import time

# Lade die Umgebungsvariablen aus der .env Datei
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))
RED_ON_PLAYERS = os.getenv('RED_ON_PLAYERS')
YELLOW_ON_PLAYERS = os.getenv('YELLOW_ON_PLAYERS')
GREEN_ON_PLAYERS = os.getenv('GREEN_ON_PLAYERS')

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

last_message = None  # Zum Speichern der letzten Nachrichten-ID

def fetch_servers():
    url = "https://api.battlemetrics.com/servers"
    params = {
        "filter[search]": "GER",
        "filter[game]": "hll",
        "sort": "-players"
    }
    while True:
        try:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Fehler beim Abrufen der Serverdaten: {response.status_code}. Versuche es erneut in 60 Sekunden.")
                time.sleep(60)
        except requests.exceptions.RequestException as e:
            print(f"Fehler bei der Netzwerkverbindung: {e}. Versuche es erneut in 60 Sekunden.")
            time.sleep(60)

async def clear_channel(channel):
    """ Löscht alle Nachrichten in einem Kanal. """
    try:
        deleted = await channel.purge(limit=None)
        print(f"Deleted {len(deleted)} message(s)")
    except Exception as e:
        print(f"Error while trying to delete messages: {str(e)}")

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await clear_channel(channel)
    update_servers.start()

@tasks.loop(seconds=10)
async def update_servers():
    global last_message
    channel = bot.get_channel(CHANNEL_ID)
    if channel is not None:
        data = fetch_servers()
        if data and "data" in data:
            message_content = []
            previous_was_kampfschweine = False
            for index, server in enumerate(data["data"], start=1):
                server_name = server["attributes"]["name"].replace('.', '.\u200B')
                players = server["attributes"]["players"]
                max_players = server["attributes"]["maxPlayers"]
                # Symbole festlegen
                if "TRÜMMERTRUPPE" in server_name.upper():
                    circle = "💯"
                else:
                    if players >= GREEN_ON_PLAYERS:
                        circle = "🟢"  # Grüner Kreis
                    elif players >= YELLOW_ON_PLAYERS:
                        circle = "🟡"  # Gelber Kreis bei weniger als 3 Spielern
                    else:
                        circle = "🔴"  # Rot
                message_content.append(f"{index}. {circle} {players}/{max_players} Spieler - {server_name}")
            message_content = '\n'.join(message_content)
            if last_message:
                try:
                    msg = await channel.fetch_message(last_message)
                    await msg.edit(content=message_content)
                except discord.NotFound:
                    msg = await channel.send(message_content)
                    last_message = msg.id
            else:
                msg = await channel.send(message_content)
                last_message = msg.id
        else:
            if last_message:
                try:
                    msg = await channel.fetch_message(last_message)
                    await msg.edit(content="Keine Server gefunden.")
                except discord.NotFound:
                    msg = await channel.send("Keine Server gefunden.")
                    last_message = msg.id
            else:
                msg = await channel.send("Keine Server gefunden.")
                last_message = msg.id

bot.run(TOKEN)
