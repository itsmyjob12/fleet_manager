# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views
from .views import *

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),


    path('home/ajout/vehicule/', new_voiture, name='ajout_vehicule'),
    path('home/liste/vehicules/', list_voitures, name='liste_voiture'),
    path('home/profile/', profile, name='profile'),
    path('home/list-mrque/', listView, name='listmrque'),
    

]
