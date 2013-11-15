# Create your views here.
from django.http import HttpResponse


from django.shortcuts import render_to_response
from django.template import RequestContext
from sitemusique.core.models import (
                                     Generique,
                                     Cours,
                                     Professeurs,
                                     AutresServices,

                                     )



def acceuil(request):
    generique = Generique.objects.get(pk=1)
    cours     = Cours.objects.all()
    professeurs = Professeurs.objects.all()
    autresServices = AutresServices.objects.all()

    context = {
            'generique':generique,
            'cours': cours,
            'professeurs' : professeurs,
            'autresServices':autresServices,
            }
    return render_to_response('acceuil.html', context,RequestContext(request) )


def professeurs(request):
    professeurs = Professeurs.objects.all()
    cours = Cours.objects.all()

    context = {
        'professeurs': professeurs,
    }
    return render_to_response('professeurs.html',context,RequestContext(request))


def cours(request):
    cours = Cours.objects.all()

    context = {
        'cours': cours,
    }
    return render_to_response('cours.html',context,RequestContext(request))


def autresServices(request):

    autresServices = AutresServices.objects.all()

    context = {
        'autresServices':autresServices,
    }

    return render_to_response('autresServices.html',context,RequestContext(request))

def faq(request):

    return render_to_response('faq.html',RequestContext(request))

def contact(request):

    return render_to_response('contact.html',RequestContext(request))



