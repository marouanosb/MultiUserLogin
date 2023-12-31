from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin


# Register your models here.
admin.site.register(User)

####    FIX PASSWORD NOT HASHING admin.site.register(User, UserAdmin)