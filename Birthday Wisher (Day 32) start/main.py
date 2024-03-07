import datetime as dt
import random
import smtplib
from dotenv import load_dotenv
import os
load_dotenv()
#
MY_EMAIL = os.getenv('MY_EMAIL')
PASSWORD = os.getenv('PASSWORD')
OPP_EMAIL = os.getenv('OPP_EMAIL')

#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="OPP_EMAIL",
#         msg="Subject:Hello\n\nThis is the body of my email")

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=1993, month=2, day=5)


if day_of_week == 2:
    with open("quotes.txt", "r") as data:
        quotes = data.readlines()
        weekly_quote = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Motivational Quote\n\n{weekly_quote}"
        )
