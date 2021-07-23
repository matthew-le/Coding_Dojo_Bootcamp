from django.shortcuts import render, redirect
from .models import Show
from django.contrib import messages

# Create your views here.
def update_show(request, show_id):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/{show_id}/edit')
    else: 
        show = Show.objects.get(id=show_id)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['release_date']
        show.desc = request.POST['desc']
        show.save()
        # messages.success(request, "Show successfully updated")

        return redirect('/shows')

def index(request):
    return redirect('/shows')

def show(request):
    context = {
        'shows': Show.objects.all()
    }

    return render(request, 'shows.html', context)

def add_show(request):
    return render(request, 'add_show.html')

def create_show(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new')
    elif request.method == "POST":
        Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date= request.POST['release_date'], desc=request.POST['desc'])
    return redirect('/shows')

def show_info(request, show_id):
    show_info = Show.objects.get(id=show_id)
    context = {
        'show': show_info
    }
    return render(request, 'show_info.html', context)

def edit_show(request, show_id):
    one_show = Show.objects.get(id=show_id)
    context = {
        'show': one_show
    }
    return render(request, 'edit_show.html', context)

def delete_show(request, show_id):
    to_delete = Show.objects.get(id=show_id)
    to_delete.delete()
    return redirect('/shows')


