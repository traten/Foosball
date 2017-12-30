# -----------------------------------------------------
 # File        fus2.py
 # Authors     Trevor Aten
 # License     GPLv3
 # -----------------------------------------------------
 #
 # Copyright (C) 2014-2017 Trevor Aten
 #
 # This program is free software: you can redistribute it and/or modify
 # it under the terms of the GNU General Public License as published by
 # the Free Software Foundation, either version 3 of the License, or
 # any later version.
 #
 # This program is distributed in the hope that it will be useful,
 # but WITHOUT ANY WARRANTY; without even the implied warranty of
 # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 # GNU General Public License for more details.
 #
 # You should have received a copy of the GNU General Public License
 # along with this program. If not, see <http://www.gnu.org/licenses/>
#
import sys
import RPi.GPIO as GPIO;
GPIO.setmode(GPIO.BCM);
import time;
import pigpio;
pi = pigpio.pi();
#=====define variables======
motionSensorWhite = 17;
motionSensorBlack= 27;
redLight = 21;
blueLight = 16;
greenLight = 19;
GPIO.setup(motionSensorWhite, GPIO.IN);
GPIO.setup(motionSensorBlack, GPIO.IN);
blinkTime = 40;
solidTime = 3;
count = 0;
rB = 0;
gB = 0;
bB = 0;

#=======Define all Colors========
#sets RGB codes for all colors
def red():
    pi.set_PWM_dutycycle(redLight, 255);
    pi.set_PWM_dutycycle(greenLight, 0);
    pi.set_PWM_dutycycle(blueLight, 0);

def green():
    pi.set_PWM_dutycycle(redLight, 0);
    pi.set_PWM_dutycycle(greenLight, 255);
    pi.set_PWM_dutycycle(blueLight, 0);

def blue():
    pi.set_PWM_dutycycle(redLight, 0);
    pi.set_PWM_dutycycle(greenLight, 0);
    pi.set_PWM_dutycycle(blueLight, 255);

def black():
    pi.set_PWM_dutycycle(redLight, 0);
    pi.set_PWM_dutycycle(greenLight, 0);
    pi.set_PWM_dutycycle(blueLight, 0);

def purple():
    pi.set_PWM_dutycycle(redLight, 160);
    pi.set_PWM_dutycycle(greenLight, 32);
    pi.set_PWM_dutycycle(blueLight, 240);

def ultramarineBlue():
    pi.set_PWM_dutycycle(redLight, 72);
    pi.set_PWM_dutycycle(greenLight, 117);
    pi.set_PWM_dutycycle(blueLight, 240);

def neonGreen():
    pi.set_PWM_dutycycle(redLight, 43);
    pi.set_PWM_dutycycle(greenLight, 240);
    pi.set_PWM_dutycycle(blueLight, 36);

def pear():
    pi.set_PWM_dutycycle(redLight, 220);
    pi.set_PWM_dutycycle(greenLight, 240);
    pi.set_PWM_dutycycle(blueLight, 36);

def lavIndigo():
    pi.set_PWM_dutycycle(redLight, 183);
    pi.set_PWM_dutycycle(greenLight, 74);
    pi.set_PWM_dutycycle(blueLight, 255);

def cerisePink():
    pi.set_PWM_dutycycle(redLight, 255);
    pi.set_PWM_dutycycle(greenLight, 48);
    pi.set_PWM_dutycycle(blueLight, 131);

def colalRed():
    pi.set_PWM_dutycycle(redLight, 255);
    pi.set_PWM_dutycycle(greenLight, 51);
    pi.set_PWM_dutycycle(blueLight, 71);

def electricBlue():
    pi.set_PWM_dutycycle(redLight, 79);
    pi.set_PWM_dutycycle(greenLight, 255);
    pi.set_PWM_dutycycle(blueLight, 249);

def gatorOrange():
    pi.set_PWM_dutycycle(redLight, 250);
    pi.set_PWM_dutycycle(greenLight, 70);
    pi.set_PWM_dutycycle(blueLight, 22);

def gatorBlue():
    pi.set_PWM_dutycycle(redLight, 0);
    pi.set_PWM_dutycycle(greenLight, 33);
    pi.set_PWM_dutycycle(blueLight, 165);


