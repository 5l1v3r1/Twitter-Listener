#!/usr/bin/python

time_in_sec = 600

from twitter import *
import re

from email.utils import parsedate

from time import sleep, strftime
from threading import Thread
import operator
import datetime


config = {}
execfile("config.py", config)

auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"])
stream = TwitterStream(auth = auth, secure = True)

tweet_iter = stream.statuses.filter(track = "#")

d = {}

def date_to_string(dt):
	return dt.strftime("%d/%m/%y") + ' ' + str(dt.hour) + ':' + str(dt.minute) + ':' + str(dt.second)


def collect_tweets():
    for tweet in tweet_iter:
            text = tweet['text']
            hashes = [
                t.strip("#").lower()
                    for t in text.split() 
                        if ((t.startswith("#") or t.endswith("#")) and t != "#")
            ]

            for h in hashes:
                if h in d:
                    d[h] += 1
                else:
                    d[h] = 1



t = Thread(target=collect_tweets)

t.daemon = True

t.start()

of = open("report.txt", 'w')
of.write(date_to_string(datetime.datetime.now()))

sleep(time_in_sec)

of.write('\t' + date_to_string(datetime.datetime.now()) + '\n')

d = sorted(d.items(), key=operator.itemgetter(1), reverse=True)

for i in d[:10]:
    of.write(i[0].encode('utf-8') + '\t' + str(i[1]) + '\n')
    print i[0].encode('utf-8'), i[1]