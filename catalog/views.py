from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Book, Author, BookInstance
from django.views.generic import ListView, DetailView
# Create your views here.

class AuthorDetailView(DetailView):
    model = Author
    context_object_name = 'author'

class AuthorListView(ListView):
    model = Author
    paginate_by = 4


class BookDetailView(DetailView):
        model = Book
        context_object_name = 'book'

class BookListView(ListView):
    model = Book
    context_object_name = 'books'
    paginate_by = 3
def index(request):
    text_head = "You can get e books on this site"
    books = Book.objects.all()
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status=2).count
    authors = Author.objects
    num_authors = Author.objects.count()
    #text_body = "Body of main page"
    context = {'text_head': text_head, 'books': books,
               'num_books': num_books, 'num_instances': num_instances,
               'num_instances_available': num_instances_available,
               'authors':authors, 'num_authors': num_authors}
    return render(request, 'catalog/index.html', context)

def about(request):
    text_head = "Data about company"
    name = "World of books"
    context = {'text_head': text_head, 'name': name}
    return render(request, 'catalog/about.html', context)


def contact(request):
    text_head = "Contacts"
    name = "IP Tsokalov"
    address = "Serova 4/1"
    tel = "8-928-338-29-98"
    email = "tsokalov1994@gmail.com"

    context = {'text_head': text_head, 'name': name, 'address': address, 'tel': tel, 'email': email }
    return render(request, 'catalog/contact.html', context)
