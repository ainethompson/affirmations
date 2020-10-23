from twilio.rest import Client
import json
import os
import model
from model import db, User, connect_to_db
import crud
import schedule
import time
from random import choice, randint


if __name__== '__main__':
    from server import app
    connect_to_db(app)

all_phones = crud.get_all_phone_nums()

phone_list = []

for phone_num in all_phones:
    phone_str =''.join(list(phone_num)) #  ('510-981-9837',) --> 510-981-9837
    raw_phone = phone_str.replace('-', '') #  510-981-9837 --> 5109819837
    
    phone_list.append(f'+1{raw_phone}') #  5109819837 --> +15109819837

with open('data/messages.json') as f:
    message_data = json.load(f)

def send_message():
    account_sid = os.environ.get('TWILIO_SID')
    auth_token = os.environ.get('TWILIO_TOKEN')
    client = Client(account_sid, auth_token)

    i = randint(0, len(message_data))
    text = ''.join(list(message_data[i].values()))
    author = ''.join(list(message_data[i].keys()))

    quote = f"Note to self ... \n{text} \n              - {author}"

    twilio_number = '+15103300507'
    for num in phone_list:
        phone = num

        message = client.messages.create(to=phone,
                                from_=twilio_number,
                                body=quote)
        print(message)
schedule.every().minute.do(send_message)
# schedule.every().day.at("19:39").do(send_message)

while True:
        schedule.run_pending()
        time.sleep(1)

    