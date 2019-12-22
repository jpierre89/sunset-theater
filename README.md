## Theater API

>RESTful API for access to Theater Database returning JSON objects consumed by client browser.
>Also has admin login/access views

#### Resources
* Flask RESTful Workshop
* The Flask Mega Tutorial

#### Tools
* Python3
* Flask RESTful
* Virtual Environment
* Ubuntu Linux
* PyCharm

#### Dependencies 
1. Create virtual environment in project root
2. Activate virtual environment
3. Install dependencies

```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip3 install -r requirements.txt 
```

#### Run
Ensure virtual environment is activated
Note: FLASK_APP environment variable is set by .flaskenv

```
$ export FLASK_APP=main.py
$ flask run
```
   
Navigate to URL in a browser

#### Database Migration
Changes schema without creating new db (Creates db if it doesn't exist)
Note: migration repository exists in application root
Note: can downgrade to undue last migration
Note: Does not support dropping/altering*

1. Generate migration script
2. run script to upgrade database

```
$ flask db migrate -m 'commit message'
$ flask db upgrade
```

#### Common Issues
* OSERROR: Address already in use
    * e.g. forgot to quit server
    * Solution: find pid and quit

```
$ ps -fA | grep python
$ kill -9 <pid>
```