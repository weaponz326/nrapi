# Generated by Django 4.1 on 2022-09-20 14:28

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('payment_code', models.CharField(blank=True, max_length=64, null=True)),
                ('payment_date', models.DateTimeField(blank=True, null=True)),
                ('amount_paid', models.DecimalField(blank=True, decimal_places=2, max_digits=11, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.account', to_field='id')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='orders.order', to_field='id')),
            ],
            options={
                'db_table': 'restaurant_module_payment',
            },
        ),
    ]
