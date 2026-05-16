from django.urls import path
from .views import *

urlpatterns = [

    path('daily-worksheet/',daily_worksheet,name='daily_worksheet'),

    path('assigned-tasks/',assigned_tasks,name='assigned_tasks'),

    path('reports/',work_reports,name='work_reports'),

]