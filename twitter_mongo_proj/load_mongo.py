#from pymongo import MongoClient


def load_data(client, data_list):
    #client = MONGO_HOST
            
    #insert the data into the mongoDB into a collection called tweets
    #if tweets doesn't exist, it will be created.
    client.twitter.collections.tweets.insert(data_list)
 
if __name__ == "__main__":
	load_data(client, data_list)
