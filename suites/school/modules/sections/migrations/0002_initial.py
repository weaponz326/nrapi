# Generated by Django 4.1 on 2022-10-15 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school_module_sections', '0001_initial'),
        ('school_account', '0001_initial'),
        ('school_module_students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sectionstudent',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school_module_students.student', to_field='id'),
        ),
        migrations.AddField(
            model_name='section',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='school_account.account', to_field='id'),
        ),
    ]
