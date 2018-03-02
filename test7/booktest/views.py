from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def setsession(request):
    request.session['name'] = 'zhangsan'

    return HttpResponse('ok')


def getsession(request):
    name = request.session['name']
    return HttpResponse(name)
