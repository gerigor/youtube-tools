from django.shortcuts import render
from common.forms import YtForm
from yt_link_shortener.services.link_shortener_service import extract_video_id, create_short_link


def link_shortener(request):
    form = YtForm(request.POST or None)
    if form.is_valid():
        video_url = form.cleaned_data.get('url')
        video_id = extract_video_id(video_url)
        if video_id:
            shorten_link = create_short_link(video_id)

            return render(request, 'yt_link_shortener/link_shortener.html', {
                'form': form,
                'shorten_link': shorten_link,
            })

    return render(request, 'yt_link_shortener/link_shortener.html', {'form': form})

# Create your views here.
