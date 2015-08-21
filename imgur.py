#!/usr/bin/env python3
# encoding: utf-8

import os
from imgurpython import ImgurClient

client_id = '3b362e020b00e29'
client_secret = '76ec3c0b20c1044c24a94b2fbd874c0e3e150079'

client = ImgurClient(client_id, client_secret)

# Example request
subreddit = 'nsfw'
items = client.subreddit_gallery(subreddit, sort='time', window='week', page=1)
for item in items:
    print(item.link)