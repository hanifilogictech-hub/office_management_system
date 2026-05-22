from django.shortcuts import render, redirect, get_object_or_404
from django.db import IntegrityError
from .models import Employee

def employee_list(request):
    employees = Employee.objects.all() 
    return render(request, 'employees/employee_list.html', {'employees': employees})

from django.shortcuts import render, redirect
from django.db import IntegrityError  # <--- Essential: This must be present
from .models import Employee

def add_employee(request):
    if request.method == 'POST':
        try:
            Employee.objects.create(
                employee_id=request.POST.get('empId'),
                name=request.POST.get('empName'),
                department=request.POST.get('empDept'),
                role=request.POST.get('empRole'),
                role_type=request.POST.get('roleType'),
                status=request.POST.get('status') # This grabs the value from the <select>
            )
            return redirect('employees_list')
        except IntegrityError:
            return render(request, 'employees/add_employee.html', {
                'error': 'Error: This Employee ID already exists.'
            })
            
    return render(request, 'employees/add_employee.html')

def edit_employee(request, emp_id):
    employee = get_object_or_404(Employee, pk=emp_id)
    
    if request.method == 'POST':
        employee.employee_id = request.POST.get('empId')
        employee.name = request.POST.get('empName')
        employee.department = request.POST.get('empDept')
        employee.role = request.POST.get('empRole')
        employee.role_type = request.POST.get('roleType')
        employee.status = request.POST.get('status')
        employee.save()
        return redirect('employees_list')
        
    return render(request, 'employees/edit_employee.html', {'employee': employee})

def delete_employee(request, emp_id):
    employee = get_object_or_404(Employee, pk=emp_id)
    if request.method == 'POST':
        employee.delete()
    return redirect('employees_list')
def attendance(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
        # Get the employee instance
        employee = Employee.objects.get(employee_id=employee_id)
        # Save attendance
        Attendance.objects.create(
            employee=employee,
            date=timezone.now().date(),
            check_in=timezone.now().time(),
            status='Present'
        )
        return redirect('attendance')

    # This part populates your dropdown
    employees = Employee.objects.all()
    # This part populates your table
    attendance_records = Attendance.objects.filter(date=timezone.now().date())
    
    return render(request, 'employees/attendance.html', {
        'employees': employees,
        'attendance_records': attendance_records
    })

# Helper Views
def attendance(request): return render(request, 'employees/attendance.html')
def leave_requests(request): return render(request, 'employees/leave_requests.html')
def skills(request): return render(request, 'employees/skills.html')
def performance(request): return render(request, 'employees/performance.html')
def salary(request): return render(request, 'employees/salary.html')