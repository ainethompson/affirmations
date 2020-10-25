from twilio.rest import Client
import json
import os
import model

import crud

import schedule
import time
from random import choice, randint


if __name__== '__main__':
    from server import app
    model.connect_to_db(app)

# TO SEND TO EVERY USER:
# all_phones = crud.get_all_phone_nums()

# phone_list = []

# for phone_num in all_phones:
#     phone_str =''.join(list(phone_num)) #  ('510-981-9837',) --> 510-981-9837
#     raw_phone = phone_str.replace('-', '') #  510-981-9837 --> 5109819837
    
#     phone_list.append(f'+1{raw_phone}') #  5109819837 --> +15109819837

# with open('data/messages.json') as f:
#     message_data = json.load(f)
# message_data = seed_database.messages_in_db

# crud.get_unsent_messages()

unsent_messages = crud.get_unsent_messages()

# for item in message_data:
#     if model.Message.sent == False:
#         unsent_messages.append(item)


def send_message():
    account_sid = os.environ.get('TWILIO_SID')
    auth_token = os.environ.get('TWILIO_TOKEN')
    client = Client(account_sid, auth_token)


    i = randint(0, len(unsent_messages))
    to_send = unsent_messages[i]
    # text = model.Message.message_text
    # author = model.Message.message_author

    text = to_send.message_text
    author = to_send.message_author

    # text = to_send['Text'].values()
    # author = to_send['Author'].values()

    # text = ''.join(list(unsent_messages[i].values()))
    # author = ''.join(list(unsent_messages[i].keys()))

    quote = f"✨ Note to self.... \n\n{text} \n\n- {author} ✨"

    twilio_number = '+15103300507'
    phone ='+15109819837'
    # for num in phone_list:
    #     phone = num
    

    message = client.messages.create(to=phone,
                            from_=twilio_number,
                            body=quote)
    print(message)

    person = crud.get_user_by_phone(phone)

    crud.create_user_message(person.user_id, to_send.message_id)
    model.Message.sent == True


schedule.every(10).seconds.do(send_message)
# schedule.every().day.at("19:39").do(send_message)

while True:
        schedule.run_pending()
        time.sleep(1)

    



    # i = randint(0, len(unsent_messages))
    # text = ''.join(listm(unsent_messages[i].values()))
    # # author = ''.join(list(unsent_messages[i].keys()))