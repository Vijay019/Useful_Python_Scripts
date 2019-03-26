# Python Script to download your desired video from Youtube.

import pytube

video_link = 'https://www.youtube.com/watch?v=JFGV250-29U'

yt = pytube.YouTube(video_link)

videos = yt.streams.first()

videos.download('D:\\python')