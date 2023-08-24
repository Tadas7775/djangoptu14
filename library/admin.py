from django.contrib import admin
from . models import Author, Book, Genre, BookInstances
# Register your models here.


class BooksInstanceInLine(admin.TabularInline):
    model = BookInstances
    extra = 0


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', "display_genre")
    inlines = [BooksInstanceInLine]
    search_fields = ('title', 'author__last_name')


@admin.register(BookInstances)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', "id", 'status', 'due_back')
    list_editable = ('status', 'due_back')
    list_filter =  ('status', 'due_back')
    search_fields = ('id', 'book__title') #naudojama vaikine(book) properties sujungia su tevine(title) properties
    fieldsets = (
        ('General', {'fields': ('id', 'book')}),
        ('Aviablility', {'fields': ('status', 'due_back')}),
    )

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name','first_name', 'display_books')



# admin.site.register(Author)
admin.site.register(Genre)
