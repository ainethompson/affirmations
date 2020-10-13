"""Models for affirmations app. """

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    """ A user can receive many affirmations """

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String(25), nullable=False)
    phone_num = db.Column(db.String(15), nullable=False)

    # 'user-messages' = a list of UserMessage objects

    def __repr__(self):
        """ Provide helpful representation when printed """
        return f"<First name = {self.fname}, phone number = {self.phone_num}>"


class Message(db.Model):
    """ A message can be sent to many users. """

    __tablename__ = "messages"

    message_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    message_text = db.Column(db.Text)

    # 'user-messages' = a list of UserMessage objects

    def __repr__(self):
        return f"<message_id = {self.message_id}, message_text = {self.message_text}>"

class UserMessage(db.Model):
    """ many to many relationship between users and messages """

    __tablename__ = "user_messages"

    user_message_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    message_id = db.Column(db.Integer, db.ForeignKey('messages.message_id'))

    user = db.relationship('User', backref='user_messages')
    message = db.relationship('Message', backref='user_messages')

    # 'user-messages' = a list of UserMessage objects

    def __repr__(self):
        return f"<user_message_id = {self.user_message_id}, user = {self.user}, message = {self.message}>"

def connect_to_db(flask_app, db_uri='postgresql:///user_messages', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')

if __name__ == '__main__':
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)
    