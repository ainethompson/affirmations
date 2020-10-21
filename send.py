from twilio.rest import Client
from quotes import quotes
import schedule
from random import choice

phone = '+15109819837'
twilio_number = '+15103300507'
quote = choice(messages.quotes)

# def send_message(message):
account_sid = 'ACcc394fecbdc5ff50a1d61b084c41c806'
auth_token = 'af01d4b0a4263bceebf7e89d697bd310'
client = Client(account_sid, auth_token)

message = client.messages.create(to=phone,
                        from_=twilio_number,
                        body=quote)

print(message.sid)

    # schedule.every().day.at("09:00").do(send_message)