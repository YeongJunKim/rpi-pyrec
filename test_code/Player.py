from datetime import datetime
from pytz import timezone
from subprocess import call
import os

def main():
    now = datetime.now(timezone('Asia/Seoul'))

    while True:
        name=str(input("file name: "))
        name=os.getcwd()+'/'+now.strftime('%Y%m%d_')+name+'.wav'
        call(["aplay", name])

if __name__ == '__main__':
    main()