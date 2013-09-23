from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from datetime import datetime
from news.models import New, Comment
from teachers.models import Teacher 


def home(request):
   return render(request,'index.html')