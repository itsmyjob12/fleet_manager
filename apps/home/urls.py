# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),


    path('', views.chauffeurs, name='chauffeurs'),
    path('<int:pk>/modifier/', views.modifier_chauffeur, name='modifier_chauffeur'),
    path('<int:pk>/supprimer/', views.supprimer_chauffeur, name='supprimer_chauffeur'),
]
