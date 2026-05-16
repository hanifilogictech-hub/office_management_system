from django.shortcuts import render

# Create your views here.


def projects(request):
    return render(request,'projects/projects.html')

def timeline(request):
    return render(request,'projects/timeline.html')

def tasks(request):
    return render(request,'projects/tasks.html')