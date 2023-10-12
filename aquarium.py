from ast import While
import threading
import subprocess

def setInterval(func,time):
    e = threading.Event()
    while not e.wait(time):
        func()

def setTimeout(func, time):
    e = threading.Event()
    e.wait(time)
    func()

def runAquarium():
    subprocess.Popen(["xterm", "-fullscreen", "asciiquarium"])
    print("launched")

def shutdownDisplay():
    print("shutdown")
    subprocess.run('xrandr --output "HDMI-2" --off', shell=True)
def turnOnDisplay():
    print("turn on")
    subprocess.run('xrandr --output "HDMI-2" --auto', shell=True)

e = threading.Event()
shutdownDisplay()
runAquarium()
while True:
    turnOnDisplay()
    e.wait(30)
    shutdownDisplay()
    e.wait(10)