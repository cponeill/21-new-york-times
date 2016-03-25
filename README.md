# 21-new-york-times

Top Story news prototype app using the NYtimes API and a 21 Bitcoin Computer

In order to use this app,  open the command line in your 21 Computer and run the following commands:

    $ git clone https://github.com/cponeill/21-new-york-times.git
    $ cd 21-new-york-times

Go to the New York Times developer portal (http://developer.nytimes.com/) and choose the top-stories API key.
Add your API key to line 15 in server.py

Run the server:

    $ python3 server.py

Open another terminal, change into the same directory, and run the following commands:

    $ python3 client.py

This is an example of what you should see when you run the client.py script on your 21 Bitcoin Computer
![Alt text](https://github.com/cponeill/21-new-york-times/blob/master/nytimes_top_story_app.JPG "nytimes_app")
