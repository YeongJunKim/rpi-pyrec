# AIY-kit word save
######tupport raspberry pi zero w board wit AIY kit.
![image](http://cdn.shopify.com/s/files/1/0176/3274/products/together-16_1024x1024_28d6a279-1133-4974-ba1a-03ea6e735a66_grande.jpg?v=1506698675)
####installation
#### 1. install AIY-Voice-kit.
###### ```AIY-Voice-kit``` img download.
https://aiyprojects.withgoogle.com/voice/
#### 2. install pip
```angular2html
sudo pip3 install pyaudio
```
####3. run aiy_main.py
```angular2html
python3.5 aiy_main.py
```
#---------------------------------
###### recording
### arecord
```
-q',
'-t',   'raw',
'-D',   'sysdefault:CARD=0',
'-c',   str(channels),
'-f',   sample_width_to_string(bytes_per_sample),
'-r',   str(sample_rate_hz)
'-d',   sampling time
```
### arecord example
```
~$ sudo arecord -D sysdefault:CARD=0 -r 16000 -f S16_LE /home/pi/temp.wav
```
### sound %
```angular2html
~$ amixer set Master 20%
```

