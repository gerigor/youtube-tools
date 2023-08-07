from django.shortcuts import render
from common.forms import YtForm
from ytTagExtractor.services.tags_extract_services import extract_all_tags, create_context
from .forms import TagsGeneratorForm


def generate_tags(request):
    form = TagsGeneratorForm(request.POST or None)

    if form.is_valid():
        title = form.cleaned_data.get('title')
        generated_tags = generate_tags(title)
        context = create_context(form, generated_tags, title)

        return render(request, 'ytTagsGenerator/tags_generator.html', context)

    return render(request, 'ytTagsGenerator/tags_generator.html', {'form': form})