# Generated by Django 4.1 on 2022-11-03 04:47

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assessment',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('assessment_code', models.CharField(blank=True, max_length=32, null=True)),
                ('assessment_name', models.CharField(blank=True, max_length=256, null=True)),
                ('assessment_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'school_module_assessment',
            },
        ),
        migrations.CreateModel(
            name='AssessmentCodeConfig',
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
                'db_table': 'school_module_assessment_code_config',
            },
        ),
        migrations.CreateModel(
            name='AssessmentSheet',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('score', models.CharField(blank=True, max_length=16, null=True)),
                ('grade', models.CharField(blank=True, max_length=8, null=True)),
                ('remarks', models.CharField(blank=True, max_length=256, null=True)),
                ('assessment', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school_module_assessment.assessment', to_field='id')),
            ],
            options={
                'db_table': 'school_module_assessment_sheet',
            },
        ),
    ]
