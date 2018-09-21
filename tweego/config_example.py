import pymongo
import urllib

cfg = { 
    "consumer_key"        : "",
    "consumer_secret"     : "",
    "access_token"        : "",
    "access_token_secret" : "" 
    }

username = ""
password = ""
username = urllib.parse.quote_plus(username)
password = urllib.parse.quote_plus(password)
client = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@basilcluster-eoh28.mongodb.net/test?retryWrites=true")
