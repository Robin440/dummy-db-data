from django.contrib import admin

# Register your models here.
from app.models import Book,Author,Publisher,BookAndAuthor

class BookAdmin(admin.ModelAdmin):
    list_display = ('id','title')
admin.site.register(Book,BookAdmin)

admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(BookAndAuthor)

