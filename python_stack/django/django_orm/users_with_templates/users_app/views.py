from django.shortcuts import render, redirect
from .models import User

# Create your views here.

def index(request):
    context = {
        'users': User.objects.all()
    }
    return render (request, "index.html", context)


def create_user(request): 
    if (request.method == "POST"):
        print("This is a post method")
    User.objects.create(first_name = request.POST['first_name'], last_name= request.POST['last_name'], email_address = request.POST['email_address'], age = request.POST['age'])
    return redirect("/")

