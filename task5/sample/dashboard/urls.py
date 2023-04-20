from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('admin_home', views.admin_home, name='admin_home'),
    path('admin_login', views.admin_login, name='admin_login'),
    path('add_user', views.add_user, name='add_user'),
    path('update_user/<int:id>', views.update_user, name='update_user'),
    path('delete_user/<int:id>',views.delete_user,name='delete_user'),
    path('search',views.search,name='search'),
]
