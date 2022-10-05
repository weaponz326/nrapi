# Generated by Django 4.1 on 2022-10-05 06:48

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurant_module_staff', '0001_initial'),
        ('restaurant_account', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('batch_name', models.CharField(blank=True, max_length=256)),
                ('batch_symbol', models.CharField(blank=True, max_length=64)),
            ],
            options={
                'db_table': 'restaurant_module_roster_batch',
            },
        ),
        migrations.CreateModel(
            name='Roster',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('roster_code', models.CharField(blank=True, max_length=32)),
                ('roster_name', models.CharField(blank=True, max_length=256)),
                ('from_date', models.DateField(null=True)),
                ('to_date', models.DateField(null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='restaurant_account.account', to_field='id')),
            ],
            options={
                'db_table': 'restaurant_module_roster',
            },
        ),
        migrations.CreateModel(
            name='RosterCodeConfig',
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
                'db_table': 'restaurant_module_roster_code_config',
            },
        ),
        migrations.CreateModel(
            name='StaffPersonnel',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('batch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='roster.batch', to_field='id')),
                ('roster', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='roster.roster', to_field='id')),
                ('staff', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='restaurant_module_staff.staff', to_field='id')),
            ],
            options={
                'db_table': 'restaurant_module_roster_staff',
            },
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('shift_name', models.CharField(blank=True, max_length=256)),
                ('start_time', models.TimeField(null=True)),
                ('end_time', models.TimeField(null=True)),
                ('roster', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='roster.roster', to_field='id')),
            ],
            options={
                'db_table': 'restaurant_module_roster_shift',
            },
        ),
        migrations.CreateModel(
            name='RosterDay',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('day', models.DateField(blank=True, null=True)),
                ('batch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='roster.batch', to_field='id')),
                ('roster', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='roster.roster', to_field='id')),
                ('shift', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='roster.shift', to_field='id')),
            ],
            options={
                'db_table': 'restaurant_module_roster_day',
            },
        ),
        migrations.AddField(
            model_name='batch',
            name='roster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='roster.roster', to_field='id'),
        ),
    ]
