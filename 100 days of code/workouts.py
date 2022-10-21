import requests
from datetime import datetime

today = datetime.now()
calendar_day = today.strftime("%d/%m/%Y")
hour = today.hour
minute = today.minute
second = today.second
time = f"{hour}:{minute}:{second}"
TOKEN = "Bearer 83q29pwur8uaserupq"

EXCERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
APP_ID = "4bacb3c3"
API_KEY = "9d51d10b723c22585bcad3a12756e283"

query = input("What exercise did you do today? ")

excercise_data = {
    "query":query,
    "gender":"male",
    "weight_kg":65.7709,
    "height_cm":187.96,
    "age":18
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

response = requests.post(EXCERCISE_ENDPOINT, json = excercise_data, headers = headers)
result = response.json()
print(result)

sheet_endpoint = "https://api.sheety.co/6166e2341348334d3e022a68b184e968/dallin'sWorkouts/workouts"
sheety_headers = {
    "Authorization": TOKEN
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": calendar_day,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheet_endpoint, json = sheet_inputs, headers = sheety_headers)

