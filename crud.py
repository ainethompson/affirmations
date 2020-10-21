""" CRUD operations. """
from model import db, User, Message, UserMessage, connect_to_db

#Functions

def create_user(fname, phone_num):
    """ create and return a new user. """

    user = User(fname=fname, phone_num=phone_num)

    db.session.add(user)
    db.session.commit()

    return user

def get_user_by_id(user_id):
    """Return a user by primary key."""

    return User.query.get(user_id)

def get_user_by_phone(phone_num):
    """ Return a user by phone_num"""
    return User.query.filter(User.phone_num == phone_num).first()

def create_message(message_text):
    """ Create and return message. """

    message = Message(message_text=message_text)

    db.session.add(message)
    db.session.commit()

    return message

def get_message_by_id(message_id):
    """ Return message by id. """
    return Message.query.get(message_id)


def create_user_message(user_id, message_id):
    """ Create and return 1 message for 1 user. """
    user_message = UserMessage(user_id=user_id, message_id=message_id)

    db.session.add(user_message)
    db.session.commit()

    return user_message

def get_user_message(user_id):
    """ return a message that this user hasnt seen yet """

    #SELECT message_id FROM messages WHERE message_id NOT IN (SELECT message_id FROM user_messages WHERE user_id = 1);

    return message

if __name__== '__main__':
    from server import app
    connect_to_db(app)