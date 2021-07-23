from django.shortcuts import render, redirect
# Create your views here.

def index(request):
    return render(request, 'form.html')

def submit_survey(request):
    request.session["full_name"] = request.POST["full_name"]
    request.session["dojo_location"] = request.POST["dojo_location"]
    request.session["fav_language"] = request.POST["fav_language"]
    request.session["comment_area"] = request.POST["comment_area"]
    return redirect("/result")

def result(request):
    return render(request, 'result_form.html')

def reset(request):
    request.session.flush()
    return redirect("/")

