#!/usr/bin/env python
import os
from twitter import *
from flask import Flask, request, render_template, redirect, abort, flash, jsonify, json
import requests
from requests_oauthlib import OAuth1

app = Flask(__name__)  # create our flask app

# configure Twitter API
twitter = Twitter(
            auth=OAuth(os.environ.get('OAUTH_TOKEN'), os.environ.get('OAUTH_SECRET'),
                       os.environ.get('CONSUMER_KEY'), os.environ.get('CONSUMER_SECRET'))
            )


@app.route('/')
def index():
	# get search term from querystring 'q'        
        query = request.args.get('q')
        if not query:
            return "hello world"
 
	#get search data from google api
	googleresults = get_googleApis(query)
	
	#get search data from duckduckgo api
	duckduckgoresults = get_ducks(query)
	tweetresults = get_tweets(query)

	results = {
            'google': {
                'url': googleresults[1],
                'text': googleresults[0]
            },
            'twitter': {
                'url': tweetresults[1],
                'text': tweetresults[0]
            },
            'duckduckgo': {
                'url': duckduckgoresults[1],
                'text': duckduckgoresults[0]
            }
        }

        return  jsonify({'query': query,
                         'results': results
        })


def get_googleApis(query):
    try:
	url = 'https://www.googleapis.com/customsearch/v1?key='+ os.environ.get('GOOGLEKEY') +'&cx='+ os.environ.get('GOOGLECX') +'&q=' + query
	showUrl = 'https://www.google.com?q=' + query
    	result = requests.get(url, timeout=1).json()
    	return result['items'][0]["snippet"], showUrl
    except requests.Timeout:
        result = "Request Timed out"
        return  result, showUrl

#query function to query duckduckgo api
def get_ducks(query):
    
    try:
        url = 'http://api.duckduckgo.com/?q=' + query + '&format=json&pretty=1'
	showUrl='https://www.duckduckgo.com?q=' + query
        result = requests.get(url, timeout=1).json()
        return  result['RelatedTopics'][0]['Text'], showUrl
    except requests.Timeout:
        result = "Request Timed out"
        return  result,showUrl

def get_tweets(query):
	showUrl ='https://www.twitter.com?q=' + query
	result = twitter.search.tweets(q=query, count=1)
	return result['statuses'][0]['text'], showUrl

#----- Server On ----------
# start the webserver

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
