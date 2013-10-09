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
