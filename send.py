from twilio.rest import Client
import json
import os

import schedule
import time
from random import choice


with open('data/messages.json') as f:
    message_data = json.load(f)

phone = '+15109819837'
twilio_number = '+15103300507'

def send_message():
    account_sid = os.environ.get('TWILIO_SID')
    auth_token = os.environ.get('TWILIO_TOKEN')
    client = Client(account_sid, auth_token)

    quote = choice(list(message_data.values()))

    message = client.messages.create(to=phone,
                            from_=twilio_number,
                            body=quote)
    print(message)

schedule.every().minute.do(send_message)
# schedule.every().day.at("15:23").do(send_message)

while True:
        schedule.run_pending()
        time.sleep(1)
    