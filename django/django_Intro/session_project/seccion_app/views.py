from django.http import request
from django.shortcuts import redirect, render

# Create your views here.
def index(request):
    if 'name' in request.session:
        return redirect('/welcome')
    return render(request, 'index.html')

def check_user(username,password):
    #user = model.check_user(username, password)
    if username=="bara" and password== "bara123":
        return "Baraa Salameh"
    return None

def create_user(username,password,con_password,gender):
    
    #varify the user is not already in the DB
    #create the user and save in DB
    #user = model.check_user(username, password)
    return "Hani Khmaiss"

def chechk_user(username,password):
    if username=="bara" and password== "bara123":
        return "Baraa Salameh"
    return None

def welcome(request):
    return render(request, 'welcome.html')

def login(request):
    if request.method == "GET" :
        if request.POST['form_type'] == 'login':
            username=request.POST['username']
            password=request.POST['password']
            user_info= check_user(username, password)
            if user_info is not None:
                request.session['name']= user_info
                request.session['type']="log in"
                return redirect('/welcome')
        
        elif request.POST['form_type']== 'register':
            username=request.POST['username']
            password=request.POST['password']
            con_password=request.POST['Confirmpassword']
            gender=request.POST['gender']
            user_info= create_user(username,password,con_password,gender)
            request.session['name']=user_info
            request.session['type']="register"
            request.session['gender']= gender
            return redirect('/welcome')
        return redirect('/')

def logout(request):
    # del request.session['name']
    request.session.clear()
    return redirect('/')