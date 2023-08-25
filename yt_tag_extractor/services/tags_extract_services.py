import requests
from bs4 import BeautifulSoup


def extract_all_tags(video_url: str):
    """ Returns tags as a list. """
    response = requests.get(video_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        tags_elements = soup.select('meta[property="og:video:tag"]')
        tags = [tag['content'] for tag in tags_elements]
        return tags
    else:
        print('Video has no tags.')


def create_context(form, all_tags: list, video_url: str):
    """ Returns context for template. """
    return {
        'form': form,
        'tags': all_tags,
        'video_url': video_url

    }
