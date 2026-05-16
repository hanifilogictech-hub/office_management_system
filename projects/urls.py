from django.urls import path
from .views import *

urlpatterns = [

    path('projects/', projects, name='projects'),
    path('timeline/', timeline, name='timeline'),
    path('tasks/', tasks, name='tasks'),

]