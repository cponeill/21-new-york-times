# Loading developer libraries

import json
from two1.commands.config import Config
from two1.lib.wallet import Wallet
from two1.lib.bitrequests import BitTransferRequests

wallet = Wallet()
username = Config().username
requests = BitTransferRequests(wallet, username)

# Set up the server to run locally
server_url = 'http://localhost:5000/'

# Request the 402 end-points from the server and assign price and address to variables.
info = requests.get_402_info(url=server_url+'top-stories')
endpoint_info = dict(info)
price = int(endpoint_info['price'])
address = str(endpoint_info['bitcoin-address'])

# Array of all the top-story sections
sections = ["home", "world", "national", "politics",
            "nyregion", "business", "opinion", "technology",
            "health", "sports", "arts", "fashion", "dining", 
            "travel", "magazine", "realestate"]


def get_top_stories(section):
    params = {
        'section': section
    }
    response = requests.post(url=server_url+'top-stories', data=params)
    if response.status_code == 200:
        top_story = response.text
    else:
        top_story = str(response.status_code) + ' error'

    return top_story

if __name__=='__main__':
    print("------------------------------------------------")
    print("Welcome to the New York Times Top Story!")
    print("------------------------------------------------")
    for i in sections:
        print(i)
    story = input("\nWhat section would you like to read?\n")
    nytimes_story = get_top_stories(story)
    stories = json.loads(nytimes_story)
    print("\n"+stories['results'][0]['title']+":\n"+stories['results'][0]['byline']+"\n"+stories['results'][0]['abstract']+"\n")
    print("Copy the following link to read the full story:\n" + stories['results'][0]['url']+"\n")
    print("You just sent " + str(price) + " satoshis to:\n" + address)
    print("------------------------------------------------")
    print("Thank you for reading the New York Times today!")
    print("------------------------------------------------")


