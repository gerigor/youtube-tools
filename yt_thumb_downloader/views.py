from django.shortcuts import render
from common.forms import YtForm

from .services.thumb_downloader_services import extract_video_id, extract_thumbnails, create_context


def downloader(request):
    form = YtForm(request.POST or None)
    if form.is_valid():
        video_url = form.cleaned_data.get('url')
        video_id = extract_video_id(video_url)
        if video_id:
            thumbnail_urls = extract_thumbnails(video_id)
            context = create_context(form, video_id, thumbnail_urls)

            return render(request, 'yt_thumb_downloader/thumb_downloader.html', context)

    return render(request, 'yt_thumb_downloader/thumb_downloader.html', {'form': form})
