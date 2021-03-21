#!/usr/bin/env python
import argparse
import feedparser

# Create the parser
my_parser = argparse.ArgumentParser(prog="rssfeed", description='Parse multiple rss feed')

# Add the arguments
my_parser.add_argument('--urls', action='store', type=str, required=True)

# Execute the parse_args() method
args = my_parser.parse_args()

urls = args.urls.split(',')

def parse(url):
  print(feedparser.parse(url).feed.title)
  
parse(urls[0])

#./rssfeed.py --urls https://zapier.com/blpg/feeds/latest