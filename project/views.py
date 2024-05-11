from django.shortcuts import render
from .models import Project

# Create your views here.
def index(request):
    return render(request, 'project/index.html')

def projects(request):
    myProjcets = Project.objects.all()
    context = {
        'myprojects':myProjcets
    }
    return render(request, 'project/projects.html', context)