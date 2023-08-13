import requests
from datetime import datetime
import time
from config import StartConnection

MY_LAT = 13.628756    # Tirupati longitude and Latitude
MY_LONG = 79.419182 

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
TimeNowInHr = time_now.hour


EmailSender = StartConnection()
is_on = True


while(is_on):
    time.sleep(60)     # Will keep checking after every 60 seconds
    time_now = datetime.now()
    TimeNowInHr = time_now.hour
    if TimeNowInHr > sunset or TimeNowInHr < sunrise:
        if abs(iss_latitude-MY_LAT ) < 5 and abs(iss_longitude-MY_LONG) < 5 :
            EmailSender.SendMail()
