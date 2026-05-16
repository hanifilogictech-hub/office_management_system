from django.shortcuts import render

# Create your views here.


def employee_list(request):
    return render(request,'employees/employee_list.html')


def attendance(request):
    return render(request,'employees/attendance.html')


def leave_requests(request):
    return render(request,'employees/leave_requests.html')


def skills(request):
    return render(request,'employees/skills.html')


def performance(request):
    return render(request,'employees/performance.html')


def salary(request):
    return render(request,'employees/salary.html')