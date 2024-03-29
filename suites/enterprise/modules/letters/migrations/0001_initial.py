# Generated by Django 4.1 on 2022-12-17 07:48

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('enterprise_account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SentLetter',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('date_sent', models.DateField(blank=True, null=True)),
                ('reference_number', models.CharField(blank=True, max_length=64, null=True)),
                ('recepient', models.CharField(blank=True, max_length=128, null=True)),
                ('subject', models.CharField(blank=True, max_length=256, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='enterprise_account.account', to_field='id')),
            ],
            options={
                'db_table': 'enterprise_module_letters_sent',
            },
        ),
        migrations.CreateModel(
            name='ReceivedLetter',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('date_received', models.DateField(blank=True, null=True)),
                ('reference_number', models.CharField(blank=True, max_length=64, null=True)),
                ('sender', models.CharField(blank=True, max_length=128, null=True)),
                ('subject', models.CharField(blank=True, max_length=256, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='enterprise_account.account', to_field='id')),
            ],
            options={
                'db_table': 'enterprise_module_letters_received',
            },
        ),
    ]
