# -*- coding: utf-8 -*-\
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    user = models.OneToOneField(
                 User, on_delete=models.CASCADE,
                 related_name='Profile',
                 verbose_name='User',
     )
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=12, blank=True, null=True)
