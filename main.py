import time
import requests
from datetime import datetime, timezone
import smtplib
import os

MY_LAT = 19.339807
MY_LONG = -99.219844

# Obtener horarios de amanecer y atardecer
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,  # UTC
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

print(f"Sunrise: {sunrise}, Sunset: {sunset}")


def look_up(iss_latitude, iss_longitude):
    time_now = datetime.now(timezone.utc).hour  # Convertir a UTC

    if MY_LAT - 5 < iss_latitude < MY_LAT + 5 and MY_LONG - 5 < iss_longitude < MY_LONG + 5:
        if time_now >= sunset or time_now <= sunrise:
            my_email = "hackthedayofficial@gmail.com"
            password = os.getenv("EMAIL_PASSWORD")

            try:
                connection = smtplib.SMTP("smtp.gmail.com", 587)
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs="diego.rdlvs1@gmail.com",
                    msg="Subject:Look Up\n\nYou better look up, ISS is passing through"
                )
                connection.close()
                print("Correo enviado con éxito")
            except smtplib.SMTPException as e:
                print(f"Error enviando el correo: {e}")
        else:
            print("Es de día, no se enviará el correo")
    else:
        print("No ISS at sight right now")


while True:
    time.sleep(60)

    # Obtener la posición actual de la ISS
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    print(f"ISS Position: {iss_latitude}, {iss_longitude}")

    look_up(iss_latitude, iss_longitude)

