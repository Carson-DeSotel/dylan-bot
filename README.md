# Dylan : A "frat bro" bot for GroupMe

author: Carson DeSotel

language: Python

date created: September 2019 

## Purpose

Dylan was created to annoy my friends in our GroupMe chat. I rarely notice or use him, as he has no express purpose. However, he ocassionally pops in with a *tasteful* remark.

## Usage

Dylan has a few key phrases that he 'listens' for. 

Cues: 
- `69`: if any message contains the number '69', Dylan will say "nice".
- `major`: if any message contains the word 'major', Dylan will sprout some nonsense about his major. 
- `pong`: if any message contains the word 'pong', Dylan will spout some phrases one may hear over a game of beer pong.
    - Note that this includes weighted chances of getting certain phrases. 
- `bro`: if any message contains the word 'bro', Dylan will afirm that he is "just chillin' with the bros"

Commands:
- `--beerme`: Dylan will sprout out a phrase along the lines that he will get you a beer.
- `--mebeer`: Dylan will have the audacity to ask **you** for a beer.

## Implementation

Dylan is written in Python using Flask and Requests to process event handling, GET's, and POST's from the GroupMe server. 

Dylan is hosted on my personal Heroku account. The app uses a local environment variable set up in Heroku so to keep my GroupMe bot ID private (*see line 13 in `app.py`*).