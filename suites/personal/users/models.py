from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

from .managers import CustomBaseManager, CustomUserManager


def users_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return 'personal/{}/users/{}'.format(instance.id, filename)

# Create your models here.

# base model for all models
# implements uuid for keys and softdelete features
class CustomBaseModel(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, max_length=36)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    objects = CustomBaseManager()

    class Meta:
        abstract = True

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.deleted_at = None
        self.save()

    def remove(self):
        super(CustomBaseModel, self).delete()

class User(AbstractUser, CustomBaseModel):
    username = None
    email = models.EmailField(max_length=256, unique=True)
    location = models.CharField(max_length=256)
    about = models.TextField()
    photo = models.FileField(null=True, blank=True, upload_to=users_upload_path)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "location", "about"]

    class Meta:
        db_table = 'personal_user'

    def get_full_name(self):
        return f"{self.first_name} - {self.last_name}"

    def get_short_name(self):
        return self.username

    def __str__(self):
        return str(self.id)
         