from aiy.vision.leds import Leds
import time
RED = (0xFF, 0x00, 0x00)

leds = Leds()
leds.update(Leds.rgb_on(RED))
#time.sleep(10)
#leds.update(Leds.rgb_off())
#while 1:
#    leds.update(Leds.rgb_off())
#    print('hello')

# #!/usr/bin/python3.5
#
# from time import sleep
# from threading import Thread
#
# from audio import capture, capture_stop
#
# class Audio(Thread):
#
#     def __init__(self, filename):
#         Thread.__init__(self)
#         self._filename = filename
#
#     def run(self):
#         capture(self._filename)
#
#     def stop(self):
#         capture_stop()
#
# a = Audio("c.wav")
# a.start()
# try:
#     while 1:
#         sleep(0.1)
# finally:
#     a.stop()