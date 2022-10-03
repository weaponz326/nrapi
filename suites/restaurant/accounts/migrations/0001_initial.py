# Generated by Django 4.1 on 2022-09-28 17:09

from django.db import migrations, models
import suites.restaurant.accounts.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=256)),
                ('location', models.CharField(max_length=256)),
                ('about', models.TextField()),
                ('logo', models.FileField(blank=True, null=True, upload_to=suites.restaurant.accounts.models.accounts_upload_path)),
            ],
            options={
                'db_table': 'restauarant_account',
            },
        ),
    ]
