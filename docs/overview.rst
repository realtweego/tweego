.. highlight:: shell

========
Overview
========

Data Retrieval
--------------
The module ´scrape_twitter´uses tweepy to retrieve posts 
related to machine learning. These posts stream directly 
into a Mongo Database via the script ´tm_connection´, which
specifies either a local or shared Mongo connection, into 
the specified path provided in ´load_mongo´. 

Data Manipulation
-----------------
The initial batch runs are, then, labeled as ´hot_or_not´
(1-hot, 0-not) by our team for the purpose of training our 
model. The ensuing batch runs are then labeled by our trained
machine learning model. These labels are added to the Mongo
database.

Finished Product
----------------
The labeled data is used to train a second machine learning
model, which uses NLP to summarize the context of these 
posts and generates a new post. These results are then fed
to our slack bot.