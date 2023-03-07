# Generated by Django 4.1 on 2023-03-07 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_module_budget', '0004_expenditure_budget_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expenditure',
            name='budget_code',
        ),
        migrations.AddField(
            model_name='budget',
            name='budget_code',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
