# Generated by Django 4.1 on 2022-11-03 04:47

from django.db import migrations, models
import django.db.models.deletion
import suites.school.modules.students.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school_account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentCodeConfig',
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
                ('year_code', models.CharField(blank=True, max_length=16, null=True)),
            ],
            options={
                'db_table': 'school_module_student_code_config',
            },
        ),
        migrations.CreateModel(
            name='Student',
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
                ('photo', models.FileField(null=True, upload_to=suites.school.modules.students.models.student_upload_path)),
                ('nationality', models.CharField(blank=True, max_length=64, null=True)),
                ('religion', models.CharField(blank=True, max_length=128, null=True)),
                ('phone', models.CharField(blank=True, max_length=32, null=True)),
                ('email', models.EmailField(blank=True, max_length=64, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('state', models.CharField(blank=True, max_length=128, null=True)),
                ('city', models.CharField(blank=True, max_length=128, null=True)),
                ('post_code', models.CharField(blank=True, max_length=64, null=True)),
                ('student_code', models.CharField(blank=True, max_length=32, null=True)),
                ('admission_date', models.DateField(blank=True, null=True)),
                ('previous_school', models.CharField(blank=True, max_length=256, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school_account.account', to_field='id')),
            ],
            options={
                'db_table': 'school_module_student',
            },
        ),
    ]
