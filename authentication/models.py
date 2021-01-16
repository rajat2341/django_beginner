from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class ModelBase(models.Model):
    """
    Abstract Model Base
    """
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        """
        To override the database table name, use the db_table parameter in class Meta.
        """
        abstract = True


class User(AbstractUser, ModelBase):
    """
    User model created here
    """
    role = models.CharField(max_length=512)
    relation = models.ForeignKey("self", on_delete=models.DO_NOTHING, null=True, blank=True)

    class Meta:
        """
        To override the database table name, use the db_table parameter in class Meta.
        """
        db_table = "user"
        verbose_name = "User"
        verbose_name_plural = "Users"


class UserDetails(ModelBase):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    roll_no = models.BigIntegerField()
    phone = models.CharField(max_length=10)

    class Meta:
        """
        To override the database table name, use the db_table parameter in class Meta.
        """
        db_table = "user_details"
        verbose_name = "UserDetails"
        verbose_name_plural = "UserDetails"