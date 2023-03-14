# Generated by Django 4.1 on 2023-03-05 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop_module_suppliers', '0002_rename_supplieritem_supplierproduct_and_more'),
        ('shop_module_payables', '0003_remove_payable_customer_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payable',
            name='customer',
        ),
        migrations.AddField(
            model_name='payable',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='shop_module_suppliers.supplier', to_field='id'),
        ),
    ]