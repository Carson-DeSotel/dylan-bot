import os
import sys
import json

from urllib.parse import urlencode
from urllib.request import Request, urlopen

from flask import Flask, request

from random import choice

app = Flask(__name__)
bot_id = os.getenv('GROUPME_BOT_ID')
@app.route('/', methods=['POST'])
def webhook():
  data = request.get_json()
  log('Recieved {}'.format(data))

  # We don't want to reply to ourselves!
  if data['name'] != 'nice-groupme':
    if('69' in data['text'] or "sixty-nine" in data['text'].lower() and data['name'] != 'Dylan'):
        send_message("nice")

    if('--beerme' in data['text'].lower() and data['name'] != 'Dylan'):
        responses = [
        "yeah bro, have a beer on me",
        "I'll get you a 'rona my dude",
        "Hope a busch latte sounds good my guy",
        "We're all out. Here's a Mike's Hard",
        "It just hasn't been the same since Michelle left man. Coors? Her favorite brew was Coors. Oh God oh fuck me. WHYYYYYYYYYYYYYYYYYYYYYY! MICHELLE I STILL LOVE YOU"
        ]
        send_message(choice(responses))

    if('--mebeer' in data['text'].lower() and data['name'] != 'Dylan'):
        responses = [
            'Bro, could you beer me? My \'rona\'s gettin low!',
            'A coors sounds pretty cash right now, not gonna lie',
            'broski, I\'d kill for a miller right now, I\'ll Venmo you',
            'Spot me for a cerveza mi amigo?',
            'brrrroooooooooo neeed another beeeerr mannnn',
            'fuck dude of fuck I\'m so juiced rn bro'
        ]
        send_message(choice(responses))

    if('major' in data['text'].lower() and data['name'] != 'Dylan'):
        responses = [
        "Yeah man, for sure. I'm studying finance with a minor in blastin babes.",
        "Major? Yeah, my dad said that if I got a business administration degree, I could work for his company",
        "My major? Not really sure right now, just as long as I don't have to take many classes or math",
        "I'm planning on a  major in getting lit with a minor in selling drugs.",
        "I used to be a finance major, but I got kicked out of my school for all the drug things"
        ]

        send_message(choice(responses))

    if('pong' in data['text'].lower() and data['name'] != 'Dylan'):
        responses = {
        0:  [
                "Wow man, you're pretty good at pong!",
                "Guess that drinks on me!",
                "Flick, swish!",
                "BRO SICK"
            ],
        1:  [
                "GOTTA GET BETTER LITTLE MAN",
                "The name's Dylan and I'm the alpha of this pong table",
                "get skunk'd"
            ]
        }

        odds = [
        0, 0, 0, 0, 1, 1,
        ]

        send_message(responses[choice(odds)])

    if('bro' in data['text'].lower() and data['name'] != 'Dylan':):
        send_message("Yup, just chillin with the bros. ")
  return "ok", 200

def send_message(msg):
  url  = 'https://api.groupme.com/v3/bots/post'

  data = {
          'bot_id' : bot_id,
          'text'   : msg,
         }
  request = Request(url, urlencode(data).encode())
  json = urlopen(request).read().decode()

def log(msg):
    print(str(msg))
    sys.stdout.flush()
