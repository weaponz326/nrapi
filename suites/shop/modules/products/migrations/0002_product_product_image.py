# Generated by Django 4.1 on 2023-03-04 17:09

from django.db import migrations, models
import suites.shop.modules.products.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_module_products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.FileField(null=True, upload_to=suites.shop.modules.products.models.product_upload_path),
        ),
    ]