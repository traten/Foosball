# Foosball
Python code for motion sensor activated led lights on a Foosball table

This code is for a raspberry pi running raspbian.

Wiring was done with a breadboard and a raspberry pi 3.
Wiring descriptions for the lights can be found here:
https://dordnung.de/raspberrypi-ledstrip/

Wiring descriptions for the motion sensors can be found here:
https://diyhacking.com/raspberry-pi-gpio-control/

The wiring for both were done on the same breadboard, no need to edit either one of the wiring diagrams to fit the other, they should work fine side by side.


 The program will need to use the pigpio library for the LED lights
 To download if your raspberry pi does not have pigpio (most should come preinstalled) follow these steps:
 http://abyz.me.uk/rpi/pigpio/download.html
  
 Running the program:
 open terminal and type: sudo pigpiod //this will start the pigpio deamon
 then you are able to run your program
