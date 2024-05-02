import re


def extract_video_id(url: str):
    """Get video id from given url. """
    pattern = r"(?:youtu\.be\/|youtube\.com\/(?:watch\?.*v=|v\/|embed\/|.*\/v\/))([^?&\"'>]+)"
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return None


def extract_thumbnails(video_id: str) -> list:
    """Return list of thumbnail urls."""
    default_thumbnail = f'https://img.youtube.com/vi/{video_id}/default.jpg'
    medium_thumbnail = f'https://img.youtube.com/vi/{video_id}/mqdefault.jpg'
    high_thumbnail = f'https://img.youtube.com/vi/{video_id}/hqdefault.jpg'
    maxres_thumbnail = f'https://img.youtube.com/vi/{video_id}/maxresdefault.jpg'
    return [default_thumbnail, medium_thumbnail, high_thumbnail, maxres_thumbnail]


def create_context(form, video_id: str, thumbnail_urls: list):
    """ Creates context for template. """
    return {
        'form': form,
        'video_id': video_id,
        'default_thumbnail': thumbnail_urls[0],
        'medium_thumbnail': thumbnail_urls[1],
        'high_thumbnail': thumbnail_urls[2],
        'maxres_thumbnail': thumbnail_urls[3],
    }
