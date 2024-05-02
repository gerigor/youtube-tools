from django.shortcuts import render
from common.forms import YtForm
from yt_tag_extractor.services.tags_extract_services import extract_all_tags


def extract_tags(request):
    form = YtForm(request.POST or None)

    if form.is_valid():
        video_url = form.cleaned_data.get('url')
        all_tags = extract_all_tags(video_url)
        context = {
            'form': form,
            'tags': all_tags,
            'video_url': video_url
        }
        return render(request, 'yt_tag_extractor/tags_extractor.html', context)

    return render(request, 'yt_tag_extractor/tags_extractor.html', {'form': form})
