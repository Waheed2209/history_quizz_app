

import requests

parameters = {
    "amount": 10,
    "category": 23,
     "type": "boolean"
}

response = requests.get("https://opentdb.com/api.php",params=parameters)
response.raise_for_status()
data = response.json()
data = data["results"]
question_data = data
print(question_data)
