from django.http import HttpResponse

def facebook_url(request):
    return HttpResponse('''<h1>Facebook</h1><a href="https://www.facebook.com/" style="text-decoration:none;">Login Page</a>''')