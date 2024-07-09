# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
def default_profile_image():
    return "images/profile/defaut1.png"


class Profile (models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        profile_image = models.ImageField(upload_to='images/profile', blank=True  )
        role = models.IntegerField(choices=((1, 'Administrator'), (2, 'Conducteur'), ), default=1)
        # is_restreint = models.BooleanField(default= True)
        is_online = models.BooleanField(default=False)

        def __str__(self):
          return self.user.username

@receiver(post_save, sender=User)
def create_or_update_Conducteur_profile(sender, instance, created, **kwargs):
    if created and instance.groups.filter(name='Conducteur').exists():
        ConducteurProfile.objects.create(user=instance)
    elif instance.groups.filter(name='Conducteur').exists():
        instance.Conducteurprofile.save() 
     
# Create your models here
class ConducteurProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_new_conducteur = models.BooleanField(default=True)
    role = models.IntegerField(choices=((1, 'Administrator'), (2, 'Conducteur')), default=2)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True)
    def __str__(self):
        return self.user.username
     #STANDARDS
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    
class AdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_new_admin = models.BooleanField(default=True)
    role = models.IntegerField(choices=((1, 'Administrator'), (2, 'Conducteur')), default=1)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True)
    def __str__(self):
        return self.user.username

         #STANDARDS
    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)