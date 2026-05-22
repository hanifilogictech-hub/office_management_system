from django.urls import path
from . import views

urlpatterns = [
    path('employee-list/', views.employee_list, name='employees_list'),
    path('add-employee/', views.add_employee, name='add_employee'),
    path('edit-employee/<int:emp_id>/', views.edit_employee, name='edit_employee'),
    path('delete-employee/<int:emp_id>/', views.delete_employee, name='delete_employee'),
    path('attendance/', views.attendance, name='attendance'),
    path('leave/', views.leave_requests, name='leave_requests'),
    path('skills/', views.skills, name='skills'),
    path('performance/', views.performance, name='performance'),
    path('salary/', views.salary, name='salary'),
]