from .models import Community

def menu_links(request):
    links = Community.objects.all()
    return dict(links=links)
