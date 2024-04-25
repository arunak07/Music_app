from django.db import models

class Music(models.Model):
    music_name = models.CharField(max_length=255,null=False)
    music_path = models.CharField(max_length=255,null=False)
    image_path = models.CharField(max_length=255,null=False)