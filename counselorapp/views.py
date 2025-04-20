from django.shortcuts import render,redirect
from django.views.decorators.cache import cache_control
from mediapp.models import Cregister,Clogin
from django.contrib  import messages
from datetime import date
from . models import Uploaddetails
# Create your views here.

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def counselorhome(request):
    try:
        if request.session['username']!=None:
            username=request.session['username']
            # reg=Register.objects.get(username=username)
            return render(request,'counselorhome.html',locals())
    except KeyError:
                return redirect('mediapp:index')

def csignout(request):
    try: 
        del request.session['username']
    except KeyError:
        return redirect('mediapp:index')
    return redirect('mediapp:services')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def cprofile(request):
    try:
        if request.session['username']!=None:
            username=request.session['username']
            creg=Cregister.objects.get(username=username)
            # reg=Register.objects.get(username=username)
            return render(request,'cprofile.html',locals())
    except KeyError:
                return redirect('mediapp:index')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def uploaddetails(request):
    try:
        if request.session['username']!=None:
            username=request.session['username']
            if request.method=='POST':
                myfile=request.FILES['myfile']
                name=request.POST['name']
                edu=request.POST['edu']
                spec=request.POST['spec']
                date=request.POST['date']
                time=request.POST['time']
                load=Uploaddetails(myfile=myfile,name=name,edu=edu,spec=spec,date=date,time=time)
                load.save()
            return render(request,'uploaddetails.html',locals())
    except KeyError:
                return redirect('mediapp:index')