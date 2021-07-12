from django.urls import path
from . import views

urlpatterns = [
    path('', views.events, name='events'),
    path('community/<slug:community_slug>/', views.events, name='events_by_community'),
]
