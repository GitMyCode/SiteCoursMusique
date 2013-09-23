from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from teachers.models import Teacher, ClassPeriod
def index(request):
    teachers = Teacher.objects.order_by('name')[:5]
    context = {'teachers': teachers}
    return render(request, 'teachers/index.html',context)

def detail(request, teacher_id):
    teacher = get_object_or_404(Teacher, pk=teacher_id)
    return render(request,'teachers/detail.html', {'teacher':teacher})
