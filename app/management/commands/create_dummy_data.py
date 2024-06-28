# myapp/management/commands/create_dummy_data.py
from django.core.management.base import BaseCommand
from app.models import Author, Publisher, Book, BookAndAuthor
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Generate dummy data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Create Authors
        authors = []
        for _ in range(10):
            author = Author(
                name=fake.name(),
                birthdate=fake.date_of_birth()
            )
            author.save()
            authors.append(author)

        # Create Publishers
        publishers = []
        for _ in range(5):
            publisher = Publisher(name=fake.company())
            publisher.save()
            publishers.append(publisher)

        # Track created books to ensure unique combinations of title and author
        created_books = set()

        # Create Books
        books = []
        for _ in range(20):
            title = fake.sentence(nb_words=3)
            author = random.choice(authors)

            # Ensure the combination of title and author is unique
            while (title, author) in created_books:
                title = fake.sentence(nb_words=3)

            book = Book(
                title=title,
                publication_date=fake.date(),
                author=author
            )
            book.save()
            created_books.add((title, author))

            # Add many-to-many relationship
            book.publishers.set(random.sample(publishers, k=random.randint(1, 3)))
            book.save()

            books.append(book)

        # Track created BookAndAuthor to ensure unique combinations of book and author
        created_book_authors = set()

        for book in books:
            for author in authors:
                # Ensure the combination of book and author is unique
                # while (book, author) in created_book_authors:
                #     book = random.choice(books)
                #     author = random.choice(authors)

                book_and_author = BookAndAuthor(
                    book=book,
                    author=author
                )
                book_and_author.save()
                created_book_authors.add((book, author))

        self.stdout.write(self.style.SUCCESS('Successfully created dummy data'))
