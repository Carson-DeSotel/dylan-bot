import os
import sys
import json

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

from random import choice

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()
  log('Recieved {}'.format(data))

  # We don't want to reply to ourselves!
  if data['name'] != 'nice-groupme':
    if('69' in data['text']):
        send_message("nice")

    if('--beerme' in data['text']):
        responses = [
        "yeah bro, have a beer on me",
        "I'll get you a 'rona my dude",
        "Hope a busch latte sounds good my guy",
        "We're all out. Here's a Mike's Hard",
        "It just hasn't been the same since Michelle left man. Coors? Her favorite brew was Coors. Oh God oh fuck me. WHYYYYYYYYYYYYYYYYYYYYYY! MICHELLE I STILL LOVE YOU"
        ]
        send_message(choice(responses))

    if('--mebeer' in data['text']):
        responses = [
            'Bro, could you beer me? My \'rona\'s gettin low!',
            'A coors sounds pretty cash right now, not gonna lie',
            'broski, I\'d kill for a miller right now, I\'ll Venmo you',
            'Spot me for a cerveza mi amigo?',
            'brrrroooooooooo neeed another beeeerr mannnn',
            'fuck dude of fuck I\'m so juiced rn bro'
        ]
        send_message(choice(responses))
  return "ok", 200

def send_message(msg):
  url  = 'https://api.groupme.com/v3/bots/post'

  data = {
          'bot_id' : os.getenv('GROUPME_BOT_ID'),
          'text'   : msg,
         }
  request = Request(url, urlencode(data).encode())
  json = urlopen(request).read().decode()
