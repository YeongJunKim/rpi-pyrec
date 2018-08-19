import aiy.voicehat
import RPi.GPIO as GPIO
from aiy_log import MyLogger
import logging

GPIO.setmode(GPIO.BCM)


class Buttonout:
    class Buttonout(Exception):
        pass

    def __init__(self):
        self.button = aiy.voicehat.get_button()
        self.logger = MyLogger(level=logging.DEBUG, get="BUTTON")
        self.logger.add_file_stream_handler('logger.log')

    def __enter__(self):
        self.logger.logger.debug("enter")
        self.run()

    def __exit__(self):
        self.logger.logger.debug("exit")

    def run(self):
        self.logger.logger.debug("detect switch state")
        while True:
            if GPIO.input(self.button.channel):
                raise Buttonout.Buttonout()


if __name__ == '__main__':
    try:
        with Buttonout():
            print("hi")

    except Buttonout.Buttonout:
        print("buttonout")


