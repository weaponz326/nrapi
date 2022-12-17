# Generated by Django 4.1 on 2022-12-17 06:30

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('enterprise_module_employees', '0001_initial'),
        ('enterprise_account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('leave_code', models.CharField(blank=True, max_length=64, null=True)),
                ('leave_type', models.CharField(blank=True, max_length=256, null=True)),
                ('leave_start', models.DateField(blank=True, null=True)),
                ('leave_end', models.DateField(blank=True, null=True)),
                ('leave_status', models.CharField(blank=True, max_length=128, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='enterprise_account.account', to_field='id')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='enterprise_module_employees.employee', to_field='id')),
            ],
            options={
                'db_table': 'enterprise_module_leave',
            },
        ),
    ]
