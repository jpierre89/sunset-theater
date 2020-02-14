# Theater API

>RESTful API for Sunset Theater

## First time setup for liux
__0. Install python3 and pip3__

__1. Clone Repo__ <br>
$ git clone https://git.txstate.edu/jfp35/Theater_API

__2. Create virtual environment from project root directory__ <br>
$ python3 -m venv env

__3. Activate virtual environment from project root directory__ <br>
$ source env/bin/activate

__4. Install dependencies__ <br>
$ pip3 install -r requirements.txt

__5. Run__ <br>
$ flask run

__6. Navigate to http://127.0.0.1:5000 in browser__ 

## Flask Error Solutions
* OSERROR: Address already in use
    * e.g. forgot to quit server
    * Solution: find pid and quit

```
$ ps -fA | grep python
$ kill -9 <pid>
```

## updating frontend distribution
* Build frontend distribution in angular project:
```
$ ng build --prod
```
* Insert front end distribution files into this project
    * copy /dist/<project name>/index.html to templates folder
    * copy dist/<project name>/* to static folder 
    
#### Flask Shell - Removed
* Use in venv to get python session with auto project imports
```
$ flask shell
```

#### Migration - Removed
* Changes schema while maintaining data in database
1. Generate migration script
2. run script to upgrade database

```
$ flask db migrate -m 'commit message'
$ flask db upgrade
```

#### Migration Error Solutions
* note: SQLite doesn's support alter table, thus set render_as_batch
    * https://github.com/miguelgrinberg/Flask-Migrate/issues/61
* "target Database is not up to date"
    * https://stackoverflow.com/questions/17768940/target-database-is-not-up-to-date
```
$ flask db stamp head
```
