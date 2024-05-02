from django.shortcuts import render
from common.forms import YtForm

from .services.video_downloader_services import extract_meta_info, create_video_audio_streams_list, create_context


def download_video(request):
    form = YtForm(request.POST or None)

    if form.is_valid():
        video_url = form.cleaned_data.get('url')
        meta_info = extract_meta_info(video_url)
        video_audio_streams = create_video_audio_streams_list(meta_info)
        context = create_context(form, meta_info, video_audio_streams, video_url)
        return render(request, 'yt_video_downloader/video_downloader.html', context)

    return render(request, 'yt_video_downloader/video_downloader.html', {'form': form})
