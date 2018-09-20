.. highlight:: shell

========
Overview
========

The Gist
--------
The module ´scrape_twitter´ uses tweepy to retrieve posts 
related to machine learning. Posts that are marked as relevant
stream directly into a Mongo Database via the script 
´tm_connection´. The ´twitter_push´ module pushes the relevant
(hot) posts to our twitter bot, which publishes them on 
twitter with the source user in the heading.