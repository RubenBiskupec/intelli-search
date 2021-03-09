pip install flask

For Linux and Mac:

$ export FLASK_APP=_init_.py
$ export FLASK_ENV=development
$ flask run
For Windows cmd, use set instead of export:

> set FLASK_APP=_init_.py
> set FLASK_ENV=development
> flask run
For Windows PowerShell, use $env: instead of export:

> $env:FLASK_APP = "_init_.py"
> $env:FLASK_ENV = "development"
> flask run

You’ll see output similar to this:

* Serving Flask app "flaskr"
* Environment: development
* Debug mode: on
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
* Debugger PIN: 855-212-761

