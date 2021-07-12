from django.shortcuts import render, get_object_or_404
from .models import Event
from Community.models import Community

# Create your views here.

def events(request, community_slug=None):
    communities = None
    events = None

    if community_slug != None:
        communties = get_object_or_404(Community, slug=community_slug)
        events = Event.objects.filter(community=communities, is_available=True)
        event_count = events.count()
    else:
        events = Event.objects.all().filter(is_available=True)
        event_count = events.count()
    context ={
            'events': events,
            'event_count':event_count,
        }
    return render(request, 'events/events.html', context)
