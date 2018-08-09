# autor : colson (Yeong Jun Kim)
# https://www.github.com/YeongJunKim
import pyaudio
import wave
import logging
import time
import aiy.voicehat
import threading
import datetime
import RPi.GPIO as GPIO
from aiy_led import MyLed
from aiy_log import MyLogger
from aiy_play import MyAudio

GPIO.setmode(GPIO.BCM)

button = aiy.voicehat.get_button()
led = MyLed()
play = MyAudio()
logger = MyLogger(level=logging.INFO, get="MAIN")

startFlag = 0
audio = 0
stream = 0
timeCnt = 0
timeout = 0
timerStart = 0
timeExitFlag = 0


def timer():
    global timeCnt
    global timeExitFlag
    global timerStart
    logger.logger.debug("timer_1")
    if timerStart == 1:
        if timeCnt > timeout:
            if GPIO.input(23) == 1:
                timeCnt = 0
                timeExitFlag = 1
        else:
            timeCnt = timeCnt + 1
    threading.Timer(1, timer).start()


def checkstate():
    logger.logger.debug("timer_2")
    if startFlag == 0:
        led.set_color(led=(0xFF, 0x00, 0x00))
        time.sleep(0.2)
        led.set_color(led=(0x00, 0x00, 0x00))
    threading.Timer(0.2, checkstate).start()


def stop_recording():
    global audio
    global stream
    stream.stop_stream()
    stream.close()
    audio.terminate()


def button_callback():
    print("button callback")
    global startFlag
    if startFlag == 0:
        startFlag = 1


def setup():
    global button
    timer()
    checkstate()
    button.on_press(button_callback)


def find_audio_device():
    po = pyaudio.PyAudio()
    for index in range(po.get_device_count()):
        desc = po.get_device_info_by_index(index)
        print("DEVICE: %s  INDEX:  %s  RATE:  %s " % (desc["name"], index, int(desc["defaultSampleRate"])))


def loop():
    global startFlag, audio, stream, timeExitFlag, timeout, timeCnt, timerStart
    while True:
        if startFlag == 1:

            FORMAT = pyaudio.paInt16
            CHANNELS = 1
            RATE = 16000
            CHUNK = 1024
            audio = pyaudio.PyAudio()

            # start Recording
            startFlag = 2
            stream = audio.open(format=pyaudio.paInt16,
                                channels=CHANNELS,
                                rate=RATE,
                                input=True,
                                input_device_index=1,
                                frames_per_buffer=CHUNK)

            try:
                timeCnt = 0
                timeout = 2
                timerStart = 1
                print("recording...")
                led.set_color(led=(0xFF, 0xFF, 0xFF))
                frames = []
                while True:
                    data = stream.read(CHUNK)
                    frames.append(data)
                    if GPIO.input(23) == 1 and timeExitFlag == 1:
                        timeExitFlag = 0
                        timerStart = 0
                        break
            except :
                logger.logger.debug("timeout")

            led.set_color(led=(0x00, 0x00, 0x00))
            print("finished recording")

            now = datetime.datetime.now()
            time_c = "%04d-%02d-%02d-%02d:%02d:%02d" % (now.year, now.month, now.day, now.hour, now.minute, now.second)
            path = "/home/pi/hot-word-backup"
            file = path + "/" + time_c + ".wav"

            savefile = wave.open(file, 'wb')
            savefile.setnchannels(CHANNELS)
            savefile.setsampwidth(audio.get_sample_size(FORMAT))
            savefile.setframerate(RATE)
            savefile.writeframes(b''.join(frames))
            savefile.close()

            logger.logger.info(file + " is saved")

            stream.stop_stream()
            stream.close()
            audio.terminate()
            play.play_audio_text("thank you!")

            startFlag = 0


def main():
    setup()
    loop()


if __name__ == '__main__':
    main()











