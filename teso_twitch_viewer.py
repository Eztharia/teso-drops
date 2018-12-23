#!/usr/bin/env python
# -*- coding: utf-8 -*-
#title           :teso_twitch_viewer.py
#description     :Visionnage des twitch live (Drop Activated)
#author          :eztharia35@gmail.com
#date            :26/10/2018
#version         :0.1
#usage           :python teso_twitch_viewer.py
#python_version  :2.7.14
#=======================================================================

####
# Get lib
####
from twitch import TwitchClient
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests, json, unicodedata, time

#####
# Send request to twitch api
####
headers = {
    'Accept': 'application/vnd.twitchtv.v5+json',
    'Client-ID': '',
}

params = (
    ('game', 'The Elder Scrolls Online'),
    ('limit', 100),
)

response = requests.get('https://api.twitch.tv/kraken/streams/', headers=headers, params=params)

#####
# Convert response to json format
#####
a = response.json()

#####
# Get number of stream
####
stream_number = len(a['streams'])
print(stream_number)
keywords=["DROPS", "Drops", "drop", "drops", "!Drops", "[Drop Actif]", "!Drops!","!DROPS", "!Loot" ,"!drops", "!DROP"]

#####
# Get name and username for all live stream
#####
i = 0
get_streams_names = []
while i < stream_number:
    names = a['streams'][i]['channel']['status']
    #print(names)
    username = a['streams'][i]['channel']['url']
    username = username.split('/')[3]
    #####
    # Filter all current live with drop enabled 
    #####
    for each in keywords:
        if each in names:
            get_streams_names.append(username)
            new_value = set(get_streams_names)
    i += 1


#####
# Get all user with drop activated & generate array for multitwitch
#####
streamers_names = []
for each in new_value:
    streamers_names.append(each)

url = "http://www.multitwitch.tv"
#url = "http://multi-twit.ch"

def concatenate_list_data(list):
    result= ''
    for element in list:
        result += str("/" + element)
    return result

users = concatenate_list_data(streamers_names)
url = url + users

print(url)
#####
# Open Web Browser and play twitch
#####
driver = webdriver.Chrome()
#driver = webdriver.Firefox()
driver.get(url)
