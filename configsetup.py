import configparser
from urllib import parse
import sys
import argparse

config = configparser.ConfigParser()

config['twitter'] = {
    "consumer_key": "",
    "consumer_secret": "",
    "access_token": "",
    "access_token_secret": ""
    }


config['database'] = {
    "client": f"www.example.io",
    "username": parse.quote_plus("example_user"),
    "password": parse.quote_plus("example_password")
}

config['cloudmachine'] = {
    "username":"",
    "password":""
}

#if somewhere in directory does not exist config file:
with open("tweepy\config.ini", 'w') as configfile:
    config.write(configfile)
