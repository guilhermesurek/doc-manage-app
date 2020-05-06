from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
import math
from datetime import datetime

from upload.models import Document

class DownloadView(View):
    def get(self, request):
        context = {
            'download_page': 'active'
        }
        return render(request, 'download/download.html', context=context)

    def post(self, request):
        request_filter = {}
        aux = request.POST.get("cnpj_sender")
        if aux != '':
            request_filter['sender__cnpj'] = aux
        aux = request.POST.get("cnpj_recipient")
        if aux != '':
            request_filter['recipient__cnpj'] = aux
        aux = request.POST.get("document_key")
        if aux != '':
            request_filter['document_key'] = aux
        aux = request.POST.get("document_date_min")
        aux1 = request.POST.get("document_date_max")
        if aux != '' and aux1 == '':
            request_filter['document_date'] = aux
        elif aux != '' and aux1 != '':
            request_filter['document_date__range'] = [aux, aux1]
        
        docs = Document.objects.filter(**request_filter)
        context = {
            'download_page': 'active',
            'docs': docs
        }
        return render(request, 'download/download.html', context=context)

class DownloadTableView(View):
    def get(self, request):
        context = {
            'download_page': 'active'
        }
        return render(request, 'download/download_datatable.html', context=context)

    def post(self, request):
        context = {
            'download_page': 'active'
        }
        return render(request, 'download/download_datatable.html', context=context)

def document_json(request):
    docs = Document.objects.all()
    total = docs.count()

    _start = request.GET.get('start')
    _length = request.GET.get('length')
    if _start and _length:
        start = int(_start)
        length = int(_length)
        page = math.ceil(start / length) + 1  # [opcional]
        per_page = length  # [opcional]

        docs = docs[start:start + length]

    data = [doc.to_dict_json() for doc in docs]
    response = {
        'data': data,
        #'page': page,  # [opcional]
        #'per_page': per_page,  # [opcional]
        'recordsTotal': total,
        'recordsFiltered': total,
    }
    return JsonResponse(response)