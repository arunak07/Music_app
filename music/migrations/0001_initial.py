# Generated by Django 5.0.2 on 2024-04-09 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('music_name', models.CharField(max_length=255)),
                ('music_path', models.CharField(max_length=255)),
                ('image_path', models.CharField(max_length=255)),
            ],
        ),
    ]
