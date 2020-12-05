###fun project by Ishani after watching a tutorial by Bukola

import random
import schedule
from twilio.rest import Client
import time

seconds = time.time()
# print("Seconds since epoch =", seconds)
phone = +4591961617
twilio_number = +12519294081

# step1
"""create a collection of messsages"""

Good_morning_quotes = [
    "Good Morning Love!",
    "I don't pray,I got you. I do donate, but not you :)",
    "Good morning love, Have a nice day",
    "Good morning love, I wish you a beautiful day!",
    "Good morning love, Thank you for being there for me",

]


### step2: use an API to send the preset message

def send_message(_quote):
    account_sid = "AC34027f833aac13779001fead12f3ddbc"
    auth_token = "dd16bc1a640c4d6403ea1f66a233065f"
    client = Client(account_sid, auth_token)

    client.messages.create(
        to="+4591961617",
        from_="+12519294081",
        body=_quote
    )


# step3 scheduler
_quote = Good_morning_quotes[random.randint(0, len(Good_morning_quotes) - 1)]
schedule.every().day.at("22:59").do(send_message, Good_morning_quotes)
# schedule.every(2).minutes.do(send_message, Good_morning_quotes)

while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(2)
