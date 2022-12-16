# Generated by Django 4.1 on 2022-12-11 19:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import suites.enterprise.accounts.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
                ('logo', models.FileField(blank=True, null=True, upload_to=suites.enterprise.accounts.models.accounts_upload_path)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='enterprise_account', to=settings.AUTH_USER_MODEL, to_field='id')),
            ],
            options={
                'db_table': 'enterprise_account',
            },
        ),
    ]
