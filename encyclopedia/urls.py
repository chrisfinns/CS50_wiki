from django.urls import path, include
from . import views

app_name = 'encyclopedia'
urlpatterns = [
    path("", views.index, name="index"),
    path('wiki/<str:title>/', views.entry_details, name="wiki_entry"),
    path('search', views.search, name="search"),
    path('new_page', views.new_page, name="new_page")
]
