﻿# BookAPI Project

This is a simple API built with Django to manage books. It includes basic CRUD operations for managing books in a database.

1. Clone the repository:
git clone https://github.com/PhatBen234/BookAPI.git </br>
cd BookApi

2. Install dependencies:

pip install -r requirements.txt

3. Run migrations to set up the database: (Because Django has connect with SQL lite, just with this command you can automatically create SQL DB by model file)
python manage.py migrate

4. Run the development server:
python manage.py runserver


