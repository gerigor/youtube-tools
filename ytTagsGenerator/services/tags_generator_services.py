import requests
from bs4 import BeautifulSoup
import re


def get_videoids_from_search_results(title: str):
    """ Returns video ids from first page of search query sorted by views for the last year. """

    search_query = f'https://www.youtube.com/results?search_query={title.replace(" ", "+")}&sp=CAMSAggF'
    response = requests.get(search_query)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        video_ids = re.findall(r'"videoRenderer":{"videoId":"([^"]+)"', str(soup))

        return video_ids


def exctract_tags_from_video(video_url: str):
    """ Returns tags as a list from given url. """
    response = requests.get(video_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        tags_elements = soup.select('meta[property="og:video:tag"]')
        tags = [tag['content'] for tag in tags_elements]
        return tags
    else:
        print('Video has no tags.')


def generate_all_tags(video_ids: list):
    """ Get unique tags from youtube videos. """

    all_tags = []

    for video_id in video_ids:
        video_url = f'https://www.youtube.com/watch?v={video_id}'
        tags = exctract_tags_from_video(video_url)
        all_tags.extend(tags)

        if len(set(all_tags)) >= 30:
            break

    unique_tags = list(set(all_tags))[:30]  # Get the first 30 unique tags
    print(unique_tags)

    return unique_tags


def create_context(form, generated_tags: list, title: str):
    """ Returns context for template. """
    return {
        'form': form,
        'tags': generated_tags,
        'video_title': title,
    }
