This project was used to create a 6 light (2 spots are doubled up, so 8 technically) light show with a keypad for input on which show to run.

The following products were purchased for a Raspbery Pi 2 Model B:
 - 1 x Super Bright White 5mm LED (25 pack) [adafruit.com](https://www.adafruit.com/product/754)
 - 2 x Pig-Tail Cables - 0.1" 2-pin - 4 Pack [adafruit.com](https://www.adafruit.com/product/1003)
 - 1 x Adafruit 24-Channel 12-bit PWM LED Driver - SPI Interface (TLC5947) [adafruit.com](https://www.adafruit.com/product/1429)
 - 1 x 3x4 Phone-style Matrix Keypad [adafruit.com](https://www.adafruit.com/product/1824)
 - 1 x Half-size breadboard [adafruit.com](https://www.adafruit.com/product/64)

Wiring followed https://learn.adafruit.com/tlc5947-tlc59711-pwm-led-driver-breakout and https://learn.adafruit.com/matrix-keypad/pinouts

I moved the GPIO5 pin for the LED Driver up one pin to the GPIO0 spot.

To auto boot the RPI into the program, I followed the instructions here: https://raspberrytips.com/which-raspberry-pi-os-is-running/

```
pi@rpi-supralights:~ $ sudo cat /etc/xdg/autostart/lights.desktop
[Desktop Entry]

Name=SupraLights
Exec=/usr/bin/python3 /home/pi/keypad.py
```
