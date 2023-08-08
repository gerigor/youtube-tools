from django.shortcuts import render
from .forms import TagsGeneratorForm
from .services.tags_generator_services import get_videoids_from_search_results, generate_all_tags, create_context


def generate_tags(request):
    form = TagsGeneratorForm(request.POST or None)

    if form.is_valid():
        title = form.cleaned_data.get('title')
        videoids = get_videoids_from_search_results(title)
        generated_tags = generate_all_tags(videoids)
        context = create_context(form, generated_tags, title)

        return render(request, 'ytTagsGenerator/tags_generator.html', context)

    return render(request, 'ytTagsGenerator/tags_generator.html', {'form': form})