from django import views
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from accounts import views as AccountViews
urlpatterns = [
  path('' , AccountViews.vendorDashboard),
  path('profile/',views.vprofile, name = 'vprofile'),
  path('menu-builder/', views.menu_builder, name = 'menu_builder'),
  path('menu-builder/category/<int:pk>/',views.fooditems_by_category, name = 'fooditems_by_category'),

  # CRUD PATHS
  
  path('menu-builder/category/add/',views.add_category, name = 'add_category')
]
