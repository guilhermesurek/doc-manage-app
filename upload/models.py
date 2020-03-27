from django.db import models

class Document(models.Model):
    cnpj_sender = models.CharField("CNPJ emissor", max_length=14)
    cnpj_recipient = models.CharField("CNPJ destinatário", max_length=14)
    document_number = models.CharField("Número do documento", max_length=30)
    document_key = models.CharField("Chave do documento", max_length=44, null=True)
    document_date = models.DateField("Data de emissão")
    upload_date = models.DateField("Data de upload", auto_now_add=True)
    doc_file = models.FileField("Arquivo do documento", upload_to='docs/')

    def __str__(self):
        return self.cnpj_sender + '_' + self.document_number + '_' + self.document_date

    def delete(self, *args, **kwargs):
        self.doc_file.delete()
        super().delete(*args, **kwargs)