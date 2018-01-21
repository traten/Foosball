# MIT License
#
# Copyright (c) 2017 Trevor Aten
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

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
whiteScore = 0;
blackScore = 0;

#=====black()======
#defines a lightless color
def black():
    pi.set_PWM_dutycycle(redLight, 0);
    pi.set_PWM_dutycycle(greenLight, 0);
    pi.set_PWM_dutycycle(blueLight, 0);

#========colorPicker()========
#user based color selector
#will define the RGB code of the color
def colorPicker(colNum):
    if(colNum == "1"): #red
        pi.set_PWM_dutycycle(redLight, 255);
        pi.set_PWM_dutycycle(greenLight, 0);
        pi.set_PWM_dutycycle(blueLight, 0);
    elif(colNum == "2"): #blue
        pi.set_PWM_dutycycle(redLight, 0);
        pi.set_PWM_dutycycle(greenLight, 0);
        pi.set_PWM_dutycycle(blueLight, 255);
    elif(colNum == "3"): #green
        pi.set_PWM_dutycycle(redLight, 0);
        pi.set_PWM_dutycycle(greenLight, 255);
        pi.set_PWM_dutycycle(blueLight, 0);
    elif(colNum == "4"): #purple
        pi.set_PWM_dutycycle(redLight, 160);
        pi.set_PWM_dutycycle(greenLight, 32);
        pi.set_PWM_dutycycle(blueLight, 240);
    elif(colNum == "5"): #Ultramirine Blue
        pi.set_PWM_dutycycle(redLight, 72);
        pi.set_PWM_dutycycle(greenLight, 117);
        pi.set_PWM_dutycycle(blueLight, 240);
    elif(colNum == "6"): #Neon Green
        pi.set_PWM_dutycycle(redLight, 43);
        pi.set_PWM_dutycycle(greenLight, 240);
        pi.set_PWM_dutycycle(blueLight, 36);
    elif(colNum == "7"): #Pear
        pi.set_PWM_dutycycle(redLight, 220);
        pi.set_PWM_dutycycle(greenLight, 240);
        pi.set_PWM_dutycycle(blueLight, 36);
    elif(colNum == "8"): #Lavender Indigo
        pi.set_PWM_dutycycle(redLight, 183);
        pi.set_PWM_dutycycle(greenLight, 74);
        pi.set_PWM_dutycycle(blueLight, 255);
    elif(colNum == "9"): #cerise Pinke
        pi.set_PWM_dutycycle(redLight, 255);
        pi.set_PWM_dutycycle(greenLight, 48);
        pi.set_PWM_dutycycle(blueLight, 131);
    elif(colNum == "10"): #coral Red
        pi.set_PWM_dutycycle(redLight, 255);
        pi.set_PWM_dutycycle(greenLight, 51);
        pi.set_PWM_dutycycle(blueLight, 71);
    elif(colNum == "11"): #electric blueLight
        pi.set_PWM_dutycycle(redLight, 79);
        pi.set_PWM_dutycycle(greenLight, 255);
        pi.set_PWM_dutycycle(blueLight, 249);
    elif(colNum == "12"): #gator orange
        pi.set_PWM_dutycycle(redLight, 255);
        pi.set_PWM_dutycycle(greenLight, 100);
        pi.set_PWM_dutycycle(blueLight, 0);
    elif(colNum == "13"): #gator blue
        pi.set_PWM_dutycycle(redLight, 0);
        pi.set_PWM_dutycycle(greenLight, 33);
        pi.set_PWM_dutycycle(blueLight, 165);
    if(colNum == "14"): #Police Lights
        pi.set_PWM_dutycycle(redLight, 255);
        pi.set_PWM_dutycycle(greenLight, 0);
        pi.set_PWM_dutycycle(blueLight, 0);
        time.sleep(.08);
        pi.set_PWM_dutycycle(redLight, 0);
        pi.set_PWM_dutycycle(greenLight, 0);
        pi.set_PWM_dutycycle(blueLight, 255);
    if(colNum == "15"): #Gator Falshing
        pi.set_PWM_dutycycle(redLight, 255);
        pi.set_PWM_dutycycle(greenLight, 100);
        pi.set_PWM_dutycycle(blueLight, 0);
        time.sleep(.08);
        pi.set_PWM_dutycycle(redLight, 79);
        pi.set_PWM_dutycycle(greenLight, 255);
        pi.set_PWM_dutycycle(blueLight, 249);

