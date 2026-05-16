from django.urls import path
from .views import *

urlpatterns = [

    path('customers/', customers, name='customers'),
    path('calls/', calls, name='calls'),
    path('targets/', targets, name='targets'),

]