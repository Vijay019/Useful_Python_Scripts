# Python program to convert a Video file to Audio.

import moviepy.editor as mp
video = mp.VideoFileClip("D:\\python\\yeh meri family.webm")
video.audio.write_audiofile("D:\\python\\yeh meri family.mp3")