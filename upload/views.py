from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.views import View

from .forms import DocumentForm
from .models import Document, EntityType, Entity
import xmltodict
from utils.xmlnfe import xml_nfe

class UploadView(View):
    def get(self, request):
        context = {
            'upload_page': 'active'
        }
        return render(request, 'upload/upload.html', context=context)

    def post(self, request):
        form = DocumentForm(request.POST, request.FILES)
        form.data = read_xml_nfe_data(form.data, xml_nfe(dict_nfe=xmltodict.parse(form.files['doc_file'])))
        if form.is_valid():
            doc = form.save()
            data = {'is_valid': True, 'docs': doc}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)

def read_xml_nfe_data(data, dict_doc):
    #dict_doc = xml_nfe(self.doc_file.url)               # Read uploaded xml file into a dict
    # Update document fields in Document instance
    data._mutable = True
    for attr, val in dict_doc.document.items():
        data[attr] = val
    # Get or Create Entity instances
    sender, _ = Entity.objects.get_or_create(cnpj=dict_doc.sender.get("cnpj"), defaults=dict_doc.sender)
    recipient, _ = Entity.objects.get_or_create(cnpj=dict_doc.recipient.get("cnpj"), defaults=dict_doc.recipient)
    if dict_doc.deliver_to.get("cnpj") != None:
        deliver_to, _ = Entity.objects.get_or_create(cnpj=dict_doc.deliver_to.get("cnpj"), defaults=dict_doc.deliver_to)
    else:
        deliver_to = recipient
    carrier, _ = Entity.objects.get_or_create(cnpj=dict_doc.carrier.get("cnpj"), defaults=dict_doc.carrier)
    # Set Entity instances to Document instance
    data["sender"] = sender
    data["recipient"] = recipient
    data["deliver_to"] = deliver_to
    data["carrier"] = carrier
    data._mutable = False
    return data

@login_required()
def single_upload(request):
    form = DocumentForm()
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        form.data = read_xml_nfe_data(form.data, xml_nfe(dict_nfe=xmltodict.parse(form.files['doc_file'])))
        if form.is_valid():
            doc = form.save()
            data = {
                'form': form,
                'docs': [doc],
                'msg': 'Carregado!'
            }
        else:
            data = {
                'form': form,
                'msg': form.errors.as_text
            }
    else:
        data = {
                'form': form
            }
    return render(request, "upload/single_upload.html", context=data)