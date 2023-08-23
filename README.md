# OSU Korean Discord Bot

## How to run this program locally
* `virtualenv` must be installed to create a virtual environment for Python 3.7.
* To install `virtualenv`, run `$ python3 -m pip install virtualenv`
* To create a virtual environment, run `$ python3.7 -m virtualenv venv`
* To activate a virtual environment, run `$ source venv/bin/activate`. To exit a virtual environment, run `$ deactivate`

### How to install dependencies
* This project uses `poetry` to manage dependencies
  - Within the virtual env, run `$ poetry install` to install dependencies

## Deployment
* On push event to the `main` branch, GitHub Actions triggers a deployment job that uploads the updated code to AWS Lambda
* Do **NOT** delete `package-original.zip`. This contains the extracted `PyNaCl` dependency from the AWS Linux 2 environment.
* AWS Lambda with AWS API Gateway
