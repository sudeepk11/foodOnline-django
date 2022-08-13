from django.contrib import admin

# Register your models here.
from .models import User, UserProfile
from django.contrib.auth.admin import UserAdmin
from menu.models import FoodItem , Category

class CustomUserAdmin(UserAdmin):
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
  

admin.site.register(User,CustomUserAdmin)
admin.site.register(UserProfile)


