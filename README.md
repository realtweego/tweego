# 

![project flowchart](https://github.com/ktroutman/tweego/blob/master/title_image.png)


## Setting up development

1. Clone the repository

2. Install MongoDB and start the server

3. Install all required modules:

    pip install -r requirements.txt
    
4. Install the program locally:
 
    pip install -e .
 
5. Add your credentials

    `cp tweego/config_example.py tweego/config.py`
    
    Add your twitter keys and mongo connection to config.py

6. Add search keywords which you would like to tweet about in `tweego/keywords.py`
	
7. Run tests

   pytest

[![Build Status](https://travis-ci.org/ErikMann/tweego.svg?branch=master)](https://travis-ci.org/ErikMann/tweego)
