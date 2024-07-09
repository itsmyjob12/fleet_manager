# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import (Modele,MarqueVoiture,Voiture,conducteur)

admin.site.register(Modele)
admin.site.register(MarqueVoiture)
admin.site.register(Voiture)
admin.site.register(conducteur)
