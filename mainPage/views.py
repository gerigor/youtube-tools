from django.shortcuts import render, get_object_or_404


def home_page(request):
    return render(request, 'mainPage/index.html')
