from django.urls import path
from .views import *

urlpatterns = [

    path('intern-list/', intern_list, name='intern_list'),
    path('syllabus/', syllabus, name='syllabus'),
    path('certification/', certification, name='certification'),

]