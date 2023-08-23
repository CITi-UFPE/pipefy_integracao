import requests
from dotenv import find_dotenv, load_dotenv
import os
from flask import Flask, requestv

app = Flask(__name__)     # usando como servidor local para receber atualizacoes da plataforma

load_dotenv(find_dotenv())

access_token = os.getenv('pipefy_auth') # token de autorização do pipefy

url = "https://api.pipefy.com/graphql"

headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": access_token       # token de autorização do pipefy
}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)