from django.shortcuts import render, HttpResponse, redirect
import random
from time import gmtime, strftime


def index(request):
    return render(request,'index.html')


def process(request):
    if request.method == "POST":
        if request.POST['which_form']=='register1':
            request.session['gold']= random.randint(10,20)
            request.session['name']='farm'
        elif request.POST['which_form']=='register2':
            request.session['gold']= random.randint(5,10)
            request.session['name']='Cave'
        elif request.POST['which_form']=='register3':
            request.session['gold']= random.randint(2,5)
            request.session['name']='House'
        elif request.POST['which_form']=='register4':
            request.session['gold']= random.randint(0,50)

        request.session['time']= strftime("%Y-%m-%d %H:%M %p", gmtime())
        if 'area' in request.session:
            if request.POST['which_form'] != 'register4':
                request.session['area'] =request.session['area'] + "\n" +"earned"+" " + str(request.session['gold'])+ " from the" +" " + str(request.session['name']) + " ! " +str(request.session['time'])
            elif request.POST['which_form'] == 'register4':
                request.session['area'] = request.session['area'] + "\n" + "earned a casino and lost "+ " " + str(request.session['gold']) + " ..Ouch.. "+ str(request.session['time'])
        else:
            if request.POST['which_form'] != 'register4':
                request.session['area'] ="earned"+" " + str(request.session['gold'])+ " from the" +" " + str(request.session['name']) + " ! " +str(request.session['time'])
            elif request.POST['which_form'] == 'register4':
                request.session['area'] ="\n" + "earned a casino and lost "+ " " + str(request.session['gold']) + " ..Ouch.. "+ str(request.session['time'])
    return redirect('/')