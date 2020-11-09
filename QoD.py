import requests
import json


response = requests.get("http://quotes.rest/qod.json?category=inspire")
print(response)
obj = response.text
res = json.loads(obj)
quote = res['contents']['quotes'][0]['quote']
author = str(res['contents']['quotes'][0]['author'])
message = ("'"+quote+"' - "+author)
emails = ['elbarton@cisco.com', 'ogerrard@cisco.com']

baseurl = 'https://webexapis.com/v1/'
type = 'messages'
url_bot = (baseurl + type)

x=0
for x in range(0, len(emails)):
    headers = {
            "Authorization": "Bearer MzNlNDNlMDYtN2YyZS00ZTA5LWE5YzAtZTQ3NTk4ZDU4MjZiNjA2OTcyODktMDlk_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f",
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
