# Generated by Django 4.1 on 2022-10-15 10:41

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school_account', '0001_initial'),
        ('school_module_students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clase',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('class_name', models.CharField(blank=True, max_length=256, null=True)),
                ('grade', models.CharField(blank=True, max_length=128, null=True)),
                ('location', models.CharField(blank=True, max_length=256, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school_account.account', to_field='id')),
            ],
            options={
                'db_table': 'school_module_class',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('department_name', models.CharField(blank=True, max_length=256, null=True)),
                ('department_description', models.TextField(blank=True, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school_account.account', to_field='id')),
            ],
            options={
                'db_table': 'school_module_department',
            },
        ),
        migrations.CreateModel(
            name='ClassStudent',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('clase', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school_module_classes.clase', to_field='id')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school_module_students.student', to_field='id')),
            ],
            options={
                'db_table': 'school_module_class_student',
            },
        ),
        migrations.AddField(
            model_name='clase',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school_module_classes.department', to_field='id'),
        ),
    ]
