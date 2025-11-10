# COMP 3005 – Database Management Systems
## Assignment 3
This project implements the objective schema using **PostgreSQL** with a basic web application in order to visualize the operations using **Django**. 
It demonstrates full CRUD operations on the `students` table using REST calls implemented using Django's ORM and a simple html website for interfacing.

## Objective
Implement a PostgreSQL database using the provided schema and write an application in your language of choice that connects to this database to perform specific CRUD (Create, Read, Update, Delete) operations.

## Comment
Due to the final project being allowed to use ORM, I implemented this using ORM. The assignment page does not mention whether we are allowed to use it.
In light of this, I populated "schema.sql" with all the necessary SQL statements in order to do the CRUD operations. Additionally and with that in mind, the database is configured to use postgres in COMP3005_A3/settings.py thus meeting the "PostgreSQL" database requirement.

https://youtu.be/ewENe9VeqoU

## Technologies Used
- Python 3.11
- Django 5.2.8
- PostgreSQL 18
- Docker 4.50.0
## Project Structure
```bash
COMP3005_A3/           # Django Base
- settings.py          # settings (Configuring postgresql)
students/
- migrations/          # Database ORM Migrations
- DatabaseFunctions.py # CRUD Operations
- models.py            # Object Relational Mapping Models
- urls.py              # Configuring web urls
- views.py             # HTTP Endpoints
templates/
- students/            # html user interface files
compose.yaml           # Docker compose file
manage.py              # Django's cli python file
requirements.txt       # Python packages
schema.sql             # CRUD Operations in SQL Form
```

## Running the assignment
1. Run postgres using docker
```bash
docker compose up -d
```
2. Install python dependencies
```bash
pip install -r requirements.txt
```
4. Apply Django migrations to setup database
```bash
python manage.py migrate
```
5. Run application
```bash
python manage.py runserver
```

## Resetting the database
In order to revert the database to its initiate state:
1. Running migrations back to 0001 (table creation) will undo everything to the database.
```bash
python manage.py migrate students 0001
```
2. Running migrations will input default data
```bash
python manage.py migrate 
```

## License
Copyright Thomas Selwyn. All rights reserved.

This project and all associated code were created as part of COMP 3005 Assignment 3 at Carleton University.

Permission is hereby granted to **Carleton University instructors, teaching assistants, and graders** to view, execute, and evaluate this code for academic assessment purposes only.

Redistribution, modification, or reuse of this code or documentation outside of course evaluation, whether in whole or in part, is **strictly prohibited**.
