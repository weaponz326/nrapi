# Generated by Django 4.1 on 2023-01-20 06:49

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hotel_account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('bill_code', models.CharField(blank=True, max_length=64)),
                ('bill_date', models.DateTimeField(blank=True, null=True)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=16, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hotel_account.account', to_field='id')),
            ],
            options={
                'db_table': 'hotel_module_bill',
            },
        ),
        migrations.CreateModel(
            name='BillCodeConfig',
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
                'db_table': 'hotel_module_bill_code_config',
            },
        ),
        migrations.CreateModel(
            name='ServiceCharge',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('item_number', models.IntegerField(blank=True, null=True)),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hotel_module_bills.bill', to_field='id')),
            ],
            options={
                'db_table': 'hotel_module_bill_service_charge',
            },
        ),
        migrations.CreateModel(
            name='CheckinCharge',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('item_number', models.IntegerField(blank=True, null=True)),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hotel_module_bills.bill', to_field='id')),
            ],
            options={
                'db_table': 'hotel_module_bill_checkin_charge',
            },
        ),
    ]
