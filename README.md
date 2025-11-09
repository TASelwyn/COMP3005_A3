# COMP 3005 – Database Management Systems
## Assignment 3
Implement a PostgreSQL database using the provided schema and write an application in your language of choice that connects to this database to perform specific CRUD (Create, Read, Update, Delete) operations.
## Running Django
1. Run postgres using docker
```docker compose up -d```
2. Install python dependencies
```pip install -r requirements.txt```
3. Apply Django base migrations
```python manage.py migrate```
4. Update Django migrations for "students" application
```python manage.py makemigrations```
```python manage.py migrate```
5. Load initial data from file
```python manage.py loaddata initial_data.json```
6. Run application
```python manage.py runserver```
