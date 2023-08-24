from django.shortcuts import render, get_object_or_404
from django.http import  HttpResponse

from .models import Book, BookInstances, Author, Genre



def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstances.objects.all().count()
    num_instances_aivable = BookInstances.objects.filter(status__exact='g').count()
    num_autoriu = Author.objects.all().count()


    context = {
        'num_books_t': num_books,
        'num_instances_t': num_instances,
        "num_instances_aivable_t" : num_instances_aivable,
        "num_autoriu_t": num_autoriu



    }

    return render(request, 'index.html', context=context)
# Create your views here.

def authors(request):

    authors = Author.objects.all()
    print(authors)
    context_t = {
        "authors_t": authors

    }
    return render(request, "authors.html", context=context_t)



def author(request, author_id):
    single_author = get_object_or_404(Author, pk=author_id)
    context_t = {
        "author_t": single_author
    }
    return render(request, "author.html", context=context_t)