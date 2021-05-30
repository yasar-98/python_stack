from typing import ContextManager
from django.db.models.expressions import Ref
from django.shortcuts import render, HttpResponse , redirect
from django.http import JsonResponse
from . import models
import bcrypt
from django.contrib import messages


def index(request):
    if 'id' in request.session:
        return redirect('/books')

    return render(request,"index.html")

def books(request):
    context={
        'all_users':models.User.objects.all(),
        'user': models.User.objects.get(id=request.session['id']),
        'all_books': models.Book.objects.all()
    }
    return render(request,'favourite_books.html',context)
    

def register(request):
    errors = models.User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        if request.method == "POST":
            first_name=request.POST["first_name"]
            last_name=request.POST["last_name"]
            email=request.POST["email"]
            passwd=request.POST["passwd"]
            pw_hash = bcrypt.hashpw(passwd.encode(), bcrypt.gensalt()).decode()  # create the hash    
            conpasswd=request.POST["conpasswd"]
            if passwd==conpasswd:
                user=models.create_user(first_name,last_name,email,pw_hash)
                request.session['id']=user.id
                request.session['first_name']=user.first_name
                request.session['last_name']=user.last_name
                return redirect('/books')

def logout(request):
    request.session.clear()
    return redirect('/')

def login(request):
    if request.method == "POST":
        email=request.POST["email"]
        passwd=request.POST["passwd"]
        user = models.get_user(email)
        if user and bcrypt.checkpw(passwd.encode(), user.passwd.encode()):
            request.session['id']=user.id
            request.session['first_name']=user.first_name
            request.session['last_name']=user.last_name
            return redirect('/books')
        return redirect('/')

def booking(request):
    if 'id' in request.session:
        user=models.User.objects.get(id=request.session['id'])
        this_book=models.Book.objects.create(title=request.POST['title'],desc=request.POST['desc'],uploader=user)
        user.books.add(this_book)
        return redirect('/books')

    return render(request,"index.html")

def add_favourite(request,num):   
    user=models.User.objects.get(id=request.session['id'])
    this_book=models.Book.objects.get(id=num)
    user.books.add(this_book)
    return redirect('/books')

def going(request,num):
    user=models.User.objects.get(id=request.session['id'])
    book=models.Book.objects.get(id=num)
    context={
            'all_users':models.User.objects.all(),
            'user': user,
            'book': book,
            'all_books': models.Book.objects.all()
        }
    if book.uploader.id == user.id:
        return render(request,"upload.html", context)
    else:
        return render(request,"detail.html", context)

def event(request,num):
    if request.method == 'POST':
        if 'update' in request.POST:
            c=models.Book.objects.get(id=num)
            c.title=request.POST['title']
            c.desc=request.POST['desc']
            c.save()
            return redirect(f'/books/{num}')

        if 'delete' in request.POST:
            c=models.Book.objects.get(id=num)
            c.delete()
            return redirect(f'/books')

def unfav(request,num):
    user=models.User.objects.get(id=request.session['id'])
    book=models.Book.objects.get(id=num)
    user.books.remove(book)
    return redirect('/books')