# Create your views here.
from django.http import HttpResponse


from django.shortcuts import render_to_response
from django.template import RequestContext
from sitemusique.core.models import (
                                     Generique,
                                     Cours,
                                     Professeurs,

                                     )



def acceuil(request):
    generique = Generique.objects.all()

    context = {
            'generique':generique,
            }
    return render_to_response('acceuil.html', context )


def professeurs(request):
    prof = Professeurs.objects.all()

    context = {
        'prof': prof,
    }
    return render_to_response('professeurs.html',context)


def cours(request):
    prof = Cours.objects.all()

    context = {
        'prof': prof,
    }
    return render_to_response('cours.html',context)


def autresServices(request):

    return render_to_response('autresServices.html')

def faq(request):

    return render_to_response('faq.html')

def contact(request):

    return render_to_response('contact.html')



