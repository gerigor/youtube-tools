from django.shortcuts import render
from common.forms import YtForm
from ytTagExtractor.services.tags_extract_services import extract_all_tags, create_context


def extract_tags(request):
    form = YtForm(request.POST or None)

    if form.is_valid():
        video_url = form.cleaned_data.get('url')
        all_tags = extract_all_tags(video_url)
        context = create_context(form, all_tags, video_url)

        return render(request, 'ytTagExtractor/tags_extractor.html', context)

    return render(request, 'ytTagExtractor/tags_extractor.html', {'form': form})