# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50 , blank = False)
    email = models.CharField(max_length=100 , blank = False)
    password = models.CharField(max_length=100 , blank = False)