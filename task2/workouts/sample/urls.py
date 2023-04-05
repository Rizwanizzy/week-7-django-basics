from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('card_list', views.card_list, name='card_list'),
    path('table_list', views.table_list, name='table_list')
]
