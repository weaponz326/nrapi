# Generated by Django 4.1 on 2022-09-28 17:09

from django.db import migrations, models
import django.db.models.deletion
import suites.restaurant.modules.staff.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('restaurant_account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('first_name', models.CharField(blank=True, max_length=128, null=True)),
                ('last_name', models.CharField(blank=True, max_length=128, null=True)),
                ('sex', models.CharField(blank=True, max_length=16, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('photo', models.FileField(null=True, upload_to=suites.restaurant.modules.staff.models.staff_upload_path)),
                ('nationality', models.CharField(blank=True, max_length=64, null=True)),
                ('religion', models.CharField(blank=True, max_length=128, null=True)),
                ('phone', models.CharField(blank=True, max_length=32, null=True)),
                ('email', models.EmailField(blank=True, max_length=64, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('state', models.CharField(blank=True, max_length=128, null=True)),
                ('city', models.CharField(blank=True, max_length=128, null=True)),
                ('post_code', models.CharField(blank=True, max_length=64, null=True)),
                ('staff_code', models.CharField(blank=True, max_length=32, null=True)),
                ('department', models.CharField(blank=True, max_length=256, null=True)),
                ('job', models.CharField(blank=True, max_length=256, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='restaurant_account.account', to_field='id')),
            ],
            options={
                'db_table': 'restaurant_module_staff',
            },
        ),
    ]
