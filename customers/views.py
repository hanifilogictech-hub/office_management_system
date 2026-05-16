from django.shortcuts import render

# Create your views here.


def customers(request):
    return render(request,'customers/customers.html')

def calls(request):
    return render(request,'customers/calls.html')

def targets(request):
    return render(request,'customers/targets.html')