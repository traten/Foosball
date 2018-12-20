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
motionSensorWhite = 17; #GPIO pin used for "white" motion sensor
motionSensorBlack= 27; #GPIO pin used for "black" motion sensor
redLight = 21; #GPIO pin used for red RGB light
blueLight = 16; #GPIO pin used for blue RGB light
greenLight = 19; #GPIO pin used for green RGB light
GPIO.setup(motionSensorWhite, GPIO.IN); #set "white" motion sensor as input pin
GPIO.setup(motionSensorBlack, GPIO.IN); #set "black" motion sensor as input pin
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

#colorSet(r,g,b)
#defines color taking in decimal number of each rgb code
def colorSet(r,g,b):
    pi.set_PWM_dutycycle(redLight, r);
    pi.set_PWM_dutycycle(greenLight, g);
    pi.set_PWM_dutycycle(blueLight, b);

#========colorPicker()========
#user based color selector
#will define the RGB code of the color
def colorPicker(colNum):
    if(colNum == "0"): #CUSTOM COLOR
        return custColor();
    else:
        foosMenu = open("foosMenu.txt","r");
        colorList = [];
        for line in foosMenu:
            colorList.append(line);
        foosMenu.close();
        colorList_Length = len(colorList);
        for x in range(colorList_Length):
            if(colorList[x] == '{}\n'.format(colNum)):
                selColor = colorList[x+2];
        print(selColor);
        return selColor;

#========updateDataBase()========
#updates database based on new entries
def updateDataBase():
    foosMenu = open("foosMenu.txt","r+");
    numOfEntriesInDataBase = int(foosMenu.readline());
    numOfEntriesInDataBase += 1;
    data = foosMenu.readlines();
    data[0] = '{}\n'.format(numOfEntriesInDataBase);
    foosMenu.close();
    foosMenu = open("foosMenu.txt","r+");
    for x in range(len(data)):
        foosMenu.write('{}' .format(data[x]));
    foosMenu.close();
    return numOfEntriesInDataBase

#======cust_color=======
#User inputed RGB values
def custColor():
    colorValueR = (input("Enter Red Value: "));
    colorValueG = (input("Enter Green Value: "));
    colorValueB = (input("Enter Blue Value: "));
    colorName = (input("Enter color Name: "));
    numOfEntriesInDataBase = updateDataBase(); #update the database to hold new color combo
    foosMenu = open("foosMenu.txt","a");
    foosMenu.write('{}\n'.format(numOfEntriesInDataBase))
    foosMenu.write('{}\n'.format(colorName));
    foosMenu.write('{}\n'.format(colorValueR + ' ' + colorValueG + ' ' + colorValueB));
    foosMenu.close();
    colorSelection = colorValueR + ' ' + colorValueG + ' ' + colorValueB;
    return colorSelection;

#======menu()========
#menu for colors
def menu():
    foosMenu = open("foosMenu.txt", "r");
    i = 0;
    for j, line in enumerate(foosMenu, start=0):
        if j % 3 == 2:
            line = line.rstrip('\n')
            print("({}): " .format(i) + line);
            i += 1;

#==========strobeColor()=============
#helper method for the strobe function
def strobeColor(red,green,blue):
    for x in range(0,10):
        colorSet(red,green,blue);
        time.sleep(.05)
        colorSet(0,0,0);
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
        colorSet(rB,gB,bB);
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
        colorSet(rB,gB,bB);
        time.sleep(.01);

#========fadeColorGame()==========
#fades Color that allows for motion sensor disruptance that will cancel the fade
def fadeColorGame(redMax,greenMax,blueMax):
    global rB;
    global gB;
    global bB;
    while(rB != redMax or gB != greenMax or bB != blueMax):
        if(motionInterupt() == True):
            return False;
        else:
            colorSet(rB,gB,bB);
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
            colorSet(rB,gB,bB);
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

