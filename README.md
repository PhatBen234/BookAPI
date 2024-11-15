# BookAPI Project

This is a simple API built with Django to manage books. It includes basic CRUD operations for managing books in a database.

## 1. Clone the repository:

- `git clone https://github.com/PhatBen234/BookAPI.git`
- `cd BookAPI` (This will navigate you to the project directory, for example, `E:\BookAPI` after the first `cd`)

## 2. Install dependencies:

- Navigate to the project folder: `cd BookAPI` (Now, you are in `E:\BookAPI\BookAPI`)
- Install the required dependencies: `pip install -r requirements.txt`

## 3. Run migrations to set up the database:

(Since Django is connected to SQLite, these commands will automatically create the SQL database using the model file.)

- `python manage.py makemigrations books`
- `python manage.py migrate`

## 4. Run the development server:

- `python manage.py runserver`

Once the server is running, you can check the API at the following URL:

- API: `http://127.0.0.1:8000/api/books/`
  ![Screenshot of the API Get by Django (no data)](images/GetBooks1.png)

---

## Creating a Book (POST Request)

Now let's move on to the **CREATE** part. In this section, I will demonstrate how to add a book using Postman.

- API: `http://127.0.0.1:8000/api/books/add/`
  ![Screenshot of the API Create by Postman](images/Create.png)

After adding, two more books have been created.

---

## Reading the Books (GET Request)

You can read all the books you have created using the Django REST API:

- API: `http://127.0.0.1:8000/api/books/`
  ![Screenshot of the API Get by Django (already have 3 books)](images/GetBooks2.png)

You can also read a specific book by its ID:

- API: `http://127.0.0.1:8000/api/books/1`
  ![Screenshot of the API Get a specific book by ID (Django)](images/GetBook1.png)

---

## Updating a Book (PUT Request)

Now, let's move to the **PUT** path. I will use Postman to update a book.

- API: `http://127.0.0.1:8000/api/books/update/2/`
  ![Screenshot of the API PUT request](images/Put.png)

After the update, you can see the updated book at:

- API: `http://127.0.0.1:8000/api/books/2`
  ![Screenshot of the API after PUT request](images/GetBook2.png)

---

## Deleting a Book (DELETE Request)

Finally, let's go to the **DELETE** path. I will use Postman to delete a book.

- API: `http://127.0.0.1:8000/api/books/delete/3/`
  ![Screenshot of the API DELETE request](images/Put.png)

After deletion, the updated list of books will be shown here:

- API: `http://127.0.0.1:8000/api/books/`
  ![Screenshot of the API after DELETE request](images/GetBooks3.png)

## Validation

The API includes validation checks to ensure that the data is correct before being saved to the database. Here are some examples:
![Price must be positive: The price of a book must be a positive number.](images/PriceMustBePositive.png)
![ISBN must be unique: If you try to add a book with the same ISBN as an existing one, it will return an error.](images/ISBN_Exists.png)
![Date format must be correct: The publication date must follow the YYYY-MM-DD format.](images/DateFormat.png)

## Error Handling

The API includes error handling to provide meaningful messages when something goes wrong. Here is an example:
![Book Not Found: If you try to access a book that does not exist, the API will return an error message indicating that the book was not found.](images/CatchErrorBookNotFound.png)

## Time Spent on the Project

- **Friday**: 4:00 PM - 5:00 PM
- **Sunday**: 6:00 PM - 9:00 PM
- **Monday**: 8:00 AM - 1:30 PM
