import configparser
from urllib import parse
import sys
import argparse

"""temporary comment 04/12/2018: Seems to be a currently unused file,
leftover from an earlier attempt to handle configuration a bit more modularly
(via the ConfigParser python package). Leaving file here for reference,
but simply making note of this to avoid confusion."""


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
with open("tweego/config.ini", 'w') as configfile:
    config.write(configfile)
