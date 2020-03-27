from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from upload.models import Document

@login_required()
def download_view(request):
    docs = Document.objects.all()
    context = {
    'docs': docs
    }
    return render(request, 'download/download.html', context=context)