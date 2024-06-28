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
        """
        This class is used to define the ordering of the books in the admin panel.
        """
        unique_together = ('title', 'author')

class BookAndAuthor(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
   
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    # def __str__(self):
    #     return self.title
    
    class Meta:
        """
        This class is used to define the ordering of the books in the admin panel.
        """
        unique_together = ('book', 'author')



