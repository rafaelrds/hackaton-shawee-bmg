# Generated by Django 3.0.6 on 2020-05-31 23:21

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_cpf_cnpj'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='expenses',
            field=models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=10),
        ),
        migrations.AddField(
            model_name='user',
            name='income',
            field=models.DecimalField(decimal_places=2, default=Decimal('0'), max_digits=10),
        ),
    ]