from django.shortcuts import render,redirect
from .models import Music
import os


def add_music(request):
    image_path = "./music/static/images"
    song_path = "./music/static/songs"
    for song_path,img_path in zip(os.listdir(song_path),os.listdir(image_path)):
        add_music = Music(image_path = "images/"+img_path, music_path = "songs/"+song_path, music_name = song_path)
        add_music.save()
    return redirect('play_music')


def play_music(request):
    music_data = Music.objects.all()
    return render(request,'play_music.html',{'paths' : music_data})