import requests
import os
import json

APP_ID = "1142572072338456616"
SERVER_ID = "633901394352537607"
try:
  BOT_TOKEN = os.environ['BOT_TOKEN']
except:
  f = open('./secrets/discord_bot.json')
  data = json.load(f)
  BOT_TOKEN = data['bot_token']
  f.close()

# global commands are cached and only update every hour
# url = f'https://discord.com/api/v10/applications/{APP_ID}/commands'

# while server commands update instantly
# they're much better for testing
url = f'https://discord.com/api/v10/applications/{APP_ID}/guilds/{SERVER_ID}/commands'

json = [
  {
    'name': 'bleb',
    'description': 'Test command.',
    'options': []
  }
]

response = requests.put(url, headers={
  'Authorization': f'Bot {BOT_TOKEN}'
}, json=json)

print(response.json())