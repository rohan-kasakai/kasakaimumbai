from django.urls import path
from . import views

urlpatterns = [
    path('', views.events, name='events'),
    path('Community/<slug:community_slug>/', views.events, name='events_by_community'),
    path('Community/<slug:community_slug>/<slug:event_slug>/', views.event_detail, name='event_detail'),
    path('search/', views.search, name='search'),
]
