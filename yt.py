from pytube import YouTube
import youtube_dl
import subprocess
import time

video_url = input("link: ")

def mp4():
    global video_url
    yt = YouTube(video_url)
    print(yt.title)
    print(yt.description)
    stream = yt.streams.first()
    print('\n')
    print("downloading.....")
    stream.download()
    print('Succes')
    print('\n')

def mp3():
    global video_url
    video_info = youtube_dl.YoutubeDL().extract_info(
        url=video_url, download=False
    )
    filename = f"{video_info['title']}.mp3"
    options = {
        'format': 'bestaudio/best',
        'keepvideo': False,
        'outtmpl': filename,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }
    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])
    print("Succes")
    print('\n')

class menu:
    def a():
        b = input("format[mp3/mp4]: ")
        if b == 'mp3':
            mp3()
            time.sleep(2)
        elif b == 'mp4':
            mp4()
            time.sleep(2)
        else:
            print("PILIH YG BENER")
            time.sleep(3)
            exit()
    def c():
        d = input("want to input another?: [y/n]")
        if d == 'y':
            video_url = input("link: ")
            menu.a()
            time.sleep(2)
            menu.c()
        elif d == 'n':
            exit()
        else:
            exit()

while True:
    menu.a()
    menu.c()
