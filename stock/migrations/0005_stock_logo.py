# Generated by Django 4.1.1 on 2022-09-19 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0004_currency_stock_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
