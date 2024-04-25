from django.urls import path,include
from .views import User_register,user_login



urlpatterns = [
    path('register/',User_register,name="register"),
    path('login/',user_login,name='login'),
    path('music/',include('music.urls'),name="music")
]