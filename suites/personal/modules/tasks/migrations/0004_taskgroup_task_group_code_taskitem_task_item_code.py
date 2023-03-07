# Generated by Django 4.1 on 2023-03-07 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_module_tasks', '0003_taskgroupcodeconfig_taskitemcodeconfig'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskgroup',
            name='task_group_code',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='taskitem',
            name='task_item_code',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
