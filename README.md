## Multple-Site-Search

### Requirements

* Python 2.7.x
* Virtualenv
* PIP
* Heroku Toolbelt / Foreman
* Twitter Account
* Google Account

## Set up virtual environment

Navigate to code directory in Terminal and run following command

* Create and activate virtual environment for directory.

		virtualenv venv
		. venv/bin/activate

* Install requirements for app

		pip install -r requirements.txt

In your Application settings, find the tokens and keys, you will need these to use the Twitter API.

Create **.env** file with the following

* Twitter Credentials


	OAUTH_TOKEN=YOUROAUTHTOKENHERE
	OAUTH_SECRET=YOUROAUTHSECRETHERE
	CONSUMER_KEY=YOURCONSUMERKEYHERE
	CONSUMER_SECRET=YOURCONSUMERSECRETHERE

* Google Credentials
   GOOGLEKEY=YOURGOOGLEKEY
   GOOGLECX=YOURGOOGLECX



Save as **.env** in your code directory.


## Start the server

To start server you must have Foreman

Start your engines

	foreman start

OR

	. start

### Enjoy

Open browser, <http://localhost:5000>


### Stop server 

	Ctrl+C