#======menu()========
#menu for colors
def menu():
    print("(1): RED");
    print("(2): BLUE");
    print("(3): GREEN");
    print("(4): PURPLE");
    print("(5): ULTRAMARINE BlUE");
    print("(6): NEON GREEN");
    print("(7): PEAR");
    print("(8): LAVENDER INDIGO");
    print("(9): CERISE PINK");
    print("(10): CORAL RED");
    print("(11): ELECTRIC BLUE");
    print("(12): GATOR ORANGE");
    print("(13): GATOR BLUE");
    print("(14): POLICE LIGHTS");
    print("(15): GATOR FLASHING");

#==========strobeColor()=============
#helper method for the strobe function
def strobeColor(red,green,blue):
    for x in range(0,10):
        pi.set_PWM_dutycycle(redLight, red);
        pi.set_PWM_dutycycle(greenLight, green);
        pi.set_PWM_dutycycle(blueLight, blue);
        time.sleep(.05)
        pi.set_PWM_dutycycle(redLight, 0);
        pi.set_PWM_dutycycle(greenLight, 0);
        pi.set_PWM_dutycycle(blueLight, 0);
        time.sleep(.05)

#======strobe()======
#strobe function that strobes each color
#rototates through all color listed
def strobe():
    #strobe for red
    strobeColor(255,0,0);
    #strobe for blue
    strobeColor(0,0,255);
    #strobe for green
    strobeColor(0,255,0);
    #strobe for purple
    strobeColor(160,32,240);
    #strobe for ultramarineBlue
    strobeColor(72,117,240);
    #strobe for neonGreen
    strobeColor(43,240,36);
    #strobe for pear
    strobeColor(220,240,36);
    #strobe for lavIndigo
    strobeColor(183,74,255);
    #strobe for cerisePink
    strobeColor(255,48,131);
    #strobe for coralRed
    strobeColor(255,51,71);
    #strobe for electricBlue
    strobeColor(79,255,249);
    #strobe for gatorOrange
    strobeColor(250,70,22);
    #strobe for gatorBlue
    strobeColor(0,33,165);

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
        time.sleep(.02);
        if(rB == redMax and gB == greenMax and bB == blueMax):
            time.sleep(3);
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
        time.sleep(.01);

#========fadeColorGame()==========
#fades Color that allows for motion sensor disruptance that will cancle the fade
def fadeColorGame(redMax,greenMax,blueMax):
    global rB;
    global gB;
    global bB;
    while(rB != redMax or gB != greenMax or bB != blueMax):
        if(motionInterupt() == True):
            return False;
        else:
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
        if(motionInterupt() == True):
            return False;
        else:
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
#fades the colors listed below
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
        #fade for coralRed
        fadeColor(255,51,71);
        #fade for electricBlue
        fadeColor(79,255,249);
        #fade for gatorOrange
        fadeColor(250,70,22);
        #fade for gatorBlue
        fadeColor(0,33,165);

#=======stationary()========
def stationary():
    menu();
    userInput = input("Enter the number of the Color you want: ");
    while True:
        colorPicker(userInput);
        exit == input("type exit to quit: ");
        if(exit == "exit"):
            break;

#=======motionInterupt()=======
#function that returns true if either of the motion sensors go off
def motionInterupt():
    if(GPIO.input(motionSensorWhite) == 1 or GPIO.input(motionSensorBlack) == 1):
        black();
        return True;
    else:
        return False;

#=======fadeInGame()=========
#fade that will allow for motion sensor disruptance
def fadeInGame():
    while(True):
        #fade for red
        if(fadeColorGame(255,0,0) == False):
            break;
        #fade for blue
        if(fadeColorGame(0,0,255) == False):
            break;
        #fade for green
        if(fadeColorGame(0,255,0) == False):
            break;
        #fade for purple
        if(fadeColorGame(160,32,240) == False):
            break;
        #fade for ultramarineBlue
        if(fadeColorGame(72,117,240) == False):
            break;
        #fade for neonGreen
        if(fadeColorGame(43,240,36) == False):
            break;
        #fade for pear
        if(fadeColorGame(220,240,36) == False):
            break;
        #fade for lavIndigo
        if(fadeColorGame(183,74,255) == False):
            break;
        #fade for cerisePink
        if(fadeColorGame(255,48,131) == False):
            break;
        #fade for coralRed
        if(fadeColorGame(255,51,71) == False):
            break;
        #fade for electricBlue
        if(fadeColorGame(79,255,249) == False):
            break;
        #fade for gatorOrange
        if(fadeColorGame(250,70,22) == False):
            break;
        #fade for gatorBlue
        if(fadeColorGame(0,33,165) == False):
            break;

