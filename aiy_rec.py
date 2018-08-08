# autor : colson (Yeong Jun Kim)
# https://www.github.com/YeongJunKim
from aiy_led import MyLed
from aiy_log import MyLogger
import logging
import aiy.voicehat
import subprocess
import threading
from time import sleep
import RPi.GPIO as GPIO


class MyRec:
    def __init__(self):
        self.logger = MyLogger(level=logging.DEBUG, get="REC")
        self.logger.add_file_stream_handler("logger.log")
        self.logger.logger.debug("Init REC drivers")
        self.proc = 0

    def record_start(self, cmd="sudo arecord -D sysdefault:CARD=0 -d 2 -r 16000 -f S16_LE /home/pi/temp3.wav"):
        thread_ = threading.Thread(target=self.button_check())
        thread = threading.Thread(target=self.record(cmd))
        thread_.start()
        thread.start()

    def record(self, cmd):
        self.logger.logger.debug("recording start")
        self.proc = subprocess.call(cmd, shell=True)

        self.logger.logger.debug("recording completed")

    def __exit__(self):
        self.logger.logger.debug("Exit REC drivers")

    def button_check(self):
        if GPIO.input(23) == 0:
            sleep(1)
            self.proc.kill()



def main():
    button = aiy.voicehat.get_button()
    led = MyLed()
    rec = MyRec()
    while True:
        led.set_color(led=(0x00, 0x00, 0x00))
        button.wait_for_press()
        led.set_color(led=(0xFF, 0xFF, 0xFF))
        rec.record_start()
        led.set_color(led=(0x00, 0x00, 0x00))


if __name__ == '__main__':
    main()




