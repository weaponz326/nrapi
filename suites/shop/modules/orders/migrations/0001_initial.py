# Generated by Django 4.1 on 2023-03-04 09:52

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop_module_products', '0001_initial'),
        ('shop_account', '0001_initial'),
        ('shop_module_customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('customer_name', models.CharField(blank=True, max_length=256, null=True)),
                ('order_code', models.CharField(blank=True, max_length=64)),
                ('order_date', models.DateTimeField(blank=True, null=True)),
                ('order_type', models.CharField(blank=True, max_length=64, null=True)),
                ('order_status', models.CharField(blank=True, max_length=32, null=True)),
                ('order_total', models.DecimalField(decimal_places=2, max_digits=16, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop_account.account', to_field='id')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='shop_module_customers.customer', to_field='id')),
            ],
            options={
                'db_table': 'shop_module_order',
            },
        ),
        migrations.CreateModel(
            name='OrderCodeConfig',
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
                'db_table': 'shop_module_order_code_config',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('item_number', models.IntegerField(blank=True, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop_module_orders.order', to_field='id')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop_module_products.product', to_field='id')),
            ],
            options={
                'db_table': 'shop_module_order_item',
            },
        ),
    ]