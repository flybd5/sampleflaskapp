#!/usr/bin/env python
# Sony python coding test
from lxml import html
import requests
import json
import io

thePage = 'http://www.metacritic.com/game/playstation-4'
headers = {'User-Agent': 'MagicBrowser'}
jsonData = {}

# Get the page, make a tree, parse it with xpath, put the results in a dictionary and json'ize it.
req = requests.get(thePage,headers=headers)
tree = html.fromstring(req.content)
games = tree.xpath('.//div[@class="main_stats"]/div[@class="basic_stat product_title"]/h3[@class="product_title"]/a/text()')
scores = tree.xpath('.//div[@class="main_stats"]/a[@class="basic_stat product_score"]/span[@class="metascore_w medium game positive"]/text()') 
intscores = [int(i) for i in scores]
jsonData = dict(zip(games,intscores))

d = {'':[{'game':key,'score':value} for key,value in jsonData.items()]}
json.dumps(d, indent=4)
print json.dumps([{'game': k, 'score': v} for k,v in jsonData.items()], indent=4, sort_keys = True)
