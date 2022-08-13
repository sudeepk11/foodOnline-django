from django.contrib import admin
from .models import FoodItem,Category 
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    list_display = ('category_name','vendor','updated_at')
    search_fields = ('category_name','vendor__vendor_name')


class FoodItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('food_title',)}
    list_display = ('food_title','category','is_available','price' ,'updated_at')
    search_fields = ('category__category_name', 'food_title', 'vendor__vendor_name','price')
    list_filter = ('is_available',)




admin.site.register(FoodItem, FoodItemAdmin)
admin.site.register(Category, CategoryAdmin)