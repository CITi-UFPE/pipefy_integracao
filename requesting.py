import requests # biblioteca de requisicoes http
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# substituir com autentificacao do pipefy e pipeid, respectivamente 
access_token = os.getenv('pipefy_auth')
pipe_id = '302904373'

url = "https://api.pipefy.com/graphql" # url para realizar as chamadas

headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": access_token   # pipefy authorization -> in this case, in a .env file 
}

query= """""" # -> requisicoes graphql

response = requests.post(url, json=query, headers=headers)

print(response) # printando Response
