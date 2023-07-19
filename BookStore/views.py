from django.shortcuts import render, HttpResponse

# Create your views here.
def sayhello(request):
    return HttpResponse('Hello Ashish')
