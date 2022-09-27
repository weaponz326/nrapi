# Generated by Django 4.1 on 2022-09-27 05:22

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockItem',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('item_code', models.CharField(blank=True, max_length=32, null=True)),
                ('item_name', models.CharField(blank=True, max_length=256, null=True)),
                ('category', models.CharField(blank=True, max_length=128, null=True)),
                ('item_type', models.CharField(blank=True, max_length=128, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('refill_ordered', models.IntegerField(blank=True, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.account', to_field='id')),
            ],
            options={
                'db_table': 'restaurant_module_stock_item',
            },
        ),
    ]
