from decoder import decode
import json
import requests as rq

with open('token.txt') as t:
  token = t.read()

with open('challenge.json') as json_file:
  json_data = json.load(json_file)

solution = [decode(str) for str in json_data['challenge']]
print(solution)

BASE_URL = 'https://generate-coding-challenge-server-rellb.ondigitalocean.app/'

response = rq.post(BASE_URL+'submit/{}'.format(token), json=solution)
print(response.status_code)
print(response.json())
