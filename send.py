from twilio.rest import Client
import json
import os
# from server import account_sid, auth_token
import schedule
import time
from random import choice, randint, randrange

quotes = { 1: "Dont let yesterday take up too much of today",
            2: "Start where you are, use what you have, do what you can",
            3: "I am learning everyday to let the space between where I am and where I want to be inspire me and not terrify me",
            4: "Do more things [today] that make you forget to check your phone",
            5: "May the flowers remind us why the rain was so necessary",
            6: "Remember when you so badly wanted what you currently have?",
            7: "Visualize your highest self, and start showing up as her",
            8: "There’s a future version of me who’s proud I was strong enough",
            9: "When you finally learn that a person's behavior has more to do with their own internal struggle than it ever did with you... you learn grace",
            10: "You need people in your life that are further along than you, people that have a bigger vision, people that are more experienced, people that are out of your league. You need to be exposed to new levels so that you can go to new levels!" }


# figure out how to get data from json file
# with open("messages.json", "")
# quote = json.loads('messages.json')

phone = '+15109819837'
twilio_number = '+15103300507'

def send_message():
    account_sid = os.environ.get('TWILIO_SID')
    # server.account_sid
    
    auth_token = os.environ.get('TWILIO_TOKEN')
    # server.auth_token
    
    client = Client(account_sid, auth_token)

    quote = choice(list(quotes.values()))
  
    message = client.messages.create(to=phone,
                            from_=twilio_number,
                            body=quote)

    print(message)

# schedule.every().minute.do(send_message)
schedule.every().day.at("15:23").do(send_message)
while True:
        schedule.run_pending()
        time.sleep(1)
    