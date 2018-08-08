# autor : colson (Yeong Jun Kim)
# https://www.github.com/YeongJunKim

import sys
import aiy.audio
from aiy_log import MyLogger
import logging
sys.path.insert(0, './home/pi/AIY-projects-python/src/aiy')


class MyAudio:
    def __init__(self):
        logger = MyLogger(level=logging.INFO, get="AUDIO")
        logger.logger.debug("Init audio driver")

    def play_audio_path(self, path):
        aiy.audio.set_tts_volume(5)
        aiy.audio.play_wave(path)

    def play_audio_text(self, text):
        aiy.audio.set_tts_volume(5)
        aiy.audio.say(text)


if __name__ == '__main__':
    a = MyAudio()
    a.play_audio_text("hello")
