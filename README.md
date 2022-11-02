# Scrapy crawler that scrapes homes from Airbnb and stores them in MongoDB

Scrapy crawler developed by Samuel Abolo for the Quibble Python developer Challenge


## Approach
As a result of Airbnb being a dynamic site with most of its content loaded from JavaScript, there where two options on how to approach this.

The first was to use frameworks like scrapy Splash or Selenium to fully load the site and execute the javascript code. The disadantage of this is that setting up these frameworks are heavy and makes the system more complex

The second approach which I picked was to figure out the endpoint the JavaScipt was sending it's requests to and scrape from there directly.

## observations
1. I noticed that the name of the owner of the listings where sometimes left blank
2. I noticed that more information about the ratings, such as [ratings for accuracy, checkin, location, etc] will have to be scraped from the room link itself. this can be done with Splash.
3. I needed to find a way to handle pagination, this was done through some important pagination info in the response


## How to run

1. Clone this repo
2. Create a virtual environment with `python -m venv env` or `python -m virtualenv env`
3. Activate your virtual environment with `source ./env/bin/activate` for linux or `.\env\Scripts\activate` for windows
4. run `pip install -r requirements.txt`
5. create a `.env` file and add `MONGO_URI=<your-mongodb-connection-string>'`
6. cd into the folder airbnb
7. run `scrapy crawl listings`


