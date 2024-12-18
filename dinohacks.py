import subprocess
import time
import pychrome
from pynput import keyboard
import threading
import random

browser = pychrome.Browser(url="http://127.0.0.1:1234")
print(__file__)
tab = browser.new_tab("chrome://dino")
tab.start()

def main_loop():
    global tab
    cactiX=tab.Runtime.evaluate(expression="Runner.instance_.setSpeed(3)")
    while True:
        try:
            cactiX=tab.Runtime.evaluate(expression="Runner.instance_.horizon.obstacles[0].xPos")["result"]["value"]
            print(cactiX)
            if cactiX <= 200:
                tab.Runtime.evaluate(expression="Runner.instance_.horizon.obstacles.pop(0)")
                tab.Runtime.evaluate(expression="Runner.instance_.distanceRan+=1000")
        except:
            print("didn't find it")

        time.sleep(0.05)


main_loop()
