from django.shortcuts import redirect, render, HttpResponse
from .models import *
from time import strftime
from django.contrib import messages

def index(request):
    return redirect('/shows')

def shows(request):
    context = {
        'all_series': Series.objects.all()
    }
    return render(request,'shows.html',context)

def new(request):
    return render(request,'new.html')

def create(request):
    errors = Series.objects.basic_validator(request.POST)
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/shows/new')
    else:
        if request.method == 'POST':
            title=request.POST['title']
            network=request.POST['network']
            release_date=request.POST['release_date']
            desc=request.POST['desc']
            z=Series.objects.create(title=title,network=network,release_date=release_date)
            num=z.id
        return redirect(f'/shows/'+str(num)+'')

def nums(request,num):
    context = {
        'series': Series.objects.get(id = num)
    }
    return render(request,'nums.html',context)

def edit(request,num):
    context = {
        'series': Series.objects.get(id = num)
    }
    return render(request,'edit.html',context)

def update(request,num):
    errors = Series.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect(f'/shows/'+str(num)+'/edit')

    else:
        x=Series.objects.get(id = num)
        if x.title !=request.POST['title']:
            x.title= request.POST['title']
            x.save()
        if x.network !=request.POST['network']:
            x.network= request.POST['network']
            x.save()
            
        date=x.release_date
        new_date=date.strftime("%Y,%m,%d")  
        if new_date !=request.POST['release_date']:
            x.release_date= request.POST['release_date']
            x.save()
        if x.desc !=request.POST['desc']:
            x.desc= request.POST['desc']
            x.save()        
        return redirect(f'/shows/'+str(num)+'')



def destroy(request,num):
    x=Series.objects.get(id = num)
    x.delete()
    return redirect('/shows')

