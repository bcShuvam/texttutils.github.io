# I have created this file

from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Hello Shuvam !</h1>")

def about(request):
    f = open('textutils/Paragraphs.txt','rt')
    data = f.read()
    return HttpResponse(f"<b>{data}</b>")