from django.urls import path
from .views import dashboard
from .views import *
urlpatterns = [
    path('', dashboard, name='dashboard'),
   
    
]