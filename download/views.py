from django.shortcuts import render
from django.views import View

from upload.models import Document

class DownloadView(View):
    def get(self, request):
        docs = Document.objects.all()
        context = {
            'docs': docs
        }
        return render(request, 'download/download.html')

    def post(self, request):
        docs = Document.objects.all()
        context = {
            'docs': docs
        }
        return render(request, 'download/download.html')