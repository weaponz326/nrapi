# Generated by Django 4.1 on 2023-03-05 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_module_receivables', '0002_receivable_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receivable',
            name='customer_name',
        ),
    ]