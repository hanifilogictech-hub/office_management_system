from django.shortcuts import render

# Create your views here.



def daily_worksheet(request):
    return render(request,'workmanagement/daily_worksheet.html')


def assigned_tasks(request):
    return render(request,'workmanagement/assigned_tasks.html')


def work_reports(request):
    return render(request,'workmanagement/work_reports.html')