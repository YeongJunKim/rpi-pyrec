
import logging
from aiy_log import MyLogger
import threading
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

logger = MyLogger(level=logging.DEBUG, get="THREAD")


class ButtonCheck(threading.Thread):
    #
    # def __init__(self):
    #     super(ButtonCheck, self).__init__()
    #     logger.logger.debug(threading.currentThread().getName())

    def run(self):
        while True:
            if GPIO.input(23) == 0:
                print(threading.currentThread().getName())


