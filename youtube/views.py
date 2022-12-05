from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q
from .models import Video


def video_view(request, video_id):
    video = Video.objects.get(video_id=video_id)
    other_videos = Video.objects.filter(~Q(video_id=video_id))
    context = {'video': video, 'other_videos': other_videos}
    return render(request, "video.html", context)


def videos_to_models(request):
    from parser.parser import load_videos
    videos = load_videos('parser/video_dataset.csv')
    for index, row in videos.iterrows():
        video_object = Video(
            video_id=row['id'],
            title=row['title'],
            description=row['description'],
            preview=row['thumbnail_maxres'],
            video=None,
            upload_datetime=row['published_datetime'],
            likes=row['likes'],
        )
        video_object.save()
    return HttpResponse(status=200)
