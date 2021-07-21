from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Event
from Community.models import Community
from carts.models import Cartitem

from carts.views import _cart_id
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q

# Create your views here.

def events(request, community_slug=None):
    communities = None
    events = None

    if community_slug != None:
        communities = get_object_or_404(Community, slug=community_slug)
        events = Event.objects.filter(community=communities, is_available=True)
        paginator = Paginator(events, 6)
        page = request.GET.get('page')
        paged_events = paginator.get_page(page)
        event_count = events.count()
    else:
        events = Event.objects.all().filter(is_available=True).order_by('id')
        paginator = Paginator(events, 6)
        page = request.GET.get('page')
        paged_events = paginator.get_page(page)
        event_count = events.count()
    context ={
            'events': paged_events,
            'event_count':event_count,
        }
    return render(request, 'events/events.html', context)


def event_detail(request, community_slug, event_slug):
    try:
        single_event = Event.objects.get(community__slug=community_slug, slug=event_slug)
        in_cart = Cartitem.objects.filter(cart__cart_id=_cart_id(request), event=single_event)

    except Exception as e:
        raise e 

    context = {
        'single_event' : single_event,
        'in_cart' : in_cart,
        }
    return render(request, 'events/event_detail.html', context)

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            events = Event.objects.order_by('-created_date').filter(Q(description__icontains=keyword) | Q(event_name__icontains=keyword))
            event_count = events.count()
        context = {
            'events' : events,
            'event_count' : event_count,
        }
    return render(request, 'events/events.html', context)
