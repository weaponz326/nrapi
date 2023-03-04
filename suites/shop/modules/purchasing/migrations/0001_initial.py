# Generated by Django 4.1 on 2023-03-04 09:52

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop_account', '0001_initial'),
        ('shop_module_products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Purchasing',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('purchasing_code', models.CharField(blank=True, max_length=64)),
                ('purchasing_date', models.DateTimeField(blank=True, null=True)),
                ('purchasing_status', models.CharField(blank=True, max_length=32, null=True)),
                ('purchasing_total', models.DecimalField(decimal_places=2, max_digits=16, null=True)),
                ('invoice_number', models.CharField(blank=True, max_length=64)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop_account.account', to_field='id')),
            ],
            options={
                'db_table': 'shop_module_purchasing',
            },
        ),
        migrations.CreateModel(
            name='PurchasingCodeConfig',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('entry_mode', models.CharField(blank=True, max_length=32, null=True)),
                ('prefix', models.CharField(blank=True, max_length=32, null=True)),
                ('suffix', models.CharField(blank=True, max_length=32, null=True)),
                ('last_code', models.CharField(blank=True, max_length=64, null=True)),
            ],
            options={
                'db_table': 'shop_module_purchasing_code_config',
            },
        ),
        migrations.CreateModel(
            name='PurchasingItem',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('item_number', models.IntegerField(blank=True, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop_module_products.product', to_field='id')),
                ('purchasing', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop_module_purchasing.purchasing', to_field='id')),
            ],
            options={
                'db_table': 'shop_module_purchasing_item',
            },
        ),
    ]
