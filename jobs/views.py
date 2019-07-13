from django.shortcuts import render
from .models import Job

def home(request):
    jobs = Job.objects
    return render(request, 'jobs/home.html', 
                 {'title' : 'Doggie Album',
                  'jobs' : jobs})