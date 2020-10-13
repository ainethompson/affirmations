""" CRUD operations. """
from model import db, User, Message, UserMessage, connect_to_db

#Functions

def create_user(fname, phone_num):
    """ create and return a new user. """

    user = User(fname=fname, phone_num=phone_num)

    db.session.add(user)
    db.session.commit()

    return user

def create_message(message_text):
    """ Create and return message. """

    message = Message(message_text=message_text)

    db.session.add(message)
    db.session.commit()

    return message

def get_messages():
    """ Return all messages. """
    return Message.query.all()



def create_user_message(user_id, message_id):
    """ Create and return 1 message for 1 user. """
    user_message = UserMessage(user_id=user_id, message_id=message_id)

    db.session.add(user_message)
    db.session.commit()

    return user_message


if __name__== '__main__':
    from server import app
    connect_to_db(app)