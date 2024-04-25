from django.urls import path
from .views import play_music, add_music


urlpatterns = [
    path('play_music/',play_music,name="play_music"),
    path('add_music/',add_music, name="add_music")
]