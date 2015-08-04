#!/usr/bin/env python3
# encoding: utf-8

import re
import os
import urllib.request as req
from bs4 import BeautifulSoup

#################
#---functions---#
#################

def write_file(link):
	# write from url to file
	site = req.urlopen(link)
	data = site.read()
	file = open(link.split('.')[1]+".html","wb") #open file in binary mode
	file.write(data)
	file.close()

def open_file(flnm):
	# read a file 
	return open(flnm,encoding='utf-8').read()

def com(wo):
	c = len(wo)+8
	print("#"*c)
	print("#---"+wo+"---#")
	print("#"*c)

link = "http://www.imgur.com/r/nsfw"

page = open_file('imgur.html')
soup = BeautifulSoup(page, 'html.parser')
lis = soup.find_all('a')
new = [i.get('href') for i in lis if "/r/nsfw" in i.get("href")]
print(new)

'''
vol = re.compile('\#Volume')
tab = re.compile('\[table]')
res = re.findall(tab, page)
print(len(res))

print(res[0])
'''

''' Game of Thrones
li = re.compile('<li>Ep\..+')
simple = re.compile('\"\>.+\<\/a\>')
season = re.findall(li,page)

for i in season:
	titles = re.findall(simple,i)
	print(titles)
'''