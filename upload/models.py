from django.db import models

class Document(models.Model):
    cnpj_sender = models.CharField(max_length=14)
    cnpj_recipient = models.CharField(max_length=14)
    document_number = models.CharField(max_length=30)
    document_key = models.CharField(max_length=44, null=True)
    document_date = models.DateField()
    upload_date = models.DateField(auto_now_add=True)
    doc_file = models.FileField(upload_to='docs/')

    def __str__(self):
        return self.cnpj_sender + '_' + self.document_number + '_' + self.document_date

    def delete(self, *args, **kwargs):
        self.doc_file.delete()
        super().delete(*args, **kwargs)