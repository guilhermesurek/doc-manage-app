from django import forms

from .models import Document

class DocumentForm(forms.ModelForm):

    def clean_cnpj_sender(self):
        cnpj_sender = self.cleaned_data.get('cnpj_sender')
        if not cnpj_sender.isdigit():
            raise forms.ValidationError('CNPJ do emissor não contém apenas dígitos.')
        if len(cnpj_sender) != 14:
            raise forms.ValidationError('CNPJ do emissor não contém 14 dígitos.')
        if (cnpj_sender == (14 * '0')) or (cnpj_sender == (14 * '1')) or (cnpj_sender == (14 * '2')) or (cnpj_sender == (14 * '3')) or \
             (cnpj_sender == (14 * '4')) or (cnpj_sender == (14 * '5')) or (cnpj_sender == (14 * '6')) or (cnpj_sender == (14 * '7')) or \
             (cnpj_sender == (14 * '8')) or (cnpj_sender == (14 * '9')):
            raise forms.ValidationError('CNPJ do emissor inválido.')
        return cnpj_sender
    
    def clean_cnpj_recipient(self):
        cnpj_recipient = self.cleaned_data.get('cnpj_recipient')
        if not cnpj_recipient.isdigit():
            raise forms.ValidationError('CNPJ do destinatário não contém apenas dígitos.')
        if len(cnpj_recipient) != 14:
            raise forms.ValidationError('CNPJ do destinatário não contém 14 dígitos.')
        if (cnpj_recipient == (14 * '0')) or (cnpj_recipient == (14 * '1')) or (cnpj_recipient == (14 * '2')) or (cnpj_recipient == (14 * '3')) or \
             (cnpj_recipient == (14 * '4')) or (cnpj_recipient == (14 * '5')) or (cnpj_recipient == (14 * '6')) or (cnpj_recipient == (14 * '7')) or \
             (cnpj_recipient == (14 * '8')) or (cnpj_recipient == (14 * '9')):
            raise forms.ValidationError('CNPJ do destinatário inválido.')
        return cnpj_recipient
    
    class Meta:
        model = Document
        fields = ('cnpj_sender', 'cnpj_recipient', 'document_number', 'document_key', 'document_date', 'doc_file')