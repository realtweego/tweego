.. highlight:: shell

========
Overview
========

How it Works
------------
The module scrape_twitter uses tweepy to retrieve posts 
related to machine learning. The top 5 posts per batch 
are labeled as ´hot´ and are pushed to the Mongo Database 
via the script tm_connection. Posts are determined to be
´hot´ by the number of user favorites. Of the top 5 posts,
the tweet with the most favorites is pushed to the twitter
bot using the twitter_push module.