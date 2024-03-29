# Generated by Django 4.1 on 2022-11-03 04:47

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school_account', '0001_initial'),
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
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='school_rink_recipient', to='school_account.account', to_field='id')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='school_rink_sender', to='school_account.account', to_field='id')),
            ],
            options={
                'db_table': 'school_nodule_portal_rink',
            },
        ),
    ]
