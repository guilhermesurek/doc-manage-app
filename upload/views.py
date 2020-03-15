from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from .forms import DocumentForm
from .models import Document

@login_required()
def upload_view(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('download')
    else:
        form = DocumentForm()
    return render(request, 'upload/upload.html', {
        'form': form
    })