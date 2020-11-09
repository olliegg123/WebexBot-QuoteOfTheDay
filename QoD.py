import requests
import json


response = requests.get("http://quotes.rest/qod.json?category=inspire")
print(response)
obj = response.text
res = json.loads(obj)
quote = res['contents']['quotes'][0]['quote']
author = str(res['contents']['quotes'][0]['author'])
message = ("'"+quote+"' - "+author)
emails = ['email1@email.com', 'email2@email.com']

baseurl = 'https://webexapis.com/v1/'
type = 'messages'
url_bot = (baseurl + type)

x=0
for x in range(0, len(emails)):
    headers = {
            "Authorization": "Bearer BEARER_TOKEN",
            "Content-Type": "application/json"
            }
    payload = {
        "toPersonEmail": emails[x-1],
        "markdown": message,
        }
    response = requests.post(url_bot, data=json.dumps(payload), headers=headers)
    print('Sent to', emails[x-1])
    x=x+1
print(response)
