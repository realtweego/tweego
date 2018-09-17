from pymongo import MongoClient
import json

MONGO_HOST= 'mongodb://localhost/twitterdb'  # assuming you have mongoDB installed locally
                                             # and a database called 'twitterdb'

def on_data(data):
    client = MongoClient(MONGO_HOST)
    # Decode the JSON 
    db = client.twitterdb
    coll = db.tw
    datajson = json.loads(data)
    #grab the 'created_at' data from the Tweet to use for display
    created_at = datajson['created_at']

    #print out a message to the screen that we have collected a tweet
    print("Tweet collected at " + str(created_at))
            
    #insert the data into the mongoDB into a collection called twitter_search
    #if twitter_search doesn't exist, it will be created.
    client.twitterdb.collections.testing_search.insert(datajson)
