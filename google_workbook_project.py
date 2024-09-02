import requests
from datetime import datetime

APP_ID = ""
API_KEY = ""

EXERCISE_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEETY_URL = "https://api.sheety.co/693cc7545208d3adb511003814c02560/100DaysPython/workouts"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

config = {
    "query": input("Tell me which exercise you did? "),
    "gender": "male",
    "weight_kg": 58,
    "height_cm": 169,
    "age": 28
}

response = requests.post(EXERCISE_URL, json=config, headers=headers)
output = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

google_headers = {
    "Authorization": "Bearer <token>"
}

for exercise in output["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    google_sheet_response = requests.post(SHEETY_URL, json=sheet_inputs,headers=google_headers)
    print(google_sheet_response.text)

# APP_ID = os.environ["APP_ID"] – raises exception if key does not exist
# APP_ID = os.environ.get("APP_ID") – returns None if key does not exist
# APP_ID = os.environ.get("APP_ID", “Message”) – returns “Message” if key does not exist
