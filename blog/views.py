#-*- coding: utf-8 -*-
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import render

def tpl(request):
    return render(request, 'blog/tpl.html', {'current_date': datetime.now()})

def home(request):
    text = """<h1>Bienvenue sur mon blog !</h1>
        <p>Les crêpes bretonnes ça tue des mouettes en plein vol !</p>"""
    return HttpResponse(text)

def addition(request, nombre1, nombre2):
    total = int(nombre1) + int(nombre2)

    # retourne nombre1, nombre2 et la somme des deux
    return render(request, 'blog/addition.html', locals())
