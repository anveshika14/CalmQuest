from django.db import models

# Create your models here.
class Register(models.Model):
    logname=models.CharField(max_length=50)
    logemail=models.CharField(max_length=50,primary_key=True)
    regdate=models.CharField(max_length=10)
class Login(models.Model):
    userid=models.CharField(max_length=50,primary_key=True)
    logpass=models.CharField(max_length=30)
    usertype=models.CharField(max_length=20)
    status=models.CharField(max_length=6)
    
class Contactus(models.Model):
    name=models.CharField(max_length=50)
    phoneno=models.CharField(max_length=10)
    email=models.CharField(max_length=30)
    enquirytext=models.TextField()
    enquirydate=models.CharField(max_length=10)
class Newsletter(models.Model):
    news=models.CharField(max_length=30)
    regdate=models.CharField(max_length=10)

class Clogin(models.Model):
    userid=models.CharField(max_length=50,primary_key=True)
    psw=models.CharField(max_length=30)
    usertype=models.CharField(max_length=20)
    status=models.CharField(max_length=6)

class Cregister(models.Model):
    username=models.CharField(max_length=50,primary_key=True)
    phoneno=models.CharField(max_length=10)
    address=models.CharField(max_length=50)
    email=models.CharField(max_length=30)
    highedu=models.CharField(max_length=50)
    special=models.CharField(max_length=50)
    work=models.CharField(max_length=10)
    preorg=models.CharField(max_length=50)
    regdate=models.CharField(max_length=30)

class Anxtest(models.Model):
    question1=models.CharField(max_length=40)
    question2=models.CharField(max_length=50)
    question3=models.CharField(max_length=40)
    question4=models.CharField(max_length=40)
    question5=models.CharField(max_length=50)
    question6=models.CharField(max_length=40)

    
