from django.shortcuts import render
from .models import Video

def video_list(request):
    beginner_videos = Video.objects.filter(difficulty='beginner')
    return render(request, 'libary/video_list.html', {
        'beginner_videos': beginner_videos,
    })

def advanced(request):
    advanced_videos = Video.objects.filter(difficulty='advanced')
    return render(request, 'libary/advanced.html', {
        'advanced_videos': advanced_videos,
    })