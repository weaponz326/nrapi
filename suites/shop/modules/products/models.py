import uuid
from django.db import models

from suites.personal.users.models import CustomBaseModel
from suites.shop.accounts.models import Account


def product_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return 'shop/{}/modules/product/{}'.format(instance.account.id, filename)

# Create your models here.

class Product(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    product_code = models.CharField(max_length=64, null=True, blank=True)
    product_name = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    product_category = models.CharField(max_length=128, null=True, blank=True)
    price = models.DecimalField(max_digits=16, decimal_places=2, null=True)
    product_image = models.FileField(null=True, upload_to=product_upload_path)

    class Meta:
        db_table = 'shop_module_product'

    def __str__(self):
        return str(self.id)

class ProductCodeConfig(CustomBaseModel):
    entry_mode = models.CharField(max_length=32, blank=True, null=True)
    prefix = models.CharField(max_length=32, blank=True, null=True)
    suffix = models.CharField(max_length=32, blank=True, null=True)
    last_code = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        db_table = 'shop_module_product_code_config'

    def __str__(self):
        return str(self.id)
