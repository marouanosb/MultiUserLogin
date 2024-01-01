from django.contrib import admin
from .models import User, Cours, Rapport
from django.contrib.auth.admin import UserAdmin


# Register your models here.
admin.site.register(User)
admin.site.register(Cours)
admin.site.register(Rapport)    

####    FIX PASSWORD NOT HASHING IN DJANGO ADMIN admin.site.register(User, UserAdmin)