#!/usr/bin/python -m flask run
# Sony python coding test

# Author: Juan Jimenez - October 2017
# Flash python code that implements the solution to the initial coding challenge
# Run: python -m flask run
# Requires:
#	- lxml, flask, collections, requests, json
# Use pip to install the dependencies.

from lxml import html
from flask import Flask
from collections import OrderedDict
import requests
import json
import io

# The URL to scrape, a fake header to fool the server
thePage = 'http://www.metacritic.com/game/playstation-4'
headers = {'User-Agent': 'MagicBrowser'}

# Init instance of Flask and define two routes to respond to GET requests
# - /games/<game> which will return json from one game with the title and score
# - /games/ will return json with all games listed on the web page.

app = Flask(__name__)
@app.route('/games/<game>')
def show_a_game(game):
  # Init an xpath to parse the html for the game title and code
  gameXPath = './/div[@class="main_stats"]/div[@class="basic_stat product_title"]/h3[@class="product_title"]/a'
  scoreXPath = './/div[@class="main_stats"]/a'
  scoreXPathEnd = '/span[@class="metascore_w medium game positive"]/text()'
  # Make the request
  req = requests.get(thePage,headers=headers)
  # If the request is successful then begin parsing
  if req.status_code == 200:
    # Init an xpath tree from the html
    tree = html.fromstring(req.content)
    # Flask passes the argument in the URL, we need to massage it a bit
    game = game.lower()
    game = game.replace(" ","-")
    game = game.replace(":","")
    # Prep the xpath statements
    gameXPath += '[contains(@href,"/game/playstation-4/' + game + '")]/text()'
    scoreXPath += '[@href="/game/playstation-4/' + game + '"]' + scoreXPathEnd
    # Parse
    aGame = tree.xpath(gameXPath)
    aScore = tree.xpath(scoreXPath)
    # Build the single json output
    output = ''
    if aGame:
      output = '[\n  {\n    "title": "'+str(aGame[0])+'",\n    "score": '+str(aScore[0])+'\n  }\n]'
    # For dev purposes I print it formatted, then return to give the browser the output
    print output
    return(output)

# This one gives you all the games listed and their scores

@app.route('/games/')
def show_all_games():
  # Again, prep the xpaths
  gameXPath = './/div[@class="main_stats"]/div[@class="basic_stat product_title"]/h3[@class="product_title"]/a/text()'
  scoreXPath = './/div[@class="main_stats"]/a/span[@class="metascore_w medium game positive"]/text()'
  # Issue the request
  req = requests.get(thePage,headers=headers)
  # If it succeeds then continue
  if req.status_code == 200:
    # Build the xpath tree
    tree = html.fromstring(req.content)
    # Build lists with the games and their corresponding scores
    games = tree.xpath(gameXPath)
    scores = tree.xpath(scoreXPath)
    # Convert the scores to integers
    intscores = [int(i) for i in scores]
    # Build the output with the json for all the game titles and scores we found.
    output = '['
    index = 0
    while index < len(games):
       output += '\n  {\n      "title": "'+str(games[index])+'",\n      "score": '+str(scores[index])+'\n  }'
       index += 1
       if index < len(games): output += ','
    output += '\n]'
    # Print for dev purposes, then pass the result to the browser
    print output
    return(output)
