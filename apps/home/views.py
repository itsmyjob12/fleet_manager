# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Chauffeur
from .forms import ChauffeurForm


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))


def chauffeurs(request):
    if request.method == 'POST':
        form = ChauffeurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestion_chauffeurs')
    else:
        form = ChauffeurForm()
    
    chauffeurs = Chauffeur.objects.all()
    return render(request, 'chauffeurs.html', {'form': form, 'chauffeurs': chauffeurs})

def supprimer_chauffeur(request, pk):
    chauffeur = get_object_or_404(Chauffeur, pk=pk)
    chauffeur.delete()
    return redirect('chauffeurs')

def modifier_chauffeur(request, pk):
    chauffeur = get_object_or_404(Chauffeur, pk=pk)
    if request.method == 'POST':
        form = ChauffeurForm(request.POST, instance=chauffeur)
        if form.is_valid():
            form.save()
            return redirect('chauffeurs')
    else:
        form = ChauffeurForm(instance=chauffeur)
    
    chauffeurs = Chauffeur.objects.all()
    return render(request, 'chauffeurs.html', {'form': form, 'chauffeurs': chauffeurs})
