# from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    # return HttpResponse("Hello world")
    langu = "framework"
    return render(request, "index.html", {'lang_key': langu})  # passing a value using dictionary ie key value pair


def addition(request):
    number1 = int(request.GET['num1'])
    number2 = int(request.GET['num2'])
    result = number1 + number2
    return render(request, "result.html", {'result': result})  # pass dictionary( key value pair)


def about(request):
    return render(request, "about.html")


def contact(request):
    return httpResponse("Contact Details Here")
