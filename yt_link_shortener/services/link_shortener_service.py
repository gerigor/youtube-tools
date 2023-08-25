import re


def extract_video_id(url: str) -> str | None:
    """ Gets video id from given url. """

    pattern = r"(?:youtu\.be\/|youtube\.com\/(?:watch\?.*v=|v\/|embed\/|.*\/v\/))([^?&\"'>]+)"
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return None


def create_short_link(video_id: str):
    """ Creates shortened youtube link. """

    return f'https://youtu.be/{video_id}'