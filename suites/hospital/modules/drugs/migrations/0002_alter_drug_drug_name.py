# Generated by Django 4.1 on 2023-02-21 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital_module_drugs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug',
            name='drug_name',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
