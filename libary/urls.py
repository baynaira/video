from django.urls import path
from . import views

app_name = 'libary'

urlpatterns = [
    path('', views.video_list, name='video_list'),
    path('advanced/', views.advanced, name='advanced'),
]