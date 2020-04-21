# Generated by Django 3.0.5 on 2020-04-21 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='document_status',
            field=models.CharField(default='100', max_length=5, verbose_name='Status do documento'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='document_total_value',
            field=models.FloatField(default=0, verbose_name='Valor total do documento'),
            preserve_default=False,
        ),
    ]
