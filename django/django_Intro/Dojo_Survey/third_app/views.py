from django.shortcuts import redirect, render, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def check_credantial(username):
    if username == "khalil":
        return True
    return False


def show(request):
    if request.method == "POST":
        name= request.POST['username']
        Location=request.POST['Location']
        Language=request.POST['Language']
        area=request.POST['area']
    if check_credantial(name):
            return redirect('result/')
    return redirect('/')
    
def success(request):
    return render('show.html')



