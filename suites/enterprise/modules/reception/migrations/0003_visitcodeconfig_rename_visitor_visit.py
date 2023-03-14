# Generated by Django 4.1 on 2023-03-10 15:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise_account', '0001_initial'),
        ('enterprise_module_reception', '0002_rename_tag_umber_visitor_tag_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='VisitCodeConfig',
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
                'db_table': 'enterprise_module_visit_code_config',
            },
        ),
        migrations.RenameModel(
            old_name='Visitor',
            new_name='Visit',
        ),
    ]