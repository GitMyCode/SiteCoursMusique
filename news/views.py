from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.urlresolvers import reverse
from datetime import datetime
from news.models import New, Comment
from teachers.models import Teacher 
def index(request):
    latest_news = New.objects.order_by('creation_date')[:5]
    context = {'latest_news': latest_news}
    return render(request, 'news/index.html',context)

def detail(request, new_id):
    new = get_object_or_404(New, pk=new_id)
    comments = new.comment_set.all()
    return render(request, 'news/detail.html',{'new': new,'comments':comments})

def comment_detail(request, new_id, comment_id):
    return HttpResponse("You're looking at comment %s" % comment_id)

def comment(request, new_id):
    new = get_object_or_404(New, pk=new_id)
    try:
        content = request.POST['comment']
        author = request.POST['author']
        now = datetime.now()
        if not author:
            return render(request,'news/index.html', {'new': new, 'error_message':"Vous n'avez pas inscrit le nom de l'auteur"})
      
        if not content:
            return render(request,'news/index.html', {'new': new, 'error_message':"Le commentaire est vide"})

        c = Comment(id=None, author=author, comment=content, new=new, creation_date=now )
        c.save()
    except (KeyError, New.DoesNotExist):
        return render(request,'news/{{ new_id }}', {'new': new, 'error_message':'The news does not exist'})

    return HttpResponseRedirect(reverse('news:detail', args=(new.id,)))