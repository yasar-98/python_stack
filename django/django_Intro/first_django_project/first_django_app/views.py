from django.db.models.expressions import Ref
from django.shortcuts import render, HttpResponse , redirect
from django.http import JsonResponse
from . import models


def index(request):
    return render(request,"index.html")

def welcome(request):
    if 'id' in request.session:
        context={
            'cars':models.get_users_cars(request.session['id'])
        }
        return render(request,'welcome.html', context)
    else:
        return redirect('/')

def register(request):
    if request.method == "POST":
        first_name=request.POST["first_name"]
        last_name=request.POST["last_name"]
        email=request.POST["email"]
        passwd=request.POST["passwd"]
        conpasswd=request.POST["conpasswd"]
        if passwd==conpasswd:
            user=models.create_user(first_name,last_name,email,passwd)
            request.session['id']=user.id
            request.session['first_name']=user.first_name
            request.session['last_name']=user.last_name
            return redirect('/welcome')
        return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')

def login(request):
    if request.method == "POST":
        email=request.POST["email"]
        passwd=request.POST["passwd"]
        user = models.get_user(email,passwd)
        if user:
            request.session['id']=user.id
            request.session['first_name']=user.first_name
            request.session['last_name']=user.last_name
            return redirect('/welcome')
        return redirect('/')
