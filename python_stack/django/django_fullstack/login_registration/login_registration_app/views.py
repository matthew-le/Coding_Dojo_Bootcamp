from django.shortcuts import render, redirect
from .models import User
import bcrypt
from django.contrib import messages

# Create your views here.

def login_register(request):
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
        return redirect('/index')
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
    return redirect('/')

def index(request):
    context = {
        'user': User.objects.get(id=request.session['userid'])
    }
    return render(request, 'index.html', context)

def logout(request):
    request.session.flush()
    return redirect('/')