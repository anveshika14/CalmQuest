from django.urls import path
from . import views
urlpatterns=[
    
    path('clienthome/',views.clienthome,name='clienthome'),
    path('clientsignout/',views.clientsignout,name='clientsignout'),
    path('clientprofile/',views.clientprofile,name='clientprofile'),
    path('changepassword/',views.changepassword,name='changepassword'),
    path('session/',views.session,name='session'),
    path('noti/',views.noti,name='noti'),
    path('aichat/',views.aichat,name='aichat'),
    path('help/',views.help,name='help'),
    path('session1/',views.session1,name='session1'),
    path('book/',views.book,name='book'),
    path('mood/',views.mood,name='mood'),
    path('viewp/',views.viewp,name='viewp'),
    path('thought/',views.thought,name='thought'),
    path('booksess/',views.booksess,name='booksess'),
    ]