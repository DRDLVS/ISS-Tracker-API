import requests
from datetime import datetime

MY_LAT = 19.339807
MY_LON = -99.219844


parameters = {
    "lat": MY_LAT,
    "lng": MY_LON,
    "formatted": 0
}

response = requests.get(url=" https://api.sunrise-sunset.org/json",
                        params=parameters,)
status = response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise, sunset)

time_now = datetime.now()
print(time_now.hour)

