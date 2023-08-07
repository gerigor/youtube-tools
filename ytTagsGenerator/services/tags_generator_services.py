import requests
from bs4 import BeautifulSoup
import re


def get_videoids_from_search_results(title: str):
    """ Searching top videos by given title. """

    search_query = f'https://www.youtube.com/results?search_query={title.replace(" ", "+")}&sp=CAMSAggF'
    res = requests.get(search_query)
    soup = BeautifulSoup(res.text, 'html.parser')
    all_videoids = re.findall(r'"videoRenderer":{"videoId":"([^"]+)"', str(soup))

    return all_videoids


def exctract_tags_from_video(link: str):
    """ Returns tags as a list. """
    pass


def generate_tags(links: list):
    """ Get unique tags from youtube videos. """
    pass


def create_context(form, generated_tags: list, title: str):
    """ Returns context for template. """
    return {
        'form': form,
        'tags': generated_tags,
        'video_url': title,
    }
