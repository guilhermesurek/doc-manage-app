from django.shortcuts import render
from django.http import HttpResponse

def download_view(request):
    return HttpResponse('Download View')