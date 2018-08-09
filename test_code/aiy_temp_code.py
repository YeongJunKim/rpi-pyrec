# autor : colson (Yeong Jun Kim)
# https://www.github.com/YeongJunKim






import subprocess
import threading

def my_process():
    a1 = "arecord -f cd -D plughw:0 -d 10 a.wav"

    a2 = "sudo arecord -D sysdefault:CARD=0 -d 5 -r 16000 -f S16_LE /home/pi/temp3.wav"
    subprocess.call(a2,shell= True)
thread = threading.Thread(target=my_process)

thread.start()

print("Audio record is only for 10sec")


# import subprocess
# import os
#
# record = 'sudo arecord -D sysdefault:CARD=0 -r 16000 -f S16_LE /home/pi/temp3.wav'
#
# # p = subprocess.Popen(record, shell=True)
# os.popen(record)