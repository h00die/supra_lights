import os
import time

import adafruit_matrixkeypad
import board
import digitalio

# 3x4 Phone-style Matrix Keypad
# https://www.adafruit.com/product/1824
cols = [digitalio.DigitalInOut(x) for x in (board.D21, board.D20, board.D26)]
rows = [digitalio.DigitalInOut(x) for x in (board.D19, board.D13, board.D6, board.D5)]
keys = ((1, 2, 3), (4, 5, 6), (7, 8, 9), ("*", 0, "#"))
keypad = adafruit_matrixkeypad.Matrix_Keypad(rows, cols, keys)

LIGHTS = "/usr/bin/python3 /home/pi/lights.py"

# kill all lights to start
os.system(f"{LIGHTS} 0 &")

while True:
    keys = keypad.pressed_keys
    # print("kp %s" % (keys))
    if keys:
        # kill all old threads
        pids = os.popen("ps -A | grep python3").read().split("\n")
        if len(pids) > 1:
            print(pids)
            pids = pids[
                1:-1
            ]  # skip this process which should be first, and the empty last line
            for pid in pids:
                print(pid)
                pid = pid.split()
                os.system("kill -9 %s" % (pid[0]))
        print(f"{LIGHTS} '{keys[0]}' &")
        os.system(f"{LIGHTS} '{keys[0]}' &")
    time.sleep(0.1)
