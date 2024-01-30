from django.shortcuts import render
from celeproj.celery import add
from myapp.tasks import sub
from celery.result import AsyncResult

def index(request):
    print("Results")
    result = add.delay(10, 20)
    print("Result -> ", result)
    #resultt2 = sub.apply_async(args=[70, 20])
    #print("Result -> ", resultt2)
    return render(request, "myapp/home.html", {"result":result})

def check_result(request, task_id):
    result = AsyncResult(task_id)
    return render(request, "myapp/check_result.html", {"result":result})

def contact(request):
    return render(request, "myapp/contact.html")

def about(request):
    return render(request, "myapp/about.html")