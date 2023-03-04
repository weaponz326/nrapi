# Generated by Django 4.1 on 2023-02-13 20:50

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hospital_account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdmissionCodeConfig',
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
                'db_table': 'hospital_module_admission_code_config',
            },
        ),
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('admission_code', models.CharField(blank=True, max_length=64, null=True)),
                ('admission_date', models.DateTimeField(blank=True, null=True)),
                ('discharge_date', models.DateTimeField(blank=True, null=True)),
                ('admission_status', models.CharField(blank=True, max_length=128, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hospital_account.account', to_field='id')),
            ],
            options={
                'db_table': 'hospital_module_admission',
            },
        ),
    ]