import requests
import json

#url = 'baseline_model2.pkl'

url = 'http://127.0.0.1:5000/api/'



data = ["I have anxiety. I want something sweet and fruity."]
j_data = json.dumps(data)
headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
r = requests.post(url, data=j_data, headers=headers)
print("The recommended cannabis medical strain for your query is:", r.text)