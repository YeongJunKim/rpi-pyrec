# AIY-kit word save

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