from django.shortcuts import render
from django.http import HttpResponse

def upload_view(request):
    return HttpResponse('Upload View')