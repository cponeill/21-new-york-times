"""
I need to clean this code up quite a bit but the basic functionality works. 
"""

# Loading developer libraries

import requests
import os
import urllib
from flask import Flask, request
from two1.lib.wallet import Wallet
from two1.lib.bitserv.flask import Payment

app = Flask(__name__)
wallet = Wallet()
payment = Payment(app, wallet)

# go to http://developer.nytimes.com/ and choose the top-stories API key.
api_key = "<add api-key>"

# Adding 402 end-point
@app.route('/top-stories', methods=['GET', 'POST'])
@payment.required(10)
def top_stories():
     """
     Choose the section of the NYTimes you would like to read
     """
     section = request.form['section']

     url = requests.get('http://api.nytimes.com/svc/topstories/v1/'+section+'.json?api-key='+api_key)

     return url.text


if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True)
