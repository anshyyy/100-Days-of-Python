from datetime import datetime
import os
import requests

APP_ID = "b953d6c2"

APP_KEY = "65b6aa67e0e525b5ef207ec0dfd06887"
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = ""

headers = {
    "x-app-id":APP_ID,
    "x-app-key":APP_KEY,
}
text = input("Tell me which exercises you did: ")
parameters = {
    "query":text,
    "gender":"MALE",
    "weight_kg":"53",
    "height_cm":"181",
    "age":"18"
}
response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")


for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
    # sheet_response = requests.post(sheet_endpoint, json=sheet_inputs)
    # sheet_response = requests.post(
    #     sheet_endpoint,
    #     json=sheet_inputs,
    #     auth=(
    #         os.environ["USERNAME"],
    #         os.environ["PASSWORD"],
    #     )
    # )

    # Bearer Token
    # bearer_headers = {
    #     "Authorization": f"Bearer anshumansharmaaa"
    # }
    # sheet_response = requests.post(
    #     sheet_endpoint,
    #     json=sheet_inputs,
    #     headers=bearer_headers
    # )

    print(sheet_response.text)




