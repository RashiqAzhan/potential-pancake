from django.db import models


class User(models.Model):
    date_of_birth = models.DateTimeField(verbose_name="Date of birth", null=False, blank=False, )
    gender = models.CharField(verbose_name="Gender", max_length=1, null=False, blank=False, )
    phone = models.CharField(verbose_name="Phone Number", null=False, blank=False, unique=True, max_length=11)
    address = models.TextField(verbose_name="Address", null=False, blank=False)
