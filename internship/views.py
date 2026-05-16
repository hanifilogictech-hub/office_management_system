from django.shortcuts import render

# Create your views here.

def intern_list(request):
    return render(request,'internship/intern_list.html')

def syllabus(request):
    return render(request,'internship/syllabus.html')

def certification(request):
    return render(request,'internship/certification.html')