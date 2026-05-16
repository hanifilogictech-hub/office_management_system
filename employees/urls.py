from django.urls import path
from .views import *

urlpatterns = [

    path('employee-list/', employee_list, name='employees_list'),
    path('attendance/', attendance, name='attendance'),
    path('leave/', leave_requests, name='leave_requests'),
    path('skills/', skills, name='skills'),
    path('performance/', performance, name='performance'),
    path('salary/', salary, name='salary'),

]