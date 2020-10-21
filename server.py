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

@app.route('/subscribe', methods=['GET'])
def show_subscribe():
    """ Show subscription page. """

    return render_template('subscribe.html')

@app.route('/subscribe', methods=['POST'])
def process_subscribe():
    """ Subscribe user to receive daily messages.

    Save user's name and phone number to DB """

    fname = request.form.get('fname')
    phone_num = request.form.get('phone_num')

    # crud.create_user(fname, phone_num)
    user = crud.create_user(fname, phone_num)
    if user:
        flash("Oops! It looks like you're already subscribed with us!")
    
    # request.args.get(take argumetn from html templat under subscribe route and save it to a variable)
# commit to db using crud methods


@app.route('/success', methods=['POST'])
def show_success():
    # user = request.args.get('fname')
    return render_template('success.html')




if __name__ == '__main__': 
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')