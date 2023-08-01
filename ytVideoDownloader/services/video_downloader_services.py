import youtube_dl


def extract_meta_info(video_url: str):
    """ Gets video information from its url using youtube_dl lib. Returns dictionary. """

    ydl_opts = {}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        meta = ydl.extract_info(
            video_url, download=False)
    return meta


def create_video_audio_streams_list(meta_info: dict):
    """ Creates list of video and audio streams. """

    video_audio_streams = []

    for m in meta_info['formats']:
        file_size = m['filesize']

        if file_size is not None:
            file_size = f'{round(int(file_size) / 1000000, 2)} mb'  # bytes to mb
        resolution = 'Audio only'

        # check if the stream has video content and set resolution as "height x width" string
        if m['height'] is not None:
            resolution = f"{m['height']}x{m['width']}"

        video_audio_streams.append({
            'resolution': resolution,
            'extension': m['ext'],
            'file_size': file_size,
            'video_url': m['url'],
            'format_note': m['format_note'],
        })
    return video_audio_streams


def create_context(form, meta_info: dict, video_audio_streams: list, video_url: str):
    """ Returns context for template. """
    return {
        'form': form,
        'title': meta_info.get('title', None),
        'streams': video_audio_streams[::-1],  # reverses the order of the list
        'description': meta_info.get('description'),
        'likes': f'{int(meta_info.get("like_count", 0)):,}',
        'thumb': meta_info.get('thumbnails')[4]['url'],
        'big_thumb': meta_info.get('thumbnail'),
        'duration': round(int(meta_info.get('duration', 1)) / 60, 2),
        'views': f'{int(meta_info.get("view_count")):,}',
        'video_url': video_url,
    }



