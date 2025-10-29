# Looking to send emails in production? Check out our Email API/SMTP product!
import smtplib
import datetime as dt
import random

sender = "Private Person <from@example.com>"
receiver = "A Test User <to@example.com>"
now = dt.datetime.now()
weekday = now.weekday()
if weekday == 6:
    with open("quotes.txt") as data:
        all_quotes = data.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    message = f"Subject: Monday Motivation\nTo: {receiver}\nFrom: {sender}\n\n{quote}"

    server = smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525)
    server.starttls()
    server.login("***", "***")
    server.sendmail(
        from_addr=sender,
        to_addrs=receiver,
        msg=message,
    )
    server.close()