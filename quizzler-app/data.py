import requests
URL = "https://opentdb.com/api.php"
PARAMETERS = {
    "amount": 10,
    "type": "boolean"
}

response = requests.get(url=URL,params=PARAMETERS)
response.raise_for_status()
data = response.json()
question_data = data["results"]



