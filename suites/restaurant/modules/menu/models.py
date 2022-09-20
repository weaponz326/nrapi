import uuid
from django.db import models

from suites.personal.users.models import CustomBaseModel
from suites.restaurant.accounts.models import Account


def menu_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return 'restaurant/{}/modules/menu/{}'.format(instance.menu_group.account.id, filename)

# Create your models here.

class MenuGroup(CustomBaseModel):
    account = models.ForeignKey(Account, to_field='id', on_delete=models.DO_NOTHING)
    menu_group = models.CharField(max_length=256, null=True)
    category = models.CharField(max_length=64, null=True)

    class Meta:
        db_table = 'restaurant_module_menu_group'

    def __str__(self):
        return str(self.id)

class MenuItem(CustomBaseModel):
    menu_group = models.ForeignKey(MenuGroup, to_field='id', on_delete=models.DO_NOTHING)
    item_code = models.CharField(max_length=32, blank=True)
    item_name = models.CharField(max_length=256, blank=True)
    price = models.DecimalField(max_digits=11, decimal_places=2, null=True)
    image = models.FileField(null=True, blank=True, upload_to=menu_upload_path)
    description = models.TextField(blank=True)

    class Meta:
        db_table = 'restaurant_module_menu_item'

    def __str__(self):
        return str(self.id)
