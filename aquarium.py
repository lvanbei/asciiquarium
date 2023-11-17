import subprocess
from datetime import datetime

import requests
from gpiozero import MotionSensor


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

def sendNotification(msg):
    try:
        url = "https://ntfy.leotech.cc/asciiquarium"
        auth = ("leo", "@5AFwXsX65AF")
        requests.post(url, auth=auth, data=msg)
        return True
    except:
        return False

def saveLogs(msg):
    try:
        sendNotification(msg)
        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        file1 = open("logs.txt", "a")  # append mode
        file1.write(date_time + " : " + msg + "\n")
        file1.close()
        return True
    except:
        return False

try:
    pir = MotionSensor(17)
except:
    exit(-1)
shutdownDisplay()
runAquarium()
while True:
    pir.wait_for_motion()
    saveLogs("I'm seeing someone !")
    turnOnDisplay()
    pir.wait_for_no_motion()
    saveLogs("No one is here.")
    shutdownDisplay()


