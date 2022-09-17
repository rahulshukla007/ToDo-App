from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('dashboard/', views.dashboard, name='Dashboard'),
    path('add/', views.addItem, name='AddItem'),
    path('del/<int:id>', views.delete, name='Delete'),
    path('signout/', views.signout, name='Signout')
    
]
