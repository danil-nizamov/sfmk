from django.shortcuts import render


def video_view(request):
    context = {}
    return render(request, "video.html", context)
