# Generated by Django 4.1 on 2023-03-10 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('association_module_committees', '0003_committeecodeconfig'),
    ]

    operations = [
        migrations.AddField(
            model_name='committee',
            name='committee_code',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
