import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient



account_sid = 'AC12a7c7332b2e85ed30413ade5535ddd3'
auth_token = '2f6b55f7e614761081bc613d318ac171'

KEY = "f35527077256be04b5542d40cd6c8b78"
parameters = {
    "lat": 37.338207,
    "lon": -121.886330,
    "appid": KEY,
    "exclude": "current,minutely,daily,alerts"

}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()
weather_slice = data["hourly"][:12]
weather_code = []
for hour in weather_slice:
    weather_code.append(int(hour["weather"][0]["id"]))

will_rain = False
for id in weather_code:
    if id < 700:
        will_rain = True

#print(weather_code)
if will_rain:
    #print("RAINING")
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https':os.environ['https_proxy']}
    client = Client(account_sid, auth_token,http_client=proxy_client)
    message = client.messages.create(
        from_='+19842063537',
        body="It will Rain.Remember to bring an Umbrella!🌧️",
        to='+917903553605'
    )
    print(message.status)
