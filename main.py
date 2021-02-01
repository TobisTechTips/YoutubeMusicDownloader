from __future__ import unicode_literals
import youtube-dl
print("Link hier einfügen / Insert the link")
link = input ("")

ydl_opts = {
    'format': 'bestaudio/best'
    'postprocressors:' [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320'
    }]
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])
