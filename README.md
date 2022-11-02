# Scrapy crawler that scrapes homes from Airbnb and stores them in MongoDB

Scrapy crawler developed by Samuel Abolo for the Quibble Python developer Challenge

## How to run

1. Clone this repo
2. Create a virtual environment with `python -m venv env` or `python -m virtualenv env`
3. Activate your virtual environment with `source ./env/bin/activate` for linux or `.\env\Scripts\activate` for windows
4. run `pip install -r requirements.txt`
5. create a `.env` file and add `MONGO_URI=<your-mongodb-connection-string>'`
6. cd into the folder airbnb
7. run `scrapy crawl listings`


