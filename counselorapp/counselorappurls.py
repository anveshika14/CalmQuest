from django.urls import path
from . import views
urlpatterns=[
    path("",views.counselorhome,name='counselorhome'),
    path("csignout",views.csignout,name='csignout'),
    path("cprofile",views.cprofile,name='cprofile'),
    path("uploaddetails",views.uploaddetails,name='uploaddetails'),
]