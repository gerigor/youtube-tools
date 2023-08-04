from django.shortcuts import render
from common.forms import YtForm
from ytTagExtractor.services.tags_extract_services import extract_all_tags, create_context


def generate_tags(request):

    return render(request, 'ytTagsGenerator/tags_generator.html')