from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path('wiki/<str:title>/', views.entry_details, name="wiki_entry"),
    #path('friend/<str:names>/', views.names, name="my_name")
]
