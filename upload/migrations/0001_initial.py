# Generated by Django 3.0.4 on 2020-03-15 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj_sender', models.CharField(max_length=14)),
                ('cnpj_recipient', models.CharField(max_length=14)),
                ('document_number', models.CharField(max_length=30)),
                ('document_key', models.CharField(max_length=44, null=True)),
                ('document_date', models.DateField()),
                ('upload_date', models.DateField(auto_now_add=True)),
                ('doc_file', models.FileField(upload_to='docs/')),
            ],
        ),
    ]