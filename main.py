import smtplib
import time

import requests
from datetime import datetime

MY_LAT = 51.507351  # Your latitude
MY_LONG = -0.127758  # Your longitude

my_email = "rajasethi056@gmail.com"
to_email = "rajasethi874@gmail.com"
password = "Mohanuma@12"


def send_update_iss(msg):
    with  smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=to_email,
                            msg=f"Subject:ISS IS GOING FROM ABOVE YOUR HEAD\n\n{msg}")


def check_pos():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if 21.912434 <= iss_latitude <= 31.912434 and 70.787270 <= iss_longitude <= 80.787270:
        send_update_iss(
            "Raja,\n The ISS has reached near your Location.Have a look in the sky from your Home to See it in Real!!!")
    else:
        print("Nope")

# Your position is within +5 or -5 degrees of the ISS position.
while True:
    check_pos()
    time.sleep(60)

# parameters = {
#     "lat": MY_LAT,
#     "lng": MY_LONG,
#     "formatted": 0,
# }
#
# response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
# response.raise_for_status()
# data = response.json()
# sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
# sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
#
# time_now = datetime.now()

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
