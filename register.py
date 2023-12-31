import requests as rq
import json

BASE_URL = 'https://generate-coding-challenge-server-rellb.ondigitalocean.app/'

# response = rq.post(BASE_URL+'register', json={
#   'name': 'Bavesh Matapathi',
#   'nuid': '001308802'
# })
# print(response.json())
# with open('challenge.json', 'w', encoding='utf-8') as f:
#   json.dump(response.json(), f, ensure_ascii=False, indent=4)

token = rq.get(BASE_URL+'forgot_token/001308802')
print(token.text)
with open('token.txt', 'w') as t:
  t.write(token.text)

challenge = rq.get(BASE_URL+'challenge/{}'.format(token.text))
print(challenge.json())
with open('challenge.json', 'w') as json_file:
  json_file.dump(challenge.json(), f, ensure_ascii=False, indent=4)

