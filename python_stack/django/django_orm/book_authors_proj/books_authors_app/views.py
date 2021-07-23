from django.shortcuts import render, redirect
from .models import Author, Book

# Create your views here.
def index(request):
    return render(request, 'index.html')

def book(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'book.html', context)

def author(request):
    context = {
        'authors': Author.objects.all()
    }
    return render(request, 'author.html', context)

def add_book(request):
    if request.method == "POST":
        Book.objects.create(title = request.POST['title'], desc = request.POST['desc'])
    return redirect('/')

def add_author(request):
    if request.method == "POST":
        Author.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], notes = request.POST['notes'])
    return redirect('/authors')


def book_info(request, book_id):
    books = Book.objects.all()
    context = {
        'book': Book.objects.get(id=book_id),
        'authors': Author.objects.all()
    }
    return render(request, 'book_info.html', context)

def author_info(request, author_id):
    authors = Author.objects.all()
    context = {
        'author': Author.objects.get(id=author_id),
        'books': Book.objects.all()
    }
    return render(request, 'author_info.html', context)

def process_new_author(request, book_id):
    book = Book.objects.get(id=book_id)
    author = Author.objects.get(id=request.POST['author'])
    book.authors.add(author)
    return redirect(f"/books/{book_id}")


def process_new_book(request, author_id):
    author = Author.objects.get(id=author_id)
    book = Book.objects.get(id=request.POST['book'])
    author.books.add(book)
    return redirect(f"/authors/{author_id}")