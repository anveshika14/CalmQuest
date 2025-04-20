from django.urls import path
from . import views

urlpatterns=[
path('',views.index,name='index'),
path('new1',views.new1,name='new1'),
path('contactus',views.contactus,name='contactus'),
path('register',views.register,name='register'),
path('depress',views.depress,name='depress'),
path('login',views.login,name='login'),
path('aboutus',views.aboutus,name='aboutus'),
path('services',views.services,name='services'),
path('clogin',views.clogin,name='clogin'),
path('cregister',views.cregister,name='cregister'),
path('greport',views.greport,name='greport'),
path('anx',views.anx,name='anx'),
path('dep',views.dep,name='dep'),
path('adhorder',views.adhorder,name='adhorder'),
path('result',views.result,name='result'),
path('newdep',views.newdep,name='newdep'),
]