#=========gameMode()==========
#function that runs the game mode
def gameMode():
    global count;
    global whiteScore;
    global blackScore;
    over = False;
    while(True):
        print("Game Mode Selected");
        player1 = input("Enter Player One's Name (White): ");
        menu();
        player1Col = input('Enter {}\'s Color (number from menu): '.format(player1));
        player2 = input("Enter Player Two's Name (Black): ");
        #menu();
        player2Col = input('Enter {}\'s (number from menu): ' .format(player2));
        print("******Game Started******");
        print('{}\'s SCORE: {}'.format(player1,whiteScore));
        print('{}\'s SCORE: {}'.format(player2,blackScore));
        while True:
            i=GPIO.input(motionSensorWhite); #motion sensor on black goal (white scores on)
            j=GPIO.input(motionSensorBlack); #motion sensor on white goal (black scores on)
            if count > 3000:
                print("Sleep Mode(Activate Motion Sensor to continue)");
                fadeInGame();
                print("Game Resumed")
                strobeColor(255,0,0); #Red strobe to alert players game is back on
                time.sleep(5);
                count = 0;
            else:
                if i==0: #motionSensorWhite OFF
                    time.sleep(0.1);
                elif i==1: #motionSensorWhite ON
                    if(whiteScore < 9):
                        for x in range(0,blinkTime):
                            colorPicker(player1Col); #HERE TO CHANGE COLOR
                            time.sleep(.05);
                            black();
                            time.sleep(.05);
                        colorPicker(player1Col); #HERE TO CHANGE COLOR
                        time.sleep(solidTime);
                        black();
                        #update score
                        whiteScore += 1;
                        print('{}\'s SCORE: {}'.format(player1,whiteScore));
                        print('{}\'s SCORE: {}'.format(player2,blackScore));
                    else:
                        print(player1," is the winner!");
                        strobe();
                        break;
                    count = 0;
                    time.sleep(.05);
                    time.sleep(7);
                if j==0: #motionSensorBlack OFF
                    time.sleep(0.1);
                elif j==1: #motionSensorBlack ON
                    if(blackScore < 9):
                        for x in range(0,blinkTime):
                            colorPicker(player2Col); #HERE TO CHANGE COLOR
                            time.sleep(.05);
                            black();
                            time.sleep(.05);
                        colorPicker(player2Col); #HERE TO CHANGE COLOR
                        time.sleep(solidTime);
                        black();
                        #update score
                        blackScore += 1;
                        print('{}\'s SCORE: {}'.format(player1,whiteScore));
                        print('{}\'s SCORE: {}'.format(player2,blackScore));
                    else:
                        print('{} is the winner!'.formate(player2));
                        strobe();
                        break;
                    count = 0;
                    time.sleep(.05);
                    time.sleep(7);
                count+=1;

#=======gameModeLite()=======
#runs game mode that has less features than regurlar game mode
#doesn't allow for score keeping, user input, or special lights upon winning
def gameModeLite():
    global count;
    print("Game Mode Lite Started");
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
                    colorPicker(6);
                    time.sleep(.05);
                    black();
                    time.sleep(.05);
                colorPicker(6);
                time.sleep(solidTime);
                black();
                time.sleep(.05);
                time.sleep(7);
            if j==0: #motionSensorBlack OFF
                time.sleep(0.1);
            elif j==1: #motionSensorBlack ON
                count = 0;
                for x in range(0,blinkTime):
                    colorPicker(11);
                    time.sleep(.05);
                    black();
                    time.sleep(.05);
                colorPicker(11);
                time.sleep(solidTime);
                black();
                time.sleep(.05);
                time.sleep(7);
            count+=1;

#=========Foosball Modes===========
#list of options for program
try:
    print("\n");
    print("*************************");
    print("WELCOME TO FOOSBALL LEDS:");
    print("*************************");
    while True:
        try:
            print("Please type in the number of the setting you would like:");
            print("(1)Foosball Game");
            print("(2)Foosball Game Lite"); #quicker motion sensors, no score and no winning lights
            print("(3)Fade");
            print("(4)Solid Color");
            userSelection = int(input("Selction: "));
        except ValueError:
            print("Invalid input select 1,2,3, or 4");
            continue
        else:
            if(userSelection == 1):
                gameMode();
            if(userSelection == 2):
                gameModeLite();
            if(userSelection == 3):
                print("Fade Started")
                fade();
            if(userSelection == 4):
                print("Solid Color Started")
                stationary();
finally:
    #turn all lights off upon exiting program
    black();
    GPIO.cleanup()
    pi.stop()
    print("PROGRAM SHUTDOWN\n");
