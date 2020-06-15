from django.test import TestCase
import vlc
import time
# Create your tests here.


p = vlc.MediaPlayer("/Users/zhao/PycharmProjects/aistroy/aistory/story_resource/1.mp3")
p.play()


while True:
    time.sleep(1)
    print(p.get_time())
    p.pause()
    p.pause()
    p.audio_set_volume(50)
    p.audio_get_volume()