from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import User, Message, Comment

# Create your views here.

def log_and_reg(request):
    if 'userid' in request.session:
        return redirect('/wall')
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

def wall(request):
    context = {
        'user': User.objects.get(id=request.session['userid']),
        'all_messages': Message.objects.all()
    }
    return render(request, 'wall.html', context)

def post_message(request):
    errors = Message.objects.validator(request.POST)
    if errors: 
        for val in errors.values():
            messages.error(request,val)
    else:
        Message.objects.create(
            content = request.POST['content'],
            creator = User.objects.get(id=request.session['userid'])
        )
    return redirect('/wall')

def post_comment(request, message_id):
    errors = Comment.objects.validator(request.POST)
    if errors: 
        for val in errors.values():
            messages.error(request,val)
    else:
        Comment.objects.create(
            content = request.POST['content'],
            creator = User.objects.get(id=request.session['userid']),
            message = Message.objects.get(id=message_id)
        )
    return redirect('/wall')

def user(request, user_id):
    context = {
        'user': User.objects.get(id=user_id)
    }
    return render(request, 'user.html', context)

def like(request, message_id):
    message = Message.objects.get(id=message_id)
    user = User.objects.get(id=request.session['userid'])
    message.users_who_liked.add(user)
    return redirect('/wall')

def unlike(request, message_id):
    message = Message.objects.get(id=message_id)
    user = User.objects.get(id=request.session['userid'])
    message.users_who_liked.remove(user)
    return redirect('/wall')

def edit(request, message_id):
    context = {
        'message': Message.objects.get(id=message_id)
    }
    return render(request, 'edit_message.html', context)

def update_message(request, message_id):
    errors = Message.objects.validator(request.POST)
    if errors: 
        for val in errors.values():
            messages.error(request,val)
    else:
        message = Message.objects.get(id=message_id)
        message.content = request.POST['content']
        message.save()
    return redirect(f'/messages/{message_id}/edit')

def update_user(request, user_id):
    errors = User.objects.edit_validator(request.POST, user_id)
    if errors: 
        for val in errors.values():
            messages.error(request,val)
    else:
        user = User.objects.get(id=user_id)
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        password = request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        user.password = pw_hash
        user.save()
    return redirect('/index')