#=======SolidColor()========
#displays a solid color until exit is typed or program is termninated
def SolidColor():
    menu();
    userInput = input("Enter the number of the Color you want: "); #solid color that will be displayed
    while True:
        solidColor = colorPicker(userInput).split();
        colorSet(solidColor[0], solidColor[1], solidColor[2])
        exit = input('type exit to return to menu: ');
        print(exit);
        if(exit == "exit"):
            black(); #turn off solid color
            break;

#=======motionInterupt()=======
#function that returns true if either of the motion sensors go off
#this function is used to allow for disruptance in sleep mode
def motionInterupt():
    if(GPIO.input(motionSensorWhite) == 1 or GPIO.input(motionSensorBlack) == 1):
        black();
        return True;
    else:
        return False;

#=======fadeInGame()=========
#fade that will allow for motion sensor disruptance
#to terminate the sleep mode that is activated after about 10mins
#of no activity
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
    while(True):
        print("Game Mode Selected");
        player1 = input("Enter Player One's Name (White): ");
        menu();
        player1Col = input('Enter {}\'s Color (number from menu): '.format(player1)); #ask for player1s color
        PlayerOneColor = colorPicker(player1Col).split(); #split player ones color into rgb values
        player2 = input("Enter Player Two's Name (Black): ");
        player2Col = input('Enter {}\'s (number from menu): ' .format(player2)); #ask for player 2s color
        PlayerTwoColor = colorPicker(player2Col).split(); #split player ones color into rgb values
        print("******Game Started******");
        print('{}\'s SCORE: {}'.format(player1,whiteScore));
        print('{}\'s SCORE: {}'.format(player2,blackScore));
        while True:
            i=GPIO.input(motionSensorWhite); #motion sensor on black goal (white scores on)
            j=GPIO.input(motionSensorBlack); #motion sensor on white goal (black scores on)
            if count > 3000: #wait around 10mins
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
                            colorPicker(player1Col);
                            time.sleep(.05);
                            black();
                            time.sleep(.05);
                        colorPicker(player1Col);
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
                    count = 0; #reset count so sleep mode does not activate
                    time.sleep(.05);
                    time.sleep(5); #give the user time to take the ball out of the goal without setting off the motion sensor
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
                        print('{} is the winner!'.format(player2));
                        strobe();
                        break;
                    count = 0; #reset count so sleep mode does not activate
                    time.sleep(.05);
                    time.sleep(5); #give the user time to take the ball out of the goal without setting off the motion sensor
                count+=1; #update count to check for sleep mode

#=======gameModeLite()=======``
#runs game mode that has less features than regurlar game mode
#doesn't allow for score keeping, user input, or special lights upon winning
#this in theory will streamline speed for motion sensors to provide for more accurate readings
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
                    colorPicker("6");
                    time.sleep(.05);
                    black();
                    time.sleep(.05);
                colorPicker("6"); #CHANGE PLAYER COLOR HERE
                time.sleep(solidTime);
                black();
                time.sleep(.05);
                time.sleep(5);
            if j==0: #motionSensorBlack OFF
                time.sleep(0.1);
            elif j==1: #motionSensorBlack ON
                count = 0;
                for x in range(0,blinkTime):
                    colorPicker("11"); #CHANGE PLAYER COLOR HERE
                    time.sleep(.05);
                    black();
                    time.sleep(.05);
                colorPicker("11");
                time.sleep(solidTime);
                black();
                time.sleep(.05);
                time.sleep(5);
            count+=1;

#=========Foosball Modes===========
#list of options for program
#This screen prompts you upon opening up application
try:
    strobeColor(255, 0, 0) #Red strobe to alert players game is back on
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
            userSelection = int(input("Selection: "));
        except ValueError:
            print("Invalid input select 1,2,3, or 4");
            continue
        else:
            if(userSelection == 1):
                gameMode();
            if(userSelection == 2):
                gameModeLite();
            if(userSelection == 3):
                print("Fade Started");
                fade();
            if(userSelection == 4):
                print("Solid Color Started");
                SolidColor();
finally:
    #turn all lights off upon exiting program
    black();
    GPIO.cleanup()
    pi.stop()
    print("PROGRAM SHUTDOWN\n");
