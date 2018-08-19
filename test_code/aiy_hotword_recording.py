# autor : colson (Yeong Jun Kim)
# https://www.github.com/YeongJunKim

from aiy_led import MyLed
from aiy_log import MyLogger
from aiy_play import MyAudio
from aiy_rec import MyRec
import logging
import aiy.voicehat
import datetime
import RPi.GPIO as GPIO
import sys
import signal
import subprocess
import threading

GPIO.setmode(GPIO.BCM)

logger = MyLogger(level=logging.DEBUG, get="MAIN")
led = MyLed()
audio = MyAudio()
rec = MyRec()
button = aiy.voicehat.get_button()

startFlag = 0


class Buttonout:
    class Buttonout(Exception):
        pass

    def __init__(self):
        self.button = aiy.voicehat.get_button()
        self.button.__init__(button.channel, GPIO.RISING)
        self.button.on_press(self.raise_buttonout)
        self.logger = MyLogger(level=logging.DEBUG, get="BUTTON")
        self.logger.logger.debug('init')

    def __enter__(self):
        self.logger.logger.debug('enter')

    def __exit__(self, *args):
        global button
        button.__init__(button.channel, GPIO.FALLING)
        button.on_press(button_handler)
        self.logger.logger.debug('exit')

    def raise_buttonout(self):
        self.logger.logger.debug("hello")
        print(self.button.polarity)
        raise Buttonout.Buttonout()


def button_handler():
    global startFlag
    if startFlag == 0:
        startFlag = 1
    print(button.polarity)


def setup():
    logger.add_file_stream_handler("logger.log")


def start():
    global startFlag
    button.__init__(button.channel, GPIO.FALLING)
    button.on_press(button_handler)

    while True:

        if startFlag == 1:
            try:
                with Buttonout():
                    led.set_color(led=(0xFF, 0xFF, 0xFF))
                    now = datetime.datetime.now()
                    time = "%04d-%02d-%02d-%02d:%02d:%02d" % (now.year, now.month, now.day, now.hour, now.minute, now.second)
                    path = "/home/pi/hot-word-backup"
                    cmd = "sudo arecord -D sysdefault:CARD=0 -d 3 -r 16000 -f S16_LE " + path + "/" + time + ".wav"
                    rec.record_start(cmd)
                    audio.play_audio_path(path + "/" + time + ".wav")
                    led.set_color(led=(0x00, 0x00, 0x00))
                    startFlag = 0
            except:
                print("error")


def main():
    start()


if __name__ == '__main__':
    main()




