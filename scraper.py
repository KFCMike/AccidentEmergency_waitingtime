21import requests

import json

import scraperwiki

from datetime import datetime

req = requests.get('http://www.ha.org.hk/aedwt/data/aedWtData.json')

j = req.json()

names=[j['result']['hospData'][i]['hospNameEn'] for i in range(0,18)]

waitime=[j['result']['hospData'][i]['topWait'] for i in range(0,18)]

names[15]=names[15][0:21]

dt=j['result']['hospData'][0]['hospTimeEn']

data = {names[i]: waitime[i] for i in range(0, 18)}

data['date'] = dt

scraperwiki.sqlite.save(unique_keys=['date'], data=data)
