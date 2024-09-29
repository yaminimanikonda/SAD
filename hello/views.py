from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from django.shortcuts import render

def hello_world_json(request):
    return JsonResponse({"Message": "Hello World!"})

def hello_world_html(request):
    return render(request, 'hello/hello.html')

