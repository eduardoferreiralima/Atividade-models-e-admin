# Generated by Django 5.1.4 on 2025-01-25 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atv', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='data_criacao',
            field=models.DateTimeField(auto_created=True, auto_now=True),
        ),
    ]
