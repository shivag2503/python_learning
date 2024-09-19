import requests
from bs4 import BeautifulSoup
import smtplib
import dotenv
import os

dotenv.load_dotenv()

my_email = os.getenv("MY_EMAIL")
password = os.getenv("PASSWORD")
recipient_email = os.getenv("RECIPIENT_EMAIL")

URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

headers = {
    "Accept-Language": "en-US",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 "
                  "Safari/537.36"
}

target_price = 100.00

response = requests.get(url=URL, headers=headers)

amazon_html = response.text

soup = BeautifulSoup(amazon_html, "html.parser")

price = soup.find(name="span", class_="a-price-whole").text

decimal = soup.find(name="span", class_="a-price-fraction").text

amazon_price = float(price + decimal)

if amazon_price < target_price:
    body = (f"You are lucky. The Amazon price for Instant is {amazon_price} which is less than your target price "
            f"{target_price} by {round(target_price - amazon_price,2)} rupees. You can buy now...\n")
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(my_email, recipient_email,
                            msg=f"Subject:Amazon Price Alert!!!\n\n{body}\nClick on below link to purchase your item: "
                                f"{URL}")
