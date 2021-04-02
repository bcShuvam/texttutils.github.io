from django.http import HttpResponse
from django.shortcuts import render

def index1(request):
    return HttpResponse('''<h1>Home 1 .</h1><br><a href="http://127.0.0.1:8000/removepunc">Next</a>''')

def removepunc(request):
    return HttpResponse('''<h1>Remove Punc 2 .</h1><br><a href="http://127.0.0.1:8000">Back</a> <a href="http://127.0.0.1:8000/capitalizefirst">Next</a>''')

def capfirst(request):
    return HttpResponse('''<h1>Capitalize First 3 .</h1><br><a href="http://127.0.0.1:8000/removepunc">Back</a> <a href="http://127.0.0.1:8000/newlineremove">Next</a>''')

def removenewline(request):
    return HttpResponse('''<h1>Remove New line 4 .</h1><br><a href="http://127.0.0.1:8000/capitalizefirst">Back</a> <a href="http://127.0.0.1:8000/spaceremover">Next</a>''')

def spaceremove(request):
    return HttpResponse('''<h1>Space Remove 5 .</h1><br><a href="http://127.0.0.1:8000/newlineremove">Back</a> <a href="http://127.0.0.1:8000/charcount">Next</a>''')

def charcount(request):
    return HttpResponse('''<h1>Count character 6 .</h1><br><a href="http://127.0.0.1:8000/spaceremover">Back</a>''')