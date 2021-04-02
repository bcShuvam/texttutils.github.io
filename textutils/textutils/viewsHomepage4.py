from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

    # return HttpResponse("Home")



def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount','off')
    print(djtext)

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change to Uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != '\n' and char!='\r':
                analyzed = analyzed + char
        params = {'purpose':'Remove Newlines','analyzed_text':analyzed}
        return render(request,'analyze.html',params)

    elif extraspaceremover == "on":
        analyzed = ""
        for index , char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose':'Remove Newlines','analyzed_text':analyzed}
        return render(request,'analyze.html',params)

    elif charcount == "on":
        analyzed = len(djtext)
        params = {'purpose':'Character counter','analyzed_text':analyzed}
        return render(request,'analyze.html',params)

    else:
        return HttpResponse("Error")

# def capfirst(request):
#     pass
#
# def removenewline(request):
#     pass
#
# def spaceremove(request):
#     pass
#
# def charcount(request):
#     pass