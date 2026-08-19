# Movie Watchlist Application

A simple Django web application for managing a personal movie watchlist.  
Users can add, edit, delete movies, mark them as watched/unwatched, search by title, and view movies ordered by newest first.  
Built with Django and PostgreSQL.

## Features

- Display all movies on the homepage (newest first)
- Add a new movie
- Edit an existing movie
- Delete a movie
- Mark a movie as Watched / Unwatched
- Search movies by title
- Django Admin integration for managing movies

## Setup Instructions

### 1.Clone the repository

```bash
git clone https://github.com/Ji-raffe/django-movie-watchlist.git
cd movie-watchlist

```

### 2.Set up virtual environment

Creaate and activate a Python virtual environment:
- On Window:
```bash
python -m venv venv
venv\Scripts\activate
```

### 3.Install Dependencies
Install all required Python Pakages:
```bash
pip install -r requirements.txt
```

### 4.Database Configuration
1. Open PostgresSQL and create a new database for this project(e.g., movie_watchlist_db)
2. Open setting.py in movie_watchlist folder

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'movie_watchlist_db',
        'USER': '<your_postgres_username>',
        'PASSWORD': '<your_postgres_password>',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5.Run database migrations
Apply the database migrations to set up the database tables:

```bash
python manage.py makeimgrations
python manage.py migrate
```

### 6.Create superuser
Create an admin account to access the Django Admin interfacce:
```bash
python manage.py createsuperuser
```

### 7.Run the server
Start the local development server:
```bash
python manage.py runserver
```
Open your web browser and visit: http://127.0.0.1:8000/

## Academic Integrity & AI Usage Acknowledgment

In accordance with academic integrity guidelines, AI tools were used as an educational assistant during the development of this project. The specific usages include:

*   **Syntax & Command Reference:** Researching standard Django syntax, model queries (`icontains`), and PostgreSQL configurations.
*   **Debugging & Troubleshooting:** Diagnosing logic errors (e.g., variable overwriting in views, URL routing mismatches, and database connection setup).
*   **Documentation:** Assisting in formatting and structuring setup instructions in this README file.