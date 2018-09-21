=====
Usage
=====

1. Clone the repository

2. Install MongoDB and start the server

3. Install all required modules: pip install -r requirements.txt

4. Install the program locally: pip install -e .

5. Add your credentials: cp tweego/config_example.py tweego/config.py

6. Add your twitter keys and mongo connection to config.py

7. Add search keywords which you would like to tweet about: tweego/keywords.py

8. Run tests: pytest