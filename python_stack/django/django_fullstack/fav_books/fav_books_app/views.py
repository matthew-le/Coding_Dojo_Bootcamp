from django.shortcuts import render, redirect
from .models import User, Book
from django.contrib import messages
import bcrypt

# Create your views here.
def log_and_reg(request):
    if 'userid' in request.session:
        return redirect('/books')
    return render(request, 'login_register.html')

def register(request):
    errors = User.objects.user_validator(request.POST)
    if errors:
        for key, val in errors.items():
            messages.error(request,val)
    elif request.method=="POST":
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        user = User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            password=pw_hash,
            confirm_password=request.POST['confirm_password'],
            birthday=request.POST['birthday']
        )
        request.session['userid'] = user.id
        messages.success(request, 'Succesfully registered account!')
        return redirect('/books')
    return redirect('/')

def login(request):
    users = User.objects.filter(email=request.POST['email'])
    if users:
        logged_user = users[0]
        if bcrypt.checkpw(request.POST['password'].encode(),logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            messages.success(request, 'Successfully logged in!')
            return redirect('/index')
        else:
            messages.error(request, 'invalid email or password entered')
    else: 
        messages.error(request, 'Account not found with email')
    return redirect('/books')

def logout(request):
    request.session.flush()
    return redirect('/')

def books(request):
    context = {
        'user': User.objects.get(id=request.session['userid']),
        'all_books': Book.objects.all()
    }
    return render(request, 'books.html', context)

def add_book(request):
    errors = Book.objects.book_validator(request.POST)
    if errors: 
        for val in errors.values():
            messages.error(request,val)
    else:
        user = User.objects.get(id=request.session['userid'])
        book = Book.objects.create(
            title = request.POST['title'],
            desc =request.POST['desc'],
            uploaded_by = User.objects.get(id=request.session['userid'])
        )
        user.books_user_favorited.add(book)
    return redirect('/books')

def edit_book(request, book_id):
    context = {
        'book': Book.objects.get(id=book_id),
        'user': User.objects.get(id=request.session['userid'])
    }
    return render(request, 'edit_book.html', context)

def update_book(request, book_id):
    errors = Book.objects.book_validator(request.POST)
    if errors: 
        for val in errors.values():
            messages.error(request,val)
    else:
        book = Book.objects.get(id=book_id)
        book.title = request.POST['title']
        book.desc = request.POST['desc']
        book.save()
    return redirect(f'/books/{book_id}/edit')

def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect('/')

def favorite(request, book_id):
    book = Book.objects.get(id=book_id)
    user = User.objects.get(id=request.session['userid'])
    user.books_user_favorited.add(book)
    return redirect('/')

def unfavorite(request, book_id):
    book = Book.objects.get(id=book_id)
    user = User.objects.get(id=request.session['userid'])
    user.books_user_favorited.remove(book)
    return redirect('/')