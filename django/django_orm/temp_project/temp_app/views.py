from django.shortcuts import redirect, render, HttpResponse
from .models import *
# other imports
# show all of the data from a table
def index(request):
    context = {
    	"all_the_user": User.objects.all()
    }
    return render(request,'index.html',context)

def process(request):
    if request.method == 'POST':
        u=User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], age=request.POST['age'])
    return redirect('/')


