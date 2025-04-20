from django.shortcuts import render,redirect,reverse
from .models import Register,Login,Contactus,Newsletter,Clogin,Cregister,Anxtest
from django.contrib import messages
from datetime import date
# Create your views here.
def index(request):
    if request.method=="POST":
        news=request.POST['news']
        regdate=date.today()
        news=Newsletter(news=news,regdate=regdate)
        news.save()
    return render(request,"index.html")
def new1(request):
    
    return render(request,"new1.html",locals())
def contactus(request):
    if request.method=="POST":
        name=request.POST['name']
        phoneno=request.POST['phoneno']
        email=request.POST['email']
        enquirytext=request.POST['enquirytext']
        enquirydate=date.today()
        con=Contactus(name=name,phoneno=phoneno,enquirytext=enquirytext,enquirydate=enquirydate,email=email)
        con.save()
    return render(request,"contactus.html",locals())
def register(request):
    if request.method=="POST":
        logname=request.POST['logname']
        logemail=request.POST['logemail']
        logpass=request.POST['logpass']
        regdate=date.today()
        usertype='client'
        status='false'
        reg=Register(logname=logname,logemail=logemail,regdate=regdate)
        reg.save()
        log=Login(userid=logemail,logpass=logpass,usertype=usertype,status=status)
        log.save()
        messages.success(request,'Registration Successfully !!!')
    return render(request,"register.html",locals())
def login(request):
    if request.method=="POST":
        userid=request.POST['userid']
        logpass=request.POST['logpass']
        try:
            obj=Login.objects.get(userid=userid,logpass=logpass)
            if obj.usertype=='client':
                request.session['logemail']=userid
                return redirect(reverse('clientapp:clienthome'))
            elif obj.usertype=='admin':
                request.session['adminid']=userid
                return redirect(reverse('adminapp:adminhome'))
        except:
            messages.error(request,'Invalid user !!!')
        
    return render(request,"login.html",locals()) 

def clogin(request):
    if request.method=="POST":
        userid=request.POST['userid']
        psw=request.POST['psw']
        print(userid,psw)
        try:
            print('yes')
            obj=Clogin.objects.get(userid=userid,psw=psw)
            
            if obj.usertype=="counselor":
                request.session['username']=userid
                return redirect(reverse('counselorapp:counselorhome'))
            else:
                print('else2')
                request.session['adminid']=userid
                return redirect(reverse('adminapp:adminhome'))
        except:

            messages.error(request,'Invalid user !!!')
    return render(request,"clogin.html",locals())

def cregister(request):
    if request.method=="POST":
        username=request.POST['username']
        phoneno=request.POST['phoneno']
        address=request.POST['address']
        email=request.POST['email']
        highedu=request.POST['highedu']
        special=request.POST['special']
        work=request.POST['work']
        preorg=request.POST['preorg']
        psw=request.POST['psw']
        conpsw=request.POST['conpsw']
        regdate=date.today()
        usertype='counselor'
        status='false'
        creg=Cregister(username=username,phoneno=phoneno,address=address,email=email,highedu=highedu,special=special,work=work,preorg=preorg,regdate=regdate)
        creg.save()
        clog=Clogin(userid=username,psw=psw,usertype=usertype,status=status)
        clog.save()
        messages.success(request,'Registration Successfully !!!')
    return render(request,"cregister.html",locals())

def depress(request):
    return render(request,"depress.html")
def aboutus(request):
    return render(request,"aboutus.html",locals())
def services(request):
    return render(request,"services.html",locals())
def greport(request):
    return render(request,"greport.html",locals())
from django.shortcuts import render,redirect,reverse
from .models import Register,Login,Contactus,Newsletter,Clogin,Cregister
from django.contrib import messages
from datetime import date
# Create your views here.
def index(request):
    if request.method=="POST":
        news=request.POST['news']
        regdate=date.today()
        news=Newsletter(news=news,regdate=regdate)
        news.save()
    return render(request,"index.html")
def new1(request):
    
    return render(request,"new1.html",locals())
