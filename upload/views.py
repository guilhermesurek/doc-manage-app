from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.views import View

from .forms import DocumentForm
from .models import Document

class UploadView(View):
    def get(self, request):
        return render(request, 'upload/upload.html')

    def post(self, request):
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            doc = form.save()
            data = {'is_valid': True, 'name': doc.file.name, 'url': doc.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)
    