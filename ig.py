from yt_dlp import YoutubeDL

yt_v_opts = {
    'paths': {
        'home': './videos/instagram'
    },    
    'outtmpl': '%(id)s.%(ext)s'
}

yt_a_opts = {
    'paths': {
        'home': './audios/instagram'
    },
    'format': 'bestaudio/best',
    'outtmpl': '%(id)s.%(ext)s'
}

def ig_dl_audio(url):
    with YoutubeDL(yt_a_opts) as ydl:
        ydl.download([url])

    output_a_path = ydl.prepare_filename(ydl.extract_info(url, download=False))
    print(output_a_path)
    return output_a_path


def ig_dl_video(url):
    with YoutubeDL(yt_v_opts) as ydl:
        ydl.download([url])    
    
    output_list = []
    output_v_path = ydl.prepare_filename(ydl.extract_info(url, download=False))
    output_list.append(output_v_path)
    output_list.append(ig_dl_audio(url))

    print(output_list)
    return output_list