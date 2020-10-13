""" Script to seed database. """

import os
import json
from random import choice, randint

import crud
import model
import server

os.system('dropdb user_messages')
os.system('createdb user_messages')

model.connect_to_db(server.app)
model.db.create_all()

#  load message data from JSON file
with open('data/messages.json') as m:
    message_data = json.loads(m.read())

 # TO DO - get message_text from message dictionary.
# create a message and append it to messages_in_db

messages_in_db = []
for message in message_data:
    message_text = message['message_text']
   
    db_message = crud.create_message(message_text)
    
    messages_in_db.append(db_message)

for n in range(10):
    fname = f'user{n}'
    phone_num = '000-000-0000'

    user = crud.create_user(fname, phone_num)

    for i in range(10):
        random_message = choice(messages_in_db)

        user_message = crud.create_user_message(user, random_message)