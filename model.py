"""Models for affirmations app. """

from flask_sqlalchemy import flask_sqlalchemy


class User(db.Model):
    """ A user can receive many affirmations """

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String(25), nullable=False)
    phone_num = db.Column(db.String(10), nullable=False)


    def __repr__(self):
        """ Provide helpful representation when printed """
        return f"user fname={self.fname}, user phone_num={self.phone_num}"


class Message(db.Model):
    """ A message can be sent to many users. """

    __tablename__ = "messages"

    message_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    message_text = db.Column(db.Text)

    def __repr__(self):
        return f"message_id={self.message_id}, message_text={self.message_text}"

class UserMessage(db.Model):
    """ many to many relationship between users and messages """

    __tablename__ = "user_message"

    user_message_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    message_id = db.Column(db.Integer, db.ForeignKey('messages.message_id'))

    user = db.relationship('User', backref=)
    message = db.relationship('User', backref=)