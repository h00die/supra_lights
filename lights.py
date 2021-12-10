import argparse
import os
import time

import adafruit_tlc5947
import board
import busio
import digitalio

# initialize LED driver
spi = busio.SPI(clock=board.SCK, MOSI=board.MOSI)
latch = digitalio.DigitalInOut(board.D0)
led_driver = adafruit_tlc5947.TLC5947(spi, latch)

TMP = "/tmp/lights_last_input"

parser = argparse.ArgumentParser(description="Control lights")
parser.add_argument(
    "display", metavar="N", type=str, help="which display action to run"
)
args = parser.parse_args()


SLEEP = 0.3
OFF = 0
ON = 4095


def license_1(i):
    led_driver[18] = i


def license_2(i):
    led_driver[21] = i


def license(i):
    license_1(i)
    license_2(i)


def brake_1(i):
    led_driver[3] = i
    led_driver[6] = i


def brake_2(i):
    led_driver[9] = i
    led_driver[12] = i


def brake(i):
    brake_1(i)
    brake_2(i)


def turn(i):
    led_driver[0] = i


def rev(i):
    led_driver[15] = i


def all_off():
    rev(OFF)
    turn(OFF)
    brake(OFF)
    license(OFF)


def all(i):
    rev(i)
    turn(i)
    brake(i)
    license(i)


def alt_flash():
    while 1:
        turn(OFF)
        rev(OFF)
        license_1(OFF)
        brake(ON)
        license_2(ON)
        time.sleep(SLEEP)
        turn(ON)
        rev(ON)
        license_1(ON)
        brake(OFF)
        license_2(OFF)
        time.sleep(SLEEP)


def flash():
    while 1:
        turn(OFF)
        rev(OFF)
        license_1(OFF)
        brake(OFF)
        license_2(OFF)
        time.sleep(SLEEP)
        turn(ON)
        rev(ON)
        license_1(ON)
        brake(ON)
        license_2(ON)
        time.sleep(SLEEP)


def pulse():
    while 1:
        all_off()
        for i in range(1, 20):
            all(int(ON / i))
        for i in reversed(range(1, 20)):
            all(int(ON / i))


def move():
    all_off()
    lights = [turn, brake_1, brake_2, rev, license_1, license_2]
    while 1:
        for light in lights:
            all(512)
            light(ON)
            time.sleep(SLEEP / 3)
        for light in reversed(lights):
            all(512)
            light(ON)
            time.sleep(SLEEP / 3)


def wave():
    all_off()
    lights = [turn, brake_1, brake_2, rev, license_1, license_2]
    b = [ON, 2048, 1024, 512, 256, OFF]
    while 1:
        for light in lights:
            i = lights.index(light)
            light(b[i])
            time.sleep(SLEEP / 3)
        lights.insert(0, lights.pop())


last_input = ""
if os.path.exists(TMP):
    with open(TMP) as f:
        last_input = f.read().strip()

with open(TMP, "w") as f:
    f.write(args.display)

print(f"Executing {args.display}, last input was {last_input}")

if args.display == str(0):
    all_off()
elif args.display == str(1):
    turn(ON)
elif args.display == str(2):
    brake_1(ON)
elif args.display == str(3):
    brake_2(ON)
elif args.display == str(4):
    rev(ON)
elif args.display == str(5):
    license_1(ON)
elif args.display == str(6):
    license_2(ON)
elif args.display == str(7):
    move()
elif args.display == str(8):
    wave()
elif args.display == str(9):
    flash()
elif args.display == "*":
    alt_flash()
elif args.display == "#":
    pulse()

elif args.display == "#" and last_input == "#":
    os.system("reboot")
