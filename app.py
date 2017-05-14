#!/usr/bin/env python
import os
from flask import Flask, request, render_template, redirect, abort, flash, jsonify, json
import requests

app = Flask(__name__)  # create our flask app


@app.route('/')
def index():
	# get search term from querystring 'q'        
        query = request.args.get('q')
        if not query:
            return "hello world"
 
	#get search data from google api
	googleresults = get_googleApis(query)

	results = {
            'google': {
                'url': googleresults[1],
                'text': googleresults[0]['items'][0]["snippet"]
            },
            'twitter': {
                'url': "https://example.com?q=the%dark%knight",
                'text': "Hello World"
            },
            'duckduckgo': {
                'url': "Hello Duck",
                'text': "Hello Duck"
            }
        }

        return  jsonify({'query': query,
                         'results': results
        })


def get_googleApis(query):

    url = 'https://www.googleapis.com/customsearch/v1?key='+ os.environ.get('GOOGLEKEY') +'&cx='+ os.environ.get('GOOGLECX') +'&q=' + query

    result = requests.get(url).json()
    return result, url

#----- Server On ----------
# start the webserver

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
