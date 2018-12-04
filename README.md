#

![project flowchart](https://github.com/ktroutman/tweego/blob/master/title_image.png)

[![Build Status](https://travis-ci.org/ErikMann/tweego.svg?branch=master)](https://travis-ci.org/ErikMann/tweego)
## Setting up development

See documentation: https://tweego.readthedocs.io/en/latest/

1. Clone the repository

2. Create a vitual enviroment

	conda create -n tweego

3. Install all required modules:

  `pip install -r requirements.txt`

	`pip install -r requirements_dev.txt`

	in case problems with permissions, try:
	`pip install --user -r requirements_dev.txt`

4. Add your twitter keys and mongo connection to config.py:
	    `cp tweego/config_example.py tweego/config.py`

   *Note that this confidential config.py file will be git-ignored and not shared publicly.*

5. Install the program locally:
    `pip install -e .`

6. Add search keywords which you would like to tweet about: `tweego/keywords.py`

7. Install MongoDB and start the server

8. Run tests
