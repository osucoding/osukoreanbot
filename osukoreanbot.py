import json
import logging
import os

from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError

try:
  PUBLIC_KEY = os.environ['PUBLIC_KEY']
except:
  f = open('./secrets/discord_bot.json')
  data = json.load(f)
  PUBLIC_KEY = data['public_key']
  f.close()

def lambda_handler(event, context):
  try:
    verify_key = VerifyKey(bytes.fromhex(PUBLIC_KEY))

    signature = event['headers']["x-signature-ed25519"]
    timestamp = event['headers']["x-signature-timestamp"]
    body = event['body']

    try:
      verify_key.verify(f'{timestamp}{body}'.encode(), bytes.fromhex(signature))
      body = json.loads(event['body'])
    except BadSignatureError as e:
      logging.error(f'BadSignatureError raised. {e}')
      return {
        'statusCode': 401,
        'body': json.dumps('invalid request signature')
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
      return {
        'statusCode': 400,
        'body': json.dumps('unhandled request type')
      }
  except:
    return {
      'statusCode': 400,
      'body': json.dumps('malformed event structure')
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
  else:
    return {
      'statusCode': 400,
      'body': json.dumps('unhandled command')
    }
