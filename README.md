INTELLI-SEARCH
A vertical search engine on AI articles

-Installation
Any Linux distribution and MacOs System

1.Open your terminal
2.Check python3 --version (better if you have a version >= 3.7),
  if you have an older version you can type and execute: sudo apt-get update, sudo apt-get install python 3.9
3.Check pip3 --version, if there isn't any pip3 type and execute: sudo apt install python3-pip.
4.Install all the pip packages in the requirements.txt file
9.cd /path/to/intelli-search/backend 
10.export FLASK_APP=__init__.py
11.export FLASK_ENV=development
12.flask run

For Windows cmd, use set instead of export:
1.set FLASK_APP=__init__.py
2.set FLASK_ENV=development
3.flask run

For Windows PowerShell, use $env: instead of export:

1.$env:FLASK_APP = "__init__.py"
2.$env:FLASK_ENV = "development"
3.flask run

You’ll see output similar to this:

* Serving Flask app "flaskr"
* Environment: development
* Debug mode: on
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
* Debugger PIN: 855-212-761

TEST
1.Digit http://127.0.0.1:500/home on you browser
1.Type your query on the search bar
2.Click search and check the results
3.Click open cso (near the search bar) to discover more info on the query
