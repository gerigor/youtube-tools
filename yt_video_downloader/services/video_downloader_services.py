import youtube_dl


def extract_meta_info(video_url: str):
    """Get video information from its url using youtube_dl lib. Returns dictionary."""

    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        meta = ydl.extract_info(
            video_url, download=False)
    return meta


def create_video_audio_streams_list(meta_info: dict):
    """Create list of video and audio streams."""

    video_audio_streams = []

    for meta in meta_info['formats']:
        file_size = meta.get('filesize')

        if file_size:
            file_size = f'{round(int(file_size) / 1000000, 2)} mb'  # bytes to mb
        resolution = 'Audio only'

        # check if the stream has video content and set resolution as "height x width" string
        height = meta.get('height')
        width = meta.get('width')
        if height and width:
            resolution = f"{height}x{width}"

        video_audio_streams.append({
            'resolution': resolution,
            'extension': meta.get('ext', None),
            'file_size': file_size,
            'video_url': meta.get('url', None),
            'format_note': meta.get('format_note'),
        })
    return video_audio_streams


def create_context(form, meta_info: dict, video_audio_streams: list, video_url: str):
    """ Returns context for template. """

    try:
        small_thumb = meta_info.get('thumbnails', [])[4]['url']
    except IndexError:
        small_thumb = None

    return {
        'form': form,
        'title': meta_info.get('title', ''),
        'streams': video_audio_streams[::-1],
        'description': meta_info.get('description', ''),
        'likes': f'{int(meta_info.get("like_count", 0)):,}',
        'thumb': small_thumb,
        'big_thumb': meta_info.get('thumbnail'),
        'duration': round(int(meta_info.get('duration', 1)) / 60, 2),
        'views': f'{int(meta_info.get("view_count", 0)):,}',
        'video_url': video_url,
    }
