import discord
import requests
from discord.ext import tasks
import json
from decouple import config

url = 'https://api.twitch.tv/helix/channels/?broadcaster_id=70298660'
auth = { 'client-id': config('CLIENT_ID')}

SKYYART_TITLE = ''
CHANNEL = config('CHANNEL')

client = discord.Client()

@client.event
async def on_ready():
    print("Skyyart Bot est prêt !")
    title_update.start()

@tasks.loop(seconds=300)
async def title_update():
    global SKYYART_TITLE 
    response = requests.get(url, headers = auth)
    data = response.json()
    channel = client.get_channel(CHANNEL)
    if (SKYYART_TITLE == data['data'][0]['title']):
        print('Aucun changement de titre fuck code createur SKYYART')
    else:
        SKYYART_TITLE = data['data'][0]['title']
        print(SKYYART_TITLE)
        await channel.send(f"NOUVEAU TITRE DE STREAM DE **SKYYART LE 10E** 🥵🥵 \n**{SKYYART_TITLE}**")
        

client.run(config('TOKEN'))
