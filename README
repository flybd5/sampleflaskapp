# Author: Juan Jimenez - October 2016
# Flask python code that implements the solution to the initial coding challenge
# Run: python -m flask run
# Requires:
#	- lxml, flask, collections, requests, json
# Use pip to install the dependencies.
# You must also "export FLASK_APP=sonyflask.py" before you can run the app
# For unit testing run: python sonytest.py or use nosetests
# A text file with the metacritic HTML is needed for unit testing and it must
# reside in the same directory in a file named "metacritic-out".
# If the file is missing you can recreate it with this command:
#   curl -X GET 'http://www.metacritic.com/game/playstation-4' -o metracritic-out -H 'User-Agent: Magic Browser'

This app scrapes http://www.metacritic.com/game/playstation-4 to extract the listed titles
and their scores. The app uses the Flask framework and runs as a server that instantiates
two GET endpoints:

1. http://127.0.0.1:5000/games/
	Lists all the game titles and their scores in json format
2. http://127.0.0.1:5000/game/<game_title>
        Lists the requested title, if it exists, and its score in json format. The
	game title name is converted to the format used in metacritic tags.

If the web site is down or the page is unavailable the app will notify of the error.
If the title does not exist, or no titles are listed, it will return an empty result.

--------

The sony.py app is a standalone app, all it does is get the entire list of titles
and outputs JSON.
