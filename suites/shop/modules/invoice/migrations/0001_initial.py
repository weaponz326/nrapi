# Generated by Django 4.1 on 2023-03-04 08:34

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('customer_name', models.CharField(blank=True, max_length=256, null=True)),
                ('customer_contact', models.TextField(blank=True, null=True)),
                ('invoice_code', models.CharField(blank=True, max_length=64)),
                ('invoice_date', models.DateTimeField(blank=True, null=True)),
                ('due_date', models.DateTimeField(blank=True, null=True)),
                ('invoice_status', models.CharField(blank=True, max_length=32, null=True)),
                ('invoice_total', models.DecimalField(decimal_places=2, max_digits=16, null=True)),
            ],
            options={
                'db_table': 'shop_module_invoice',
            },
        ),
        migrations.CreateModel(
            name='InvoiceCodeConfig',
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
                'db_table': 'shop_module_invoice_code_config',
            },
        ),
        migrations.CreateModel(
            name='InvoiceItem',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('item_number', models.IntegerField(blank=True, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop_module_invoice.invoice', to_field='id')),
            ],
            options={
                'db_table': 'shop_module_invoice_item',
            },
        ),
    ]
