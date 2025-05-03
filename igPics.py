from instaloader import Instaloader, Profile, Post
import re
from pathlib import Path

# Get instance
L = Instaloader()
# L.login(USER, PASSWORD)

# Load a profile from an Instagram handle
# profile = Profile.from_username(L.context, '05kaizin')

# get and return user profile picture
def ig_dl_profilepic(url):
    with YoutubeDL(yt_a_opts) as ydl:
        ydl.download([url])

    output_a_path = ydl.prepare_filename(ydl.extract_info(url, download=False))
    print(output_a_path)
    return output_a_path

def ig_dl_audio(url):
    with YoutubeDL(yt_a_opts) as ydl:
        ydl.download([url])

    output_a_path = ydl.prepare_filename(ydl.extract_info(url, download=False))
    print(output_a_path)
    return output_a_path

def extract_shortcode(url):
    shortcode = re.search(r'instagram.com/p/([^/]+)/', url)
    if shortcode:
        return shortcode.group(1)
    else:
        return None



def ig_pfp(url, username):
    # L.login("hellisforu", "vikai1812")
    # Example usage
    # extrai o shortcode
    shortcode = extract_shortcode(url)
    print(shortcode)
    # cria a estrutura post com metadata
    post = Post.from_shortcode(L.context, shortcode)
    # posso acessar a metadata agora
    caption = post.caption
    criadoEm = post.date_local

    dateUtc = str(post.date_utc).replace(":", "-").replace(" ", "_")
    mediaCount = post.mediacount
    print(mediaCount)

    path = Path('igPics/' + username)
    postNode = L.download_post(post=post, target=path)
    mediaArr = []

    if mediaCount == 1:
        mediaArr.append(f'{path}\\{dateUtc}_UTC.jpg')
    else:
        for i in range(mediaCount):
            e = i + 1
            mediaArr.append(f'{path}\\{dateUtc}_UTC_{e}.jpg')
    print(mediaArr)
        
        


    # print(post.caption)
    return mediaArr, caption, criadoEm, mediaCount
    

# L.download_profilepic(profile.username, profile)

