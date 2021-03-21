#!/usr/bin/env python
# -*- encoding: utf8 -*-
#import re
#import feedparser

#d = feedparser.parse("https://zapier.com/blpg/feeds/latest")
#print(d.entry [0])
urls = []
with open('Domtxt', 'r') as Domtxt:
  for line in Domtxt:
    urls += line.split('\n')
    
print(' '.join(urls).split())