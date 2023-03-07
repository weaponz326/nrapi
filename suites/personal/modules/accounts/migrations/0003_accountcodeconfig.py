# Generated by Django 4.1 on 2023-03-07 15:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('personal_module_accounts', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountCodeConfig',
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
                'db_table': 'personal_module_account_code_config',
            },
        ),
    ]
