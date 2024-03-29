# Generated by Django 4.1 on 2023-02-13 20:50

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hospital_module_patients', '0001_initial'),
        ('hospital_account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('ward_number', models.CharField(blank=True, max_length=32, null=True)),
                ('ward_name', models.CharField(blank=True, max_length=256, null=True)),
                ('ward_type', models.CharField(blank=True, max_length=256, null=True)),
                ('location', models.CharField(blank=True, max_length=256, null=True)),
                ('capacity', models.IntegerField(blank=True, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hospital_account.account', to_field='id')),
            ],
            options={
                'db_table': 'hospital_module_ward',
            },
        ),
        migrations.CreateModel(
            name='WardCodeConfig',
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
                'db_table': 'hospital_module_ward_code_config',
            },
        ),
        migrations.CreateModel(
            name='WardPatient',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('checkin_date', models.DateField(blank=True, null=True)),
                ('checkout_date', models.DateField(blank=True, null=True)),
                ('bed_number', models.CharField(blank=True, max_length=64, null=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hospital_module_patients.patient', to_field='id')),
                ('ward', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hospital_module_wards.ward', to_field='id')),
            ],
            options={
                'db_table': 'hospital_module_ward_patient',
            },
        ),
    ]
