# INTELLI-SEARCH

A vertical search engine on AI articles

- ## Installation

Any Linux distribution and MacOs System

1. ## Terminal

Open your terminal

cd /path/to/intelli-search

Check python3 --version (better if you have a version >= 3.7), if you have an older version you can type and execute: sudo apt-get update, sudo apt-get install python 3.9

3. ## Pip

Check pip3 --version, if there isn't any pip3 type and execute: sudo apt install python3-pip.

4. ## Virtual Env 

Create a virtual environment 
$ python3 -m venv tutorial-env

On Unix or MacOS, run:
$ source tutorial-env/bin/activate

On Windows, run:
tutorial-env\Scripts\activate.bat

5. ## Project Requirements 

Install all the pip packages from the requirements.txt file

$ pip install -r requirements.txt

6. ## Set up Flask Environment

For Mac and Linux:
$ cd /backend 
$ export FLASK_APP=__init__.py
$ export FLASK_ENV=development

For Windows cmd, use set instead of export:
set FLASK_APP=__init__.py
set FLASK_ENV=development

For Windows PowerShell, use $env: instead of export:
$env:FLASK_APP = "__init__.py"
$env:FLASK_ENV = "development"

6. ## Run it
Now you can run the flask application:
$ flask run

You’ll see output similar to this:

* Serving Flask app "flask"
* Environment: development
* Debug mode: on
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
* Debugger PIN: 855-212-761

7. ## Use it!

- Digit http://127.0.0.1:5000/home on you browser
- Type your query on the search bar
- Click search and check the results
- Click open cso (near the search bar) to discover more info on the query

