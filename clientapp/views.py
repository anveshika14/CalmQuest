from django.shortcuts import render,redirect
from mediapp.models import Register,Login,Contactus
from counselorapp.models import Uploaddetails
from django.views.decorators.cache import cache_control
from django.contrib  import messages
from datetime import date
# Create your views here.
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def clienthome(request):
    try:
        if request.session['logemail']!=None:
            logemail=request.session['logemail']
            reg=Register.objects.get(logemail=logemail)
            return render(request,'clienthome.html',locals())
    except KeyError:
                return redirect('mediapp:login')
    
def clientsignout(request):
    try: 
        del request.session['email']
    except KeyError:
        return redirect('mediapp:index')
    return redirect('mediapp: index')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def clientprofile(request):
    try:
        if request.session['logemail']!=None:
            logemail=request.session['logemail']
            reg=Register.objects.all()
            return render(request,'clientprofile.html',locals())
    except KeyError:
        return redirect('mediapp:login')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def changepassword(request):
    try:
        if request.session['logemail']!=None:
            logemail=request.session['logemail']
            reg=Register.objects.get(logemail=logemail)
            if request.method=='POST':
                oldpasslog=request.POST['oldpasslog']
                newpasslog=request.POST['newpasslog']
                confirmpasslog=request.POST['confirmpasslog']
                if newpasslog!=confirmpasslog:
                    messages.error(request,'Newpassword and Confirmpassword are not matched')
                    return render(request,'changepassword.html',locals())
                try:
                    obj=Login.objects.get(userid=logemail,passlog=oldpasslog)
                    Login.objects.filter(userid=logemail).update(passlog=newpasslog)
                    return redirect('clientapp:clientsignout')
                except:
                    messages.error(request,'Oldpassword is not matched')
                    return render(request,'changepassword.html',locals())
            return render(request,'changepassword.html',locals())
    except KeyError:
        return redirect('mediapp:login')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def session(request):
    try:
        if request.session['logemail']!=None:
            logemail=request.session['logemail']
            reg=Register.objects.get(logemail=logemail)
            return render(request,'session.html',locals())
    except KeyError:
                return redirect('mediapp:login')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def aichat(request):
    try:
        if request.session['logemail']!=None:
            logemail=request.session['logemail']
            reg=Register.objects.get(logemail=logemail)
            return render(request,'aichat.html',locals())
    except KeyError:
                return redirect('mediapp:login') 

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def noti(request):
    try:
        if request.session['logemail']!=None:
            logemail=request.session['logemail']
            reg=Register.objects.get(logemail=logemail)
            return render(request,'noti.html',locals())
    except KeyError:
                return redirect('mediapp:login')        

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def help(request):
    try:
        if request.session['logemail']!=None:
            logemail=request.session['logemail']
            reg=Register.objects.get(logemail=logemail)
            return render(request,'help.html',locals())
    except KeyError:
                return redirect('mediapp:login')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def session1(request):
    try:
        if request.session['logemail']!=None:
            logemail=request.session['logemail']
            reg=Register.objects.get(logemail=logemail)
            detail = Uploaddetails.objects.all()
            return render(request,'session1.html',locals())
    except KeyError:
                return redirect('mediapp:login')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def book(request):
    try:
        if request.session['logemail']!=None:
            logemail=request.session['logemail']
            reg=Register.objects.get(logemail=logemail)
            return render(request,'book.html',locals())
    except KeyError:
                return redirect('mediapp:login')
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def mood(request):
    try:
        if request.session['logemail']!=None:
            logemail=request.session['logemail']
            reg=Register.objects.get(logemail=logemail)
            return render(request,'mood.html',locals())
    except KeyError:
                return redirect('mediapp:login')
    
@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def viewp(request):
    try:
        if request.session['logemail']!=None:
            logemail=request.session['logemail']
            reg=Register.objects.get(logemail=logemail)
            return render(request,'viewp.html',locals())
    except KeyError:
                return redirect('mediapp:login')    

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def thought(request):
    try:
        if request.session['logemail']!=None:
            logemail=request.session['logemail']
            reg=Register.objects.get(logemail=logemail)
            return render(request,'thought.html',locals())
    except KeyError:
                return redirect('mediapp:login')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def booksess(request):
    try:
        if request.session['logemail']!=None:
            logemail=request.session['logemail']
            reg=Register.objects.get(logemail=logemail)
            return render(request,'booksess.html',locals())
    except KeyError:
                return redirect('mediapp:login')