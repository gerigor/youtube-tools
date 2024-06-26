from django.shortcuts import render
from .forms import TagsGeneratorForm
from .services.tags_generator_services import get_video_ids_from_search_results, generate_all_tags, create_context


def generate_tags(request):
    form = TagsGeneratorForm(request.POST or None)

    if form.is_valid():
        title = form.cleaned_data.get('title')
        video_ids = get_video_ids_from_search_results(title)
        generated_tags = generate_all_tags(video_ids)
        context = {
            'form': form,
            'tags': generated_tags,
            'video_title': title,
        }
        return render(request, 'yt_tags_generator/tags_generator.html', context)

    return render(request, 'yt_tags_generator/tags_generator.html', {'form': form})