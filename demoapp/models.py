from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class Vendor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    product = models.CharField(max_length=100, null=True) 

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    company_established = models.DateField(null=True)
    software_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name
    



class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    business_name = models.CharField(max_length=100)
    business_type = models.CharField(max_length=100)
    business_address = models.CharField(max_length=255)
    
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='custom_user_groups',
        related_query_name='custom_user_group',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_permissions',
        related_query_name='custom_user_permission',
    )

    # Specify custom related names for groups and user_permissions
    class Meta:
        permissions = [('can_change_status', 'Can change status')]
        verbose_name_plural = "Custom Users"
