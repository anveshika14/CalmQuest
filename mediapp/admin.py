from django.contrib import admin
from . models import Register,Login,Contactus,Newsletter
# Register your models here.
admin.site.register(Register)
admin.site.register(Login)
admin.site.register(Contactus)
admin.site.register(Newsletter)
