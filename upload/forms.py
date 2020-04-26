from django import forms

from .models import Document, Entity, EntityType
from utils.xmlnfe import xml_nfe

class DocumentForm(forms.ModelForm):
    
    class Meta:
        model = Document
        fields = ('doc_file', 'sender', 'recipient', 'carrier', 'deliver_to', 'document_type', 'document_number', 'document_key',
                  'document_date', 'document_total_value', 'document_status')
        widgets = {
            'sender': forms.HiddenInput(),
            'recipient': forms.HiddenInput(),
            'carrier': forms.HiddenInput(),
            'deliver_to': forms.HiddenInput(),
            'document_type': forms.HiddenInput(),
            'document_number': forms.HiddenInput(),
            'document_key': forms.HiddenInput(),
            'document_date': forms.HiddenInput(),
            'document_total_value': forms.HiddenInput(),
            'document_status': forms.HiddenInput(),
        }
    
    '''def save(self, commit=True):
        instance = super(DocumentForm, self).save(False)        # Get instance
        import ipdb; ipdb.set_trace()
        dict_doc = xml_nfe(self.doc_file.url)               # Read uploaded xml file into a dict
        # Update document fields in Document instance
        for attr, val in dict_doc.document.items():
            setattr(instance, attr, val)
        # Get or Create Entity instances
        sender, _ = Entity.objects.get_or_create(cnpj=dict_doc.sender.get("cnpj"), defaults=dict_doc.sender)
        recipient, _ = Entity.objects.get_or_create(cnpj=dict_doc.recipient.get("cnpj"), defaults=dict_doc.recipient)
        if dict_doc.deliver_to.get("cnpj") != None:
            deliver_to, _ = Entity.objects.get_or_create(cnpj=dict_doc.deliver_to.get("cnpj"), defaults=dict_doc.deliver_to)
        else:
            deliver_to = recipient
        carrier, _ = Entity.objects.get_or_create(cnpj=dict_doc.carrier.get("cnpj"), defaults=dict_doc.carrier)
        # Set Entity instances to Document instance
        setattr(instance, "sender", sender)
        setattr(instance, "recipient", recipient)
        setattr(instance, "deliver_to", deliver_to)
        setattr(instance, "carrier", carrier)
        # Check commit and save
        if commit:
            instance.save()
        return instance'''