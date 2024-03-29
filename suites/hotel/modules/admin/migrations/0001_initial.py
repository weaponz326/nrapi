# Generated by Django 4.1 on 2023-01-20 06:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hotel_account', '0001_initial'),
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
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hotel_account.account', to_field='id')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='hotel_invitee', to=settings.AUTH_USER_MODEL, to_field='id')),
            ],
            options={
                'db_table': 'hotel_module_admin_invitation',
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
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hotel_account.account', to_field='id')),
                ('personal_user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='hotel_account_user', to=settings.AUTH_USER_MODEL, to_field='id')),
            ],
            options={
                'db_table': 'hotel_module_admin_account_user',
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
                ('bills_access', models.BooleanField(default=False)),
                ('staff_access', models.BooleanField(default=False)),
                ('roster_access', models.BooleanField(default=False)),
                ('guests_access', models.BooleanField(default=False)),
                ('payments_access', models.BooleanField(default=False)),
                ('services_access', models.BooleanField(default=False)),
                ('checkin_access', models.BooleanField(default=False)),
                ('bookings_access', models.BooleanField(default=False)),
                ('rooms_access', models.BooleanField(default=False)),
                ('assets_access', models.BooleanField(default=False)),
                ('housekeeping_access', models.BooleanField(default=False)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='hotel_account.account', to_field='id')),
            ],
            options={
                'db_table': 'hotel_module_admin_access',
            },
        ),
    ]
