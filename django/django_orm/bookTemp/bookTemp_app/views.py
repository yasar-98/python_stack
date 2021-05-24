from django.shortcuts import render, HttpResponse,redirect
from .models import *

def index(request):
    context = {
        "all_the_books": Book.objects.all(),
    }
    return render(request, "index.html", context)

def index2(request):
    context = {
        "all_the_authors": Author.objects.all(),
    }
    return render(request, "index2.html", context)

def book(request):
    Book.objects.create(title=request.POST['title'],desc=request.POST['desc'])
    return redirect('/')

def books(request,num):
    h=Book.objects.get(id=num)
    context = {
        "book": h,
        "all_the_authors":Author.objects.all()
    }
    return render(request, "booking.html", context)

def booking(request,num):
    
    y=Author.objects.get(id=request.POST['author'])
    Book.objects.get(id=num).authors.add(y) 
    return redirect(f'/book/'+ str(num) +'')

def authorg(request):
    Author.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],note=request.POST['note'])
    return redirect('/author')

def authors(request,num):
    h=Author.objects.get(id=num)
    context = {
        "author": h,
        "all_the_books":Book.objects.all()
    }
    return render(request, "authoring.html", context)

def authoring(request,num):
    y=Book.objects.get(id=request.POST['book'])
    Author.objects.get(id=num).book.add(y) 
    return redirect(f'/author/'+ str(num) +'')