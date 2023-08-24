import uuid

from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField("Vardas", max_length=100)
    last_name = models.CharField("Pavarde", max_length=100)
    description = models.TextField("Aprasymas", max_length=2000, default="Labai geras autorius")

    class Meta:
        ordering = ["last_name", "first_name"]

    def display_books(self): # pridedam prie autoriaus jo knygas per Books.author kur related_name
       return ", ".join(book.title for book in self.books.all())# galima kirpti rodomu zanru kieki su slice [:2]

    display_books.short_description = "Knygos"


    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

class Book(models.Model):
    title = models.CharField("Pavadinimas", max_length=200)
    summary = models.TextField("Aprasymas", max_length=1000)
    isbn = models.CharField("ISBN", max_length=13, help_text='13 Simbolių <a href="https://www.isbn-international.org/content/what-isbn"> ISBN kodas</a>')
    author = models.ForeignKey("Author", on_delete=models.SET_NULL, null=True, related_name='books') #related_name padaro prie autoriaus prijungia autoriaus obijekto knygas
    genre = models.ManyToManyField("Genre")


    class Meta:
        ordering = ["title"]



    def __str__(self):
        return f"{self.title}"

    def display_genre(self):
       return ", ".join(genre.name for genre in self.genre.all())# galima kirpti rodomu zanru kieki su slice [:2]

    display_genre.short_description = "Zanras"




class Genre(models.Model):
    name = models.CharField("Pavadinimas", max_length=20, help_text="galima prideti kelis zanrus")

    class Meta:
        verbose_name = "Zanras"
        verbose_name_plural = "Zanrai"





    def __str__(self):
        return f"{self.name}"


class BookInstances(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    book = models.ForeignKey("Book", on_delete=models.CASCADE)
    due_back = models.DateField("Bus prieinama", null=True, blank=True)

    LOAN_STATUS = (
        ('a', 'Administruojama'),
        ('p', 'Paimta'),
        ('g', 'Galima paimti'),
        ('r', 'Rezervuota')
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        blank=True,
        help_text="Kopijos statusas"
    )

    class Meta:
        ordering = ['due_back']



    def __str__(self):
        # return f"{self.id}, {self.book}, {self.book.author}"
          return f"{self.id}"