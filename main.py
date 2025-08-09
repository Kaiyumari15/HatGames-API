import os
from flask import Flask
from dotenv import load_dotenv

from games.i_love_you_message import send_love_message

load_dotenv()

GAMES = ["i_love_you_message"]
current_game = "i_love_you_message"

app = Flask(__name__)

# Although we are technically 'posting' an NFC tag scan action to the server, 
# NFC tags cannot tell the scanning device to run a POST command
# Therefore, we will simulate this by using a GET request and putting the ID in the query parameters
# This is not secure as anyone could send this request, but I'm not bothered as this is just a fun little project
@app.route("/scan/<sender>", methods=["GET"])
def hello_world(sender):
    if current_game == "i_love_you_message":
        send_love_message(sender)
        return "Message Sent!"