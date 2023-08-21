import json

from nacl.signing import VerifyKey
from nacl.exceptions import BadSignatureError
# from discord_interactions import verify_key

PUBLIC_KEY = 'add667855a0645dabbb2230f36cf37d3127bc17ceb8ea6b732070524413b932c'

def lambda_handler(event, context):
    # return {
    #     'statusCode': 200,
    #     'body': json.dumps({
    #         'message': 'sup'
    #     })
    # }
  try:
    body = json.loads(event['body'])

    signature = event['headers']['x-signature-ed25519']
    timestamp = event['headers']['x-signature-timestamp']

    # validate the interaction

    verify_key = VerifyKey(bytes.fromhex(PUBLIC_KEY))
    # if not verify_key(body, signature, timestamp, PUBLIC_KEY):
    #   return {
    #     'message': 'not verified'
    #   }

    message = timestamp + json.dumps(body, separators=(',', ':'))

    try:
      verify_key.verify(message.encode(), signature=bytes.fromhex(signature))
    except BadSignatureError:
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
    raise

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
