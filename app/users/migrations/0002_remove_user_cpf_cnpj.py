# Generated by Django 3.0.6 on 2020-05-31 22:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='cpf_cnpj',
        ),
    ]
