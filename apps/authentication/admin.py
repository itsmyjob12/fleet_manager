# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import *

admin.site.register(Profile)
admin.site.register(ConducteurProfile)
admin.site.register(AdminProfile)



# Register your models here.
