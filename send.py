from twilio.rest import Client
import json
import os
import model
# from crud import get_all_phone_nums
import crud
import schedule
import time
from random import choice

# want to send message to every user in db

# for user in model.User:
#     phone = User.self.phone_num


# for number in list of all phone_nums:
#     phone = number

# crud.get_all_phone_nums

phone_nums = crud.get_all_phone_nums()

with open('data/messages.json') as f:
    message_data = json.load(f)

for phone_num in phone_nums:
    phone = phone_num
# phone = '+15109819837'
twilio_number = '+15103300507'

def send_message():
    account_sid = os.environ.get('TWILIO_SID')
    auth_token = os.environ.get('TWILIO_TOKEN')
    client = Client(account_sid, auth_token)

    quote = choice(message_data)
    # quote = choice(list(message_data.values()))

    message = client.messages.create(to=phone,
                            from_=twilio_number,
                            body=quote)
    print(message)

schedule.every().minute.do(send_message)
# schedule.every().day.at("15:23").do(send_message)

while True:
        schedule.run_pending()
        time.sleep(1)
    