
# Django Project: Fake Data Generation

This project demonstrates how to generate and populate a Django PostgreSQL database with dummy data, including handling `unique_together` constraints and relationships like `ForeignKey` and `ManyToManyField`.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Models](#models)
- [Generating Dummy Data](#generating-dummy-data)
- [Usage](#usage)
- [License](#license)

## Prerequisites

- Python 3.x
- Django
- PostgreSQL
- `Faker` library

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/fake_data_generation.git
    cd fake_data_generation
    ```

2. **Set Up Virtual Environment**:
    ```bash
    python -m venv fake_env
    source fake_env/bin/activate  # On Windows, use `fake_env\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```bash
    pip install django faker psycopg2-binary
    ```

4. **Configure PostgreSQL**:
    Ensure you have PostgreSQL installed and a database created. Update your `settings.py` with your database credentials:
    ```python
    # myproject/settings.py
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'mydatabase',
            'USER': 'myuser',
            'PASSWORD': 'mypassword',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

5. **Run Migrations**:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

## Models

The project includes the following models:

- **Author**: Represents an author with a name and birthdate.
- **Publisher**: Represents a publisher with a name.
- **Book**: Represents a book with a title, publication date, author (`ForeignKey` to `Author`), and publishers (`ManyToManyField` to `Publisher`).
- **BookAndAuthor**: Represents a unique relationship between a book and an author (`ForeignKey` to `Book` and `Author`).

### Model Definitions

```python
# myapp/models.py
from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField()
    def __str__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publishers = models.ManyToManyField(Publisher)
    def __str__(self):
        return self.title
    
    class Meta:
        unique_together = ('title', 'author')

class BookAndAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('book', 'author')
