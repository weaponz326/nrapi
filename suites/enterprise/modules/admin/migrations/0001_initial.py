# Generated by Django 4.1 on 2022-12-11 19:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('enterprise_account', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='enterprise_account.account', to_field='id')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='enterprise_invitee', to=settings.AUTH_USER_MODEL, to_field='id')),
            ],
            options={
                'db_table': 'enterprise_module_admin_invitation',
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
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='enterprise_account.account', to_field='id')),
                ('personal_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='enterprise_account_user', to=settings.AUTH_USER_MODEL, to_field='id')),
            ],
            options={
                'db_table': 'enterprise_module_admin_account_user',
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
                ('accounts_access', models.BooleanField(default=False)),
                ('appraisal_access', models.BooleanField(default=False)),
                ('assets_access', models.BooleanField(default=False)),
                ('attendance_access', models.BooleanField(default=False)),
                ('budget_access', models.BooleanField(default=False)),
                ('employees_access', models.BooleanField(default=False)),
                ('files_access', models.BooleanField(default=False)),
                ('leave_access', models.BooleanField(default=False)),
                ('fiscal_year_access', models.BooleanField(default=False)),
                ('ledger_access', models.BooleanField(default=False)),
                ('letters_access', models.BooleanField(default=False)),
                ('payroll_access', models.BooleanField(default=False)),
                ('procurement_access', models.BooleanField(default=False)),
                ('reception_access', models.BooleanField(default=False)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='enterprise_account.account', to_field='id')),
            ],
            options={
                'db_table': 'enterprise_module_admin_access',
            },
        ),
    ]
