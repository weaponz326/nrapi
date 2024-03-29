# Generated by Django 4.1 on 2022-09-28 17:09

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('calendar_name', models.CharField(blank=True, max_length=256, null=True)),
            ],
            options={
                'db_table': 'personal_module_calendar',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('schedule_name', models.CharField(blank=True, max_length=256, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=256, null=True)),
                ('status', models.CharField(blank=True, max_length=32, null=True)),
                ('calendar', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='personal_module_calendar.calendar', to_field='id')),
            ],
            options={
                'db_table': 'personal_module_calendar_schedule',
            },
        ),
    ]
