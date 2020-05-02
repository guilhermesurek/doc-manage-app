from django.db import models
class StdModel(models.Model):
    date_lastupdated = models.DateField(auto_now=True)
    date_added = models.DateField(auto_now_add=True)
    timestamp_lastupdated = models.DateTimeField(auto_now=True)
    timestamp_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class EntityType(StdModel):
    entity_type = models.CharField("Tipo de entidade", max_length=20)

    class Meta:
        verbose_name = "Tipo de Entidade"
        verbose_name_plural = "Tipos de Entidade"

class Entity(StdModel):
    cnpj = models.CharField("CNPJ", max_length=14, primary_key=True)
    company_name = models.CharField("Razão Social", max_length=120)
    fantasy_name = models.CharField("Nome Fantasia", max_length=100)
    address_name = models.CharField("Logradouro", max_length=200)
    address_number = models.CharField("Número", max_length=20, blank=True)
    neighborhood = models.CharField("Bairro", max_length=100, blank=True)
    city_code = models.CharField("Código do município", max_length=7, blank=True)
    city_name = models.CharField("Código do município", max_length=100)
    state_code = models.CharField("UF", max_length=2)
    zip_code = models.CharField("CEP", max_length=8, blank=True)
    country_code = models.CharField("Código do país", max_length=4, blank=True)
    country_name = models.CharField("País", max_length=40, blank=True)
    phone_number = models.CharField("Telefone", max_length=16, blank=True)
    state_registration = models.CharField("IE", max_length=16, blank=True)
    entity_type = models.ManyToManyField(EntityType, blank=True)

    def __str__(self):
        return self.fantasy_name
    
    def save(self, *args, **kwargs):
        if self.fantasy_name == None or self.fantasy_name == '':
            self.fantasy_name = self.company_name
        super(Entity, self).save(*args, **kwargs)

    class Meta:
        ordering = ["company_name"]
        verbose_name = "Entidade"
        verbose_name_plural = "Entidades"

class Document(StdModel):
    sender = models.ForeignKey(Entity, on_delete=models.CASCADE, verbose_name="emissor", related_name='sender_document_set')
    recipient = models.ForeignKey(Entity, on_delete=models.CASCADE, verbose_name="destinatário", related_name='recipient_document_set')
    carrier = models.ForeignKey(Entity, on_delete=models.CASCADE, verbose_name="transportador", related_name='carrier_document_set')
    deliver_to = models.ForeignKey(Entity, on_delete=models.CASCADE, verbose_name="entrega", related_name='deliver_to_document_set')
    document_type = models.CharField("Modalidade de documento", max_length=2)
    document_number = models.CharField("Número do documento", max_length=30)
    document_key = models.CharField("Chave do documento", max_length=44, primary_key=True)
    document_date = models.DateField("Data de emissão")
    document_total_value = models.FloatField("Valor total do documento")
    document_status = models.CharField("Status do documento", max_length=5)
    doc_file = models.FileField("Arquivo do documento", upload_to='docs/')

    def __str__(self):
        if self.document_key != None:
            return self.document_key
        return self.sender.cnpj + '_' + self.document_number + '_' + self.document_date

    def delete(self, *args, **kwargs):
        self.doc_file.delete()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = "Documento"
        verbose_name_plural = "Documentos"
    
    def to_dict_json(self):
        return {
            'name_sender': self.sender.fantasy_name,
            'cnpj_sender': self.sender.cnpj,
            'name_recipient': self.recipient.fantasy_name,
            'cnpj_recipient': self.recipient.cnpj,
            'document_type': self.document_type,
            'document_number': self.document_number,
            'document_key': self.document_key,
            'document_date': self.document_date,
            'document_total_value': self.document_total_value,
            'document_status': self.document_status,
            'document_file_name': self.doc_file.name,
            'document_file_url': self.doc_file.url,
        }