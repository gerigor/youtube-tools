import requests
from bs4 import BeautifulSoup


def extract_all_tags(video_url: str) -> list | None:
    """Return tags as a list."""
    response = requests.get(video_url)
    if response.status_code != 200:
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    tags_elements = soup.select('meta[property="og:video:tag"]')
    tags = [tag['content'] for tag in tags_elements]
    return tags
