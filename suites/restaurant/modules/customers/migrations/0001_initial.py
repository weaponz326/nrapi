# Generated by Django 4.1 on 2022-09-27 05:22

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('customer_code', models.CharField(blank=True, max_length=64, null=True)),
                ('customer_name', models.CharField(blank=True, max_length=256, null=True)),
                ('customer_type', models.CharField(blank=True, max_length=256, null=True)),
                ('phone', models.CharField(blank=True, max_length=32, null=True)),
                ('email', models.EmailField(blank=True, max_length=128, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('state', models.CharField(blank=True, max_length=128, null=True)),
                ('city', models.CharField(blank=True, max_length=128, null=True)),
                ('post_code', models.CharField(blank=True, max_length=64, null=True)),
                ('allergies', models.TextField(blank=True, null=True)),
                ('preferences', models.TextField(blank=True, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.account', to_field='id')),
            ],
            options={
                'db_table': 'restaurant_module_customer',
            },
        ),
    ]
