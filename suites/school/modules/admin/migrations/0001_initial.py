# Generated by Django 4.1 on 2022-11-03 04:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('school_account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('account_type', models.CharField(max_length=64, null=True)),
                ('invitation_status', models.CharField(max_length=64, null=True)),
                ('date_confirmed', models.DateTimeField(blank=True, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school_account.account', to_field='id')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='school_invitee', to=settings.AUTH_USER_MODEL, to_field='id')),
            ],
            options={
                'db_table': 'school_module_admin_invitation',
            },
        ),
        migrations.CreateModel(
            name='AccountUser',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('is_creator', models.BooleanField(default=False)),
                ('access_level', models.CharField(max_length=32, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school_account.account', to_field='id')),
                ('personal_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='school_account_user', to=settings.AUTH_USER_MODEL, to_field='id')),
            ],
            options={
                'db_table': 'school_module_admin_account_user',
            },
        ),
        migrations.CreateModel(
            name='Access',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('admin_access', models.BooleanField(default=False)),
                ('portal_access', models.BooleanField(default=False)),
                ('settings_access', models.BooleanField(default=False)),
                ('parents_access', models.BooleanField(default=False)),
                ('assessment_access', models.BooleanField(default=False)),
                ('subjects_access', models.BooleanField(default=False)),
                ('attendance_access', models.BooleanField(default=False)),
                ('students_access', models.BooleanField(default=False)),
                ('lesson_plan_access', models.BooleanField(default=False)),
                ('reports_access', models.BooleanField(default=False)),
                ('teachers_access', models.BooleanField(default=False)),
                ('payments_access', models.BooleanField(default=False)),
                ('classes_access', models.BooleanField(default=False)),
                ('timetable_access', models.BooleanField(default=False)),
                ('fees_access', models.BooleanField(default=False)),
                ('sections_access', models.BooleanField(default=False)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school_account.account', to_field='id')),
            ],
            options={
                'db_table': 'school_module_admin_access',
            },
        ),
    ]
