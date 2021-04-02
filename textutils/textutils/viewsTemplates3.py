from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {
        'name':'harry',
        'planet':'Mars'
    }
    return render(request,'index.html',params)