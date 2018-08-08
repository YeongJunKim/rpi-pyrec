# autor : colson (Yeong Jun Kim)
# https://www.github.com/YeongJunKim
from aiy.vision.leds import Leds
from time import sleep
from aiy_log import MyLogger
import logging


class MyLed:
    def __init__(self, led=(0x00, 0x00, 0x00)):
        self.logger = MyLogger(level=logging.INFO, get="LED")
        self.leds = Leds()
        self.leds.update(Leds.rgb_on(led))
        self.logger.logger.debug("Init LED drivers")

    def set_color(self, led):
        self.leds.update(Leds.rgb_on(led))
        self.logger.logger.debug("set LED colors")

    def __exit__(self):
        led = (0x00, 0x00, 0x00)
        self.leds.update(Leds.rgb_on(led))
        self.logger.logger.debug("exit LED drivers")


def main():
    a = MyLed()
    while True:
        leds = (0x00, 0x00, 0xFF)
        a.set_color(led=leds)
        sleep(0.1)
        leds = (0x00, 0xFF, 0x00)
        a.set_color(led=leds)
        sleep(0.1)
        leds = (0xFF, 0x00, 0x00)
        a.set_color(led=leds)
        sleep(0.1)


if __name__ == '__main__':
    main()





