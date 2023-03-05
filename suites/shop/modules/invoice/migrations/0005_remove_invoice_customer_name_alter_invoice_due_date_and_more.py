# Generated by Django 4.1 on 2023-03-05 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_module_invoice', '0004_rename_invoice_code_invoice_invoice_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='customer_name',
        ),
        migrations.AlterField(
            model_name='invoice',
            name='due_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoice_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
