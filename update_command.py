import requests
import os
import logging as log
import json

log.getLogger().setLevel(log.INFO)

def update_command_list(event, lambda_context):
  log.info(f'{event = }')
  log.info(f'{lambda_context = }')
  try:
    APP_ID = os.environ['APP_ID']
    SERVER_ID = os.environ['SERVER_ID']
    BOT_TOKEN = os.environ['BOT_TOKEN']
  except:
    f = open('./secrets/discord_bot.json')
    data = json.load(f)
    BOT_TOKEN = data['bot_token']
    APP_ID = data['app_id']
    SERVER_ID = data['server_id']
    f.close()

  # global commands are cached and only update every hour
  # url = f'https://discord.com/api/v10/applications/{APP_ID}/commands'

  # while server commands update instantly
  # they're much better for testing
  url = f'https://discord.com/api/v10/applications/{APP_ID}/guilds/{SERVER_ID}/commands'

  command_list = [
    {
      'name': 'bleb',
      'description': 'Test command.',
      'options': []
    },
    {
      'name': 'next-event',
      'description': 'Return the next upcoming event.',
      'options': [
        {
          'name': 'osu',
          'description': 'Return the next upcoming event for Ohio State.',
          'type': 1
        }
      ]
    }
  ]

  response = requests.put(url, headers={
    'Authorization': f'Bot {BOT_TOKEN}'
  }, json=command_list)

  log.info(response.json())
  log.info(f'{response.status_code = }')
  return {
    'statusCode': 200,
    'body': response.json()
  }

if __name__ == '__main__':
  update_command_list()