# Theater API

>API for Sunset Theater

## First time setup for linux

```sh
$ python3 -m venv env
$ source env/bin/activate
$ pip3 install -r requirements.txt
$ flask run
```


## Flask Error Solutions
* OSERROR: Address already in use
    * e.g. forgot to quit server
    * Solution: find pid and quit

```
$ ps -fA | grep python
$ kill -9 <pid>
```

## Updating frontend distribution
* Build frontend distribution in angular project:
```
$ ng build --prod
```
* Insert front end distribution files into this project
    * copy /dist/<project name>/index.html to templates folder
    * copy dist/<project name>/* to static folder 
    
## Flask Shell - Removed
* Use in venv to get python session with auto project imports
```
$ flask shell
```

## Migration - Removed
* Changes schema while maintaining data in database
1. Generate migration script
2. run script to upgrade database

```
$ flask db migrate -m 'commit message'
$ flask db upgrade
```

## Migration Error Solutions
* note: SQLite doesn's support alter table, thus set render_as_batch
    * https://github.com/miguelgrinberg/Flask-Migrate/issues/61
* "target Database is not up to date"
    * https://stackoverflow.com/questions/17768940/target-database-is-not-up-to-date
```
$ flask db stamp head
```
