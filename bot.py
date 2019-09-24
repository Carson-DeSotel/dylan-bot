import os
import json
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from flask import Flask, request

app = Flask(__name__)
bot_id = "REPLACE THIS WITH YOUR BOT ID ONCE BOT IS ADDED TO THE CHAT"


@app.route('/', methods=['POST'])
def webhook():
	# 'message' is an object that represents a single GroupMe message.
	message = request.get_json()

	if '69' in message['text'].lower() and not sender_is_bot(message): # if message contains 'groot', ignoring case, and sender is not a bot...
		reply('nice')

	return "ok", 200


def reply(msg):
    url = 'https://api.groupme.com/v3/bots/post'
    data = {
        'bot_id'		: bot_id,
        'text'			: msg
    }
    request = Request(url, urlencode(data).encode())
    json = urlopen(request).read().decode()


def sender_is_bot(message):
	return message['sender_type'] == "bot"
