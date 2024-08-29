import datetime as dt
import random
import smtplib

my_email = "shivamagrawal1166171@gmail.com"
password = "bbjfvnqejnbuxnxz"
recipient_email = "shomuagrawal@gmail.com"

today_date_time = dt.datetime.now()
today_week_day = today_date_time.weekday()

if today_week_day == 3:
    with open("quotes.txt", "r") as file:
        quote_list = file.readlines()

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(my_email, recipient_email, msg=f"Subject:Quote of the day\n\n{random.choice(quote_list)}")

