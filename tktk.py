from yt_dlp import YoutubeDL

yt_v_opts = {
    'paths': {
        'home': './videos/tiktok'
    },
    'outtmpl': '%(id)s.%(ext)s'
}

yt_a_opts = {
    'paths': {
        'home': './audios/tiktok'
    },
    'format': 'bestaudio/best',
    'outtmpl': '%(id)s.%(ext)s'
}

def tiktok_dl_audio(url):
    with YoutubeDL(yt_a_opts) as ydl:
        ydl.download([url])

    output_a_path = ydl.prepare_filename(ydl.extract_info(url, download=False))
    print(output_a_path)
    return output_a_path


def tiktok_dl_video(url):
    with YoutubeDL(yt_v_opts) as ydl:
        ydl.download([url])    
    
    output_list = []
    output_v_path = ydl.prepare_filename(ydl.extract_info(url, download=False))
    output_list.append(output_v_path)
    output_list.append(tiktok_dl_audio(url))

    print(output_list)
    return output_list