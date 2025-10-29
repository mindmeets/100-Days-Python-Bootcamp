# import smtplib
#
# # sender = "appbreweryinfo@gmail.com"
# sender = "***"
# # receiver = "***"
# receiver = "***"
#
# message = "Subject: Hi Mailtrap\n\nThis is a test e-mail message."
#
# user_name = "***"
# password = "***"
# # password = "***"
# # "****"
# with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=user_name, password=password)
#     connection.sendmail(from_addr=sender, to_addrs=receiver, msg=message)
#

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# print(now)
# print(year)
# date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
# print(date_of_birth)

import smtplib
import datetime as dt
import random

sender = "***"
receiver = "***"
user_name = "***"
password = "***"
now = dt.datetime.now()
weekday = now.weekday()
if weekday == 6:
    with open("quotes.txt") as data:
        all_quotes = data.readlines()
        quote = random.choice(all_quotes)
        message = f"Subject: Monday Motivation\n\n{quote}"

    print(quote)
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as server:
        server.starttls()
        server.login(user=user_name, password=password)
        server.sendmail(sender, receiver, message)
        print(f"Email sent to {receiver} successfully!")
        print(f"Message sent: {message}.")