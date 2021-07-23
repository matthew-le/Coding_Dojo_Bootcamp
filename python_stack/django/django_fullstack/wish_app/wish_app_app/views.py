from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import User, Wish
# Create your views here.

def log_and_reg(request):
    if 'userid' in request.session:
        return redirect('/wishes')
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
        )
        request.session['userid'] = user.id
        messages.success(request, 'Succesfully registered account!')
        return redirect('/wishes')
    return redirect('/')

def login(request):
    users = User.objects.filter(email=request.POST['email'])
    if users:
        logged_user = users[0]
        if bcrypt.checkpw(request.POST['password'].encode(),logged_user.password.encode()):
            request.session['userid'] = logged_user.id
            messages.success(request, 'Successfully logged in!')
            return redirect('/wishes')
        else:
            messages.error(request, 'invalid email or password entered')
    else: 
        messages.error(request, 'Account not found with email')
    return redirect('/')

def index(request):
    context = {
        'user': User.objects.get(id=request.session['userid']),
        'wishes': Wish.objects.filter(creator=User.objects.get(id=request.session['userid'])).exclude(granted=True),
        'granted_wishes': Wish.objects.filter(granted=True),

    }
    return render(request, 'index.html', context)

def logout(request):
    request.session.flush()
    return redirect('/')

def new_wish(request):
    context = {
        'user': User.objects.get(id=request.session['userid'])
    }
    return render(request, 'wish.html', context)

def make_wish(request):
    errors = Wish.objects.validator(request.POST)
    if errors:
        for val in errors.values():
            messages.error(request,val)
    else:
        Wish.objects.create(
            item = request.POST['item'],
            desc = request.POST['desc'],
            creator = User.objects.get(id=request.session['userid']),
            granted = request.POST['granted']
        )
        return redirect('/wishes')
    return redirect('/wishes/new')

def edit_wish(request, wish_id):
    one_wish = Wish.objects.get(id=wish_id)
    context = {
        'wish': one_wish
    }
    return render(request, 'edit_wish.html', context)

def update_wish(request, wish_id):
    errors = Wish.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/wishes/{wish_id}/edit')
    else: 
        wish = Wish.objects.get(id=wish_id)
        wish.item = request.POST['item']
        wish.desc = request.POST['desc']
        wish.save()
        # messages.success(request, "Show successfully updated")

        return redirect('/wishes')

def delete_wish(request, wish_id):
    to_delete = Wish.objects.get(id=wish_id)
    to_delete.delete()
    return redirect('/wishes')

def grant_wish(request, wish_id):
    wish = Wish.objects.get(id=wish_id)
    wish.granted = True
    wish.save()
    return redirect('/wishes')

def like(request, wish_id):
    wish = Wish.objects.get(id=wish_id)
    user = User.objects.get(id=request.session['userid'])
    wish.users_who_liked.add(user)
    return redirect('/wishes')

def unlike(request, wish_id):
    wish = Wish.objects.get(id=wish_id)
    user = User.objects.get(id=request.session['userid'])
    wish.users_who_liked.remove(user)
    return redirect('/wishes')

def stats(request):
    context = {
    'user': User.objects.get(id=request.session['userid']),
    'wishes': Wish.objects.filter(creator=User.objects.get(id=request.session['userid'])).exclude(granted=True),
    'granted_wishes': Wish.objects.filter(creator=User.objects.get(id=request.session['userid']), granted=True),
    'total_granted_wishes': Wish.objects.filter(granted=True)
    }
    return render(request, 'stats.html', context)