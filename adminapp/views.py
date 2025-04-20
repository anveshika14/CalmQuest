from django.shortcuts import render,redirect
from django.views.decorators.cache import cache_control
from mediapp.models import Register,Login,Contactus,Clogin,Cregister
from datetime import date
from django.contrib import messages
# Create your views here.
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def adminhome(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            return render(request,'adminhome.html',locals())
    except KeyError:
        return redirect('mediapp:login')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def clientcontact(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            con=Contactus.objects.all()
            return render(request,'clientcontact.html',locals())
    except KeyError:
        return redirect('mediapp:login')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def clientdetails(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            reg=Register.objects.all()
            return render(request,'clientdetails.html',locals())
    except KeyError:
        return redirect('mediapp:login')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def uploadtest(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            return render(request,'uploadtest.html',locals())
    except KeyError:
        return redirect('mediapp:login')

def counselor(request):
    try:
        if request.session['adminid']!=None:
            adminid=request.session['adminid']
            creg = Cregister.objects.all()
            return render(request,'counselor.html',locals())
    except KeyError:
        return redirect('mediapp:login')