from django.shortcuts import render
from .models import Slider,Team
from youtubers.models import Youtuber

# Create your views here.

def home(request):
    sliders = Slider.objects.all()
    tubers_teams = Team.objects.all()
    you_tubers_featured = Youtuber.objects.order_by('-created_date').filter(is_featured = True)
    all_tubers = Youtuber.objects.order_by('-created_date')
    data = {
        'sliders1' : sliders,
        'tubers_team' : tubers_teams,
        'featured_youtubers' : you_tubers_featured,
        'all_tubers' : all_tubers,
    }
    return render(request,'webpages/home.html',data)


def about(request):
    tubers_teams = Team.objects.all()
    data_to_webpage ={
        'tubers_team' : tubers_teams,
    }
    return render(request,'webpages/about.html',data_to_webpage)


def contact(request):
    return render(request,'webpages/contact.html')


def services(request):
    return render(request,'webpages/services.html')
  