## Theater API

>RESTful API for Sunset Theater

Note: If no user with admin role, start secure = false to create user with superuser role in /admin url.

#### Update frontend distribution
* Angular CLI on frontend directory:
```
$ ng build --prod
```
* copy /dist/<project name>/index.html to templates folder
* copy dist/<project name>/* to static folder 

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

#### Migration - Removed
* Changes schema while maintaining data in database
1. Generate migration script
2. run script to upgrade database

```
$ flask db migrate -m 'commit message'
$ flask db upgrade
```

#### Flask Shell - Removed
* Use in venv to get python session with auto project imports
```
$ flask shell
```

#### Flask Error Solutions
* OSERROR: Address already in use
    * e.g. forgot to quit server
    * Solution: find pid and quit

```
$ ps -fA | grep python
$ kill -9 <pid>
```

#### Migration Error Solutions
* note: SQLite doesn's support alter table, thus set render_as_batch
    * https://github.com/miguelgrinberg/Flask-Migrate/issues/61
* "target Database is not up to date"
    * https://stackoverflow.com/questions/17768940/target-database-is-not-up-to-date
```
$ flask db stamp head
```
