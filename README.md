# Foosball LED Lights
Python 3 code for motion sensor activated LED lights on a Foosball table

This code is for a Raspberry Pi 3 running raspbian.

### Wiring
Wiring was done with a breadboard and a raspberry pi 3.
Wiring descriptions for the lights can be found [here](https://dordnung.de/raspberrypi-ledstrip/)

Wiring descriptions for the motion sensors can be found [here](https://diyhacking.com/raspberry-pi-gpio-control/)

The wiring for both were done on the same breadboard, no need to edit either one of the wiring diagrams to fit the other, they should work fine side by side.


 The program will need to use the pigpio library for the LED lights.
 To download if your Raspberry Pi does not have pigpio (most should come preinstalled) follow [these steps](http://abyz.me.uk/rpi/pigpio/download.html)
  
 ### Running the program:
Running the program requies that the pigpio deamon is running, to do this, type `sudo pigpiod`. You are now able to run your program.
