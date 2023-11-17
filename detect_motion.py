import threading
import subprocess
from gpiozero import MotionSensor
from datetime import datetime

def setInterval(func,time):
    e = threading.Event()
    while not e.wait(time):
        func()

def setTimeout(func, time):
    e = threading.Event()
    e.wait(time)
    func()

def runAquarium():
    res = subprocess.Popen("/usr/bin/asciiquarium", text=True)
    #print("launched")

def shutdownDisplay():
    res = subprocess.run('setterm --blank force', shell=True, capture_output=True, text=True)
    if(res.stderr != ""):
        exit(-1)
    #print("shutdown")
def turnOnDisplay():
    res = subprocess.run('setterm --blank poke', shell=True, capture_output=True, text=True)
    if(res.stderr != ""):
       exit(-1)
    #print("turn on")

e = threading.Event()
try:
    pir = MotionSensor(17)
except:
    exit(-1)
#shutdownDisplay()
#runAquarium()
print("init done");
while True:
    now = datetime.now()
    date_time = now.strftime("%H:%M:%S")
    pir.wait_for_motion()
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    print(date_time + " : human")
    #turnOnDisplay()
    pir.wait_for_no_motion()
    now = datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    print(date_time + " : looking")
    #shutdownDisplay()


