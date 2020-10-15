from flask import (Flask, render_template, request, flash, session, redirect)
from model import connect_to_db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "aine-first-project"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
    """ View Homepage. """
    return render_template('homepage.html')

@app.route('/subscribe')
def show_subscribe():
    """ Show subscription page. """

    return render_template('subscribe.html')

@app.route('/subscribe', methods=['POST'])
def process_subscribe():
    """ Subscribe user to receive daily messages.

    Save user's name and phone number to DB """




# @app.route('/messages')
# def all_messages():
#     """ View all messages. """

#     messages = crud.get_messages

#     return render_template('all_messages.html', messages=messages)


if __name__ == '__main__': 
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')