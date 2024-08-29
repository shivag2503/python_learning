import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 24.585445
MY_LONG = 73.712479

my_email = "datasciencefuture2025@gmail.com"
password = ""
recipient_email = "shivamagrawal1166171@gmail.com"


def is_iss_near():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    my_lat_inc = MY_LAT + 5
    my_lat_dec = MY_LAT - 5

    my_lng_inc = MY_LONG + 5
    my_lng_dec = MY_LONG - 5

    if (my_lat_dec <= iss_latitude <= my_lat_inc) and (
            my_lng_dec <= iss_longitude <= my_lng_inc):
        return True


def is_dark_now():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
        "tzid": "Asia/KOLKATA"
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour
    if time_now <= sunrise or time_now >= sunset:
        return True


while True:
    if is_iss_near() and is_dark_now():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(my_email, password)
            connection.sendmail(my_email, recipient_email,
                                msg="Subject:ISS is near!!!\n\nPlease look into sky ISS is near")
    time.sleep(60)
