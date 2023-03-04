# Generated by Django 4.1 on 2023-02-11 13:17

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hospital_account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rink',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('rink_type', models.CharField(max_length=64, null=True)),
                ('rink_source', models.CharField(max_length=64, null=True)),
                ('comment', models.TextField(blank=True, null='True')),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='hospital_rink_recipient', to='hospital_account.account', to_field='id')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='hospital_rink_sender', to='hospital_account.account', to_field='id')),
            ],
            options={
                'db_table': 'hospital_nodule_portal_rink',
            },
        ),
    ]
