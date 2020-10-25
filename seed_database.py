""" Script to seed database. """

import os
import json
from random import choice, randint

import crud
import model
import server

os.system('dropdb affirmations_db')
os.system('createdb affirmations_db')

model.connect_to_db(server.app)
model.db.create_all()

with open('data/messages.json') as f:
    message_data = json.load(f)

messages_in_db = []
for message in message_data:
    message_author = message['Author']
    message_text = message['Text']

    db_message = crud.create_message(message_author, message_text)
    
    messages_in_db.append(db_message)


fname = model.User.fname
phone_num = model.User.phone_num
user = crud.create_user(fname, phone_num)

# for message in sent messages:
    # if user has received that message:
    # create instance of user_message
# user_message = crud.create_user_message(user, db_message)