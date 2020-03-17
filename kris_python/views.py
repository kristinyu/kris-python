# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import HttpResponse
from django.shortcuts import render

# Create your views here.
def fun(request):
    return HttpResponse("ddddd")


def getRequest(request):
    request.encoding='utf-8'
    if 'q' in request.GET and request.GET['q']:
        mess='ur input param is'+request.GET['q']
    else:
        mess='input error'
    return HttpResponse(mess)

def postRequest(request):
    ctx={}
    if request.POST:
        ctx['rtx'] = request.POST['a']
        mess = "ur post request params are"+ctx
    else:
        mess = 'ur post error accure'
    return render(request,ctx)

