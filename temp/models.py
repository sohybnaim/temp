
from email.policy import default
import imp
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.forms import CharField
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.core.validators import FileExtensionValidator
# Create your models here.


class Companies(models.Model):
    Companies_name = models.CharField(max_length=100)
    email = models.EmailField(('email'), null=True, blank=True)
    website = models.CharField(max_length=100)
    logo = models.ImageField(null=True, upload_to="images/")
    logo= models.ImageField(upload_to='logo/',null=True, default='logo/img.png', blank=True)

    REQUIRED_FIELDS = ['Companies_name', 'email']

    def __str__(self):
        return self.Companies_name


class Employees(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = PhoneNumberField(unique=True, null=False, blank=False)
    email = models.EmailField(('email'), null=True, blank=True)
    Companies_name = models.ForeignKey(
        Companies, on_delete=models.CASCADE, null=True)

    REQUIRED_FIELDS = ['Companies_name', 'email']
