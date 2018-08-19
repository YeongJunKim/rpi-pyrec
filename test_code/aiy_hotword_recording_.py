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
GPIO.setmode(GPIO.BCM)

logger = MyLogger(level=logging.DEBUG, get="MAIN")
led = MyLed()
audio = MyAudio()
rec = MyRec()

startFlag = 0
stopFlag = 0

def setup():
    logger.add_file_stream_handler("logger.log")


def button_callback():
    print("button callback")
    global startFlag
    if startFlag == 0:
        startFlag = 1


def start():
    global startFlag
    button = aiy.voicehat.get_button()
    button.on_press(button_callback)
    # thread_button_checker = ButtonCheck(name="button_checker")
    # thread_button_checker.start()

    while True:
        if startFlag == 1:
            led.set_color(led=(0xFF, 0xFF, 0xFF))
            now = datetime.datetime.now()
            time = "%04d-%02d-%02d-%02d:%02d:%02d" % (now.year, now.month, now.day, now.hour, now.minute, now.second)
            path = "/home/pi/hot-word-backup"
            cmd = "sudo arecord -D sysdefault:CARD=0 -d 4 -r 16000 -f S16_LE " + path + "/" + time + ".wav"
            rec.record_start(cmd)
            audio.play_audio_path(path + "/" + time + ".wav")
            led.set_color(led=(0x00, 0x00, 0x00))
            startFlag = 0


def main():
    start()


if __name__ == '__main__':
    main()




