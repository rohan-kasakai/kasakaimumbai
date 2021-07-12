from django.shortcuts import render
from events.models import Event

def home(request):
    events = Event.objects.all().filter(is_available=True)

    context ={
            'events': events,
        }
    return render(request, 'home.html', context)
