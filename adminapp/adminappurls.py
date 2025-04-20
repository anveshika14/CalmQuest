from django.urls import path
from . import views

urlpatterns=[
  path('adminhome/',views.adminhome,name='adminhome'),
  path('clientcontact/',views.clientcontact,name='clientcontact'),
  path('clientdetails/',views.clientdetails,name='clientdetails'),
  path('uploadtest/',views.uploadtest,name='uploadtest'),
  path('counselor/',views.counselor,name='counselor'),
]