def contactus(request):
    if request.method=="POST":
        name=request.POST['name']
        phoneno=request.POST['phoneno']
        email=request.POST['email']
        enquirytext=request.POST['enquirytext']
        enquirydate=date.today()
        con=Contactus(name=name,phoneno=phoneno,enquirytext=enquirytext,enquirydate=enquirydate,email=email)
        con.save()
    return render(request,"contactus.html",locals())
def register(request):
    if request.method=="POST":
        logname=request.POST['logname']
        logemail=request.POST['logemail']
        logpass=request.POST['logpass']
        regdate=date.today()
        usertype='client'
        status='false'
        reg=Register(logname=logname,logemail=logemail,regdate=regdate)
        reg.save()
        log=Login(userid=logemail,logpass=logpass,usertype=usertype,status=status)
        log.save()
        messages.success(request,'Registration Successfully !!!')
    return render(request,"register.html",locals())
def login(request):
    if request.method=="POST":
        userid=request.POST['userid']
        logpass=request.POST['logpass']
        try:
            obj=Login.objects.get(userid=userid,logpass=logpass)
            if obj.usertype=='client':
                request.session['logemail']=userid
                return redirect(reverse('clientapp:clienthome'))
            elif obj.usertype=='admin':
                request.session['adminid']=userid
                return redirect(reverse('adminapp:adminhome'))
        except:
            messages.error(request,'Invalid user !!!')
        
    return render(request,"login.html",locals()) 

def clogin(request):
    if request.method=="POST":
        userid=request.POST['userid']
        psw=request.POST['psw']
        print(userid,psw)
        try:
            print('yes')
            obj=Clogin.objects.get(userid=userid,psw=psw)
            
            if obj.usertype=="counselor":
                request.session['username']=userid
                return redirect(reverse('counselorapp:counselorhome'))
            else:
                print('else2')
                request.session['adminid']=userid
                return redirect(reverse('adminapp:adminhome'))
        except:

            messages.error(request,'Invalid user !!!')
    return render(request,"clogin.html",locals())

def cregister(request):
    if request.method=="POST":
        username=request.POST['username']
        phoneno=request.POST['phoneno']
        address=request.POST['address']
        email=request.POST['email']
        highedu=request.POST['highedu']
        special=request.POST['special']
        work=request.POST['work']
        preorg=request.POST['preorg']
        psw=request.POST['psw']
        conpsw=request.POST['conpsw']
        regdate=date.today()
        usertype='counselor'
        status='false'
        creg=Cregister(username=username,phoneno=phoneno,address=address,email=email,highedu=highedu,special=special,work=work,preorg=preorg,regdate=regdate)
        creg.save()
        clog=Clogin(userid=username,psw=psw,usertype=usertype,status=status)
        clog.save()
        messages.success(request,'Registration Successfully !!!')
    return render(request,"cregister.html",locals())

def depress(request):
    return render(request,"depress.html")
def aboutus(request):
    return render(request,"aboutus.html",locals())
def services(request):
    return render(request,"services.html",locals())
def greport(request):
    return render(request,"greport.html",locals())
def anx(request):
    if request.method=="POST":
        quesa=request.POST['question1']
        quesb=request.POST['question2']
        quesc=request.POST['question3']
        quesd=request.POST['question4']
        quese=request.POST['question5']
        quesf=request.POST['question6']
        ans = [quesa,quesb,quesc,quesd,quese,quesf]
        level = 0
        for i in ans:
            if i =='Yes': 
                level=level+1
        print(level)        
        if level<=2:
            msg = "Negative Result"
        else:
            msg = "Positive Result"       

        anx=Anxtest(question1=quesa,question2=quesb,question3=quesc,question4=quesd,question5=quese,question6=quesf)
        anx.save()
        messages.success(request,'submit Successfully !!!')
        return render(request,'result.html',locals())
    return render(request,"anx.html",locals())
def dep(request):
    return render(request,"dep.html",locals())
def adhorder(request):
    return render(request,"adhorder.html",locals())
def result(request):
    return render(request,"result.html",locals())

def newdep(request):
    return render(request,"newdep.html",locals())
