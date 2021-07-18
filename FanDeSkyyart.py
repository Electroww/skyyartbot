import discord
import requests
from discord.ext import tasks
import json

# url = 'https://api.twitch.tv/helix/channels/?broadcaster_id=70298660'
#136494402
#url = 'https://api.twitch.tv/helix/streams?client_id=136494402&user_login=glayen'
url = 'https://api.twitch.tv/helix/channels/?broadcaster_id=70298660'
auth = { 'client-id': 'wi08ebtatdc7oj83wtl9uxwz807l8b'}

SKYYART_TITLE = ''
CHANNEL = 234749317443878912

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
    else :
        SKYYART_TITLE = data['data'][0]['title']
        print(SKYYART_TITLE)
        await channel.send(f"NOUVEAU TITRE DE STREAM DE **SKYYART LE 10E** 🥵🥵 \n**{SKYYART_TITLE}**")
        

client.run("NTU5NzcyNDE0Mjg0OTIyODgx.XJj-rw.Hy0HcMh62WZGwtBzfQmLnfBX9EY")
