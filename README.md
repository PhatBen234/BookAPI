# BookAPI Project </br>

This is a simple API built with Django to manage books. It includes basic CRUD operations for managing books in a database. </br>

1. Clone the repository: </br>
- git clone https://github.com/PhatBen234/BookAPI.git </br>
- cd BookAPI (this will help you on the project for example Now you on E:\BookAPI after first cd) </br>

2. Install dependencies: </br>
- cd BookAPI (Continue go this part to set up you on E:\BookAPI\BookAPI now)
- pip install -r requirements.txt </br>

3. Run migrations to set up the database: (Because Django has connect with SQL lite, just with this command you can automatically create SQL DB by model file) </br>
- python manage.py makemigrations books </br>
- python manage.py migrate 

4. Run the development server: </br>
- python manage.py runserver </br>


