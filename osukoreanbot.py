import json
import logging as log
import os

from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError

from next_command import next_command

try:
  PUBLIC_KEY = os.environ['PUBLIC_KEY']
except:
  f = open('./secrets/discord_bot.json')
  data = json.load(f)
  PUBLIC_KEY = data['public_key']
  f.close()

def lambda_handler(event, lambda_context):
  log.info(f'{event = }')
  log.info(f'{lambda_context = }')
  try:
    verify_key = VerifyKey(bytes.fromhex(PUBLIC_KEY))

    signature = event['headers']["x-signature-ed25519"]
    timestamp = event['headers']["x-signature-timestamp"]
    body = event['body']

    try:
      verify_key.verify(f'{timestamp}{body}'.encode(), bytes.fromhex(signature))
      body = json.loads(event['body'])
    except BadSignatureError as e:
      log.error(f'BadSignatureError raised. {e}')
      return {
        'statusCode': 401,
        'body': json.dumps('Invalid request signature')
      }

    # handle the interaction

    t = body['type']

    if t == 1:
      return {
        'statusCode': 200,
        'body': json.dumps({
          'type': 1
        })
      }
    elif t == 2:
      return command_handler(body)
    else:
      msg = f'Invalid request type: {t}'
      log.error(msg)
      return {
        'statusCode': 400,
        'body': json.dumps(msg)
      }
  except:
    msg = 'Invalid event structure'
    log.error(msg)
    return {
      'statusCode': 400,
      'body': json.dumps(msg)
    }

def command_handler(body):
  command = body['data']['name']

  if command == 'bleb':
    return {
      'statusCode': 200,
      'body': json.dumps({
        'type': 4,
        'data': {
          'content': 'Hello, World.',
        }
      })
    }
  elif command == 'next-event':
    return next_command(body)
  else:
    msg = f'Invalid command: {command}'
    log.warn(msg)
    return {
      'statusCode': 400,
      'body': json.dumps(msg)
    }
