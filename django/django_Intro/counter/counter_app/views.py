from django.shortcuts import render,HttpResponse,redirect

def index(request):

    if 'vcount' not in request.session:
        request.session['vcount']=1
    else:
        request.session['vcount']+=1

    if 'count' not in request.session:
        request.session['count']=1
    else:
        request.session['count']+=1
    return render(request,'index.html')

def destroy(request):
    request.session.clear()
    return redirect('/')

def increment(request):
    request.session['count']+=1
    request.session['vcount']-=1
    
    return redirect('/')

def increm(request):
    request.session['count']+=int(request.POST['increm'])-1
    request.session['vcount']-=1
    
    return redirect('/')