from django.shortcuts import render
from .models import job

# Create your views here.

def index(request):

    jobs = job.objects.all()
    
    context = {
        'jobs':jobs,
    }

    return render(request, 'jobs/index.html', context)