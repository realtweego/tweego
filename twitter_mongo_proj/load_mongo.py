#from pymongo import MongoClient


def load_data(client, data_list):
    #client = MONGO_HOST
            
    #insert the data into the mongoDB into a collection called tweets
    #if tweets doesn't exist, it will be created.
    followers=[]
    for tweet in data_list:
        followers.append(tweet['followers'])
    for i in range(len(data_list)//10):
        for tweet in data_list:
            if tweet['followers']==max(followers):
                tweet['interesting']=1
        followers.remove(max(followers)) 
    client.twitter.collections.tweets_labeled.insert(data_list)
 
if __name__ == "__main__":
	load_data(client, data_list)
