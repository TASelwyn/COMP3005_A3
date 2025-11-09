# COMP 3005 – Database Management Systems
## Assignment 3
Implement a PostgreSQL database using the provided schema and write an application in your language of choice that connects to this database to perform specific CRUD (Create, Read, Update, Delete) operations.

## Comment
This entire assignment was implemented using Django, a web framework for python with a strong ORM system. 
The database is configured to use postgres in COMP3005_A3/settings.py thus meeting the "PostgreSQL" database requirement. 
Django provides abstraction models for ORM, and thus no raw sql will be used for this assignment.

## Running Django
1. Run postgres using docker
```docker compose up -d```
2. Install python dependencies
```pip install -r requirements.txt```
3. Update Django migrations
```python manage.py makemigrations```
4. Apply Django migrations
```python manage.py migrate```
5. Load initial data from file
```python manage.py loaddata initial_data.json```
6. Run application
```python manage.py runserver```