#this function does not work and is not in use
#=========blink()==========
#takes in color method and length of time for blinking
#Blinks for user set time, and then color stays solid
#for user set amount of time
def blink(color,blinkTime,solidTime):
    for x in range(0,blinkTime):
        print("purple");
        color;
        time.sleep(.05);
        black();
        time.sleep(.05);
    print("what")
    color;
    time.sleep(solidTime);
    black();
    time.sleep(.05);
    time.sleep(7);


#==========fadeColor()=============
#helper method for the fade function
def fadeColor(redMax,greenMax,blueMax):
    global rB;
    global gB;
    global bB;
    while(rB != redMax or gB != greenMax or bB != blueMax):
        pi.set_PWM_dutycycle(redLight, rB);
        pi.set_PWM_dutycycle(greenLight, gB);
        pi.set_PWM_dutycycle(blueLight, bB);
        if(rB < redMax):
            rB+=1;
        if(gB < greenMax):
            gB+=1;
        if(bB < blueMax):
            bB+=1;
        time.sleep(.03);
        if(rB == redMax and gB == greenMax and bB == blueMax):
            time.sleep(2);
    while(rB != 0 or gB != 0 or bB != 0):
        if(rB > 0):
            rB-=1;
        if(gB > 0):
            gB-=1;
        if(bB > 0):
            bB-=1;
        pi.set_PWM_dutycycle(redLight, rB);
        pi.set_PWM_dutycycle(greenLight, gB);
        pi.set_PWM_dutycycle(blueLight, bB);
        time.sleep(.02);

#===========fade()========
def fade():
    while True:
        #fade for red
        fadeColor(255,0,0);
        #fade for blue
        fadeColor(0,0,255);
        #fade for green
        fadeColor(0,255,0);
        #fade for purple
        fadeColor(160,32,240);
        #fade for ultramarineBlue
        fadeColor(72,117,240);
        #fade for neonGreen
        fadeColor(43,240,36);
        #fade for pear
        fadeColor(220,240,36);
        #fade for lavIndigo
        fadeColor(183,74,255);
        #fade for cerisePink
        fadeColor(255,48,131);
        #fade for colalRed
        fadeColor(255,51,71);
        #fade for electricBlue
        fadeColor(79,255,249);
        #fade for gatorOrange
        fadeColor(250,70,22);
        #fade for gatorBlue
        fadeColor(0,33,165);



#=========Game implemintation===========
#waits for motion sensors to be set off in constant while loop
try:
    print("\n");
    print("*************************");
    print("WELCOME TO FOOSBALL LEDS:");
    print("*************************");
    while True:
        try:
            print("Please type in the number of the setting you would like:");
            print("(1)Foosball Game");
            print("(2)Fade");
            userSelction = int(input("Selction: "));
        except ValueError:
            print("Invalid input select 1 or 2");
            continue
        else:
            if(userSelction == 1):
                print("Game Mode Started");
                while True:
                    i=GPIO.input(motionSensorWhite);
                    j=GPIO.input(motionSensorBlack);
                    if count > 3000:
                        print("sleep");
                        while(i == 0 or j == 0):
                            fade();
                        count = 0;
                    else:
                        if i==0: #motionSensorWhite OFF
                            time.sleep(0.1);
                        elif i==1: #motionSensorWhite ON
                            count = 0;
                            for x in range(0,blinkTime):
                                neonGreen(); #HERE TO CHANGE COLOR
                                time.sleep(.05);
                                black();
                                time.sleep(.05);
                            neonGreen(); #HERE TO CHANGE COLOR
                            time.sleep(solidTime);
                            black();
                            time.sleep(.05);
                            time.sleep(7);
                        if j==0: #motionSensorBlack OFF
                            time.sleep(0.1);
                        elif j==1: #motionSensorBlack ON
                            count = 0;
                            for x in range(0,blinkTime):
                                gatorBlue(); #HERE TO CHANGE COLOR
                                time.sleep(.05);
                                black();
                                time.sleep(.05);
                            gatorBlue(); #HERE TO CHANGE COLOR
                            time.sleep(solidTime);
                            black();
                            time.sleep(.05);
                            time.sleep(7);
                        count = count+1;
                        print(count);
            if(userSelction == 2):
                print("Fade Started")
                fade();
finally:
    #turn all lights off upon exiting program
    black();
    GPIO.cleanup()
    pi.stop()
    print("PROGRAM SHUTDOWN\n");
