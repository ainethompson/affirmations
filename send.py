from twilio.rest import Client
import json
import os
import model
from model import db, User, connect_to_db
# from crud import get_all_phone_nums
import crud
import schedule
import time
from random import choice, randint

# want to send message to every user in db

# all_phones = model.db.session.query(User.phone_num).all()

# crud.get_all_phone_nums

# all_phones = crud.get_all_phone_nums()

# for phone_num in all_phones:
#     phone_str =''.join(list(phone)) #  ('510-981-9837',) --> 510-981-9837
#     raw_phone = phone_str.replace('-', '') #  510-981-9837 --> 5109819837

#     phone = f'+1{raw_phone}' #  5109819837 --> +15109819837

    # phone = '+14157864060'

with open('data/messages.json') as f:
    message_data = json.load(f)

twilio_number = '+15103300507'
# phone = '+15109819837'
# phone = '+14157864060'

def send_message():
    account_sid = os.environ.get('TWILIO_SID')
    auth_token = os.environ.get('TWILIO_TOKEN')
    client = Client(account_sid, auth_token)

    i = randint(0, len(message_data))
    text = ''.join(list(message_data[i].values()))
    author = ''.join(list(message_data[i].keys()))

    quote = f"Note to self ... \n{text} \n- {author}"

    message = client.messages.create(to=phone,
                            from_=twilio_number,
                            body=quote)
    print(message)

schedule.every().minute.do(send_message)
# schedule.every().day.at("15:23").do(send_message)

while True:
        schedule.run_pending()
        time.sleep(1)
    