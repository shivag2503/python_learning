import pandas as pd
import datetime as dt
import random
import smtplib

birthday_data = pd.read_csv("birthdays.csv")
birthday_dict = {(item.month, item.day): item.to_dict() for (_, item) in birthday_data.iterrows()}

today = dt.datetime.now()
today_month = today.month
today_day = today.day

my_email = "shivamagrawal1166171@gmail.com"
password = ""

if (today_month, today_day) in birthday_dict:
    name = birthday_dict[(today_month, today_day)]["name"]
    recipient_email = birthday_dict[(today_month, today_day)]["email"]
    random_letter = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(random_letter, "r") as letter:
        content = letter.read()
        content = content.replace("[NAME]", name)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(my_email, recipient_email, msg=f"Subject:Happy Birthday!!\n\n{content}")
