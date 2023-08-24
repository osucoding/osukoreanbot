# OSU Korean Discord Bot

## How to run this program locally
* `virtualenv` must be installed to create a virtual environment for Python 3.11.
* To install `virtualenv`, run `$ python3 -m pip install virtualenv`
* To create a virtual environment, run `$ python3.11 -m virtualenv venv`
* To activate a virtual environment, run `$ source venv/bin/activate`. To exit a virtual environment, run `$ deactivate`
* Running `update_command.py` locally would require you to create `./secrets/discord_bot.json` file with the Discord credentials. For example,
  -
  ```
  {
    "bot_token": "BOT TOKEN HERE",
    "app_id": "APP ID HERE",
    "server_id": "SERVER ID HERE",
    "public_key": "PUBLIC KEY HERE"
  }
  ```

### How to install dependencies
* This project uses `poetry` to manage dependencies
  - Within the virtual env, run `$ poetry install` to install dependencies

## Deployment
* On push event to the `main` branch, GitHub Actions triggers a deployment job that uploads the updated code to AWS Lambda
* Do **NOT** delete `pynacl-aws-linux-2-3.11.zip`. This contains the extracted `PyNaCl` dependency from the AWS Linux 2 environment.
* AWS Lambda with AWS API Gateway
