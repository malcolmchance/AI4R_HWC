#!/usr/bin/python

################################################################################
# Import Statements 
################################################################################
import time
import sys

#-------------------------------------------------------------------------------
# Uncomment for used with Raspberry Pi Board
#-------------------------------------------------------------------------------
# import RPi.GPIO as GPIO
# import RaspberryPiPortSetup as PiPort # imports RPi.GPIO as GPIO

#-------------------------------------------------------------------------------
# Uncomment for used with Raspberry Pi Simulator
#-------------------------------------------------------------------------------
import RaspberryPiPortSetupSim as PiPort # imports RPi.GPIO as GPIO

#-------------------------------------------------------------------------------
# Enable or disable debug print statements. Set 'debug = True' to enable
#-------------------------------------------------------------------------------
global debug
debug = True

#-------------------------------------------------------------------------------
# Initialize ports and set all output ports state to low.
#-------------------------------------------------------------------------------
PiPort.initializeIO()
PiPort.setAllOutputsLow()
inputState = [False, False, False,False]

################################################################################
# Create Array of LED States
################################################################################


#------------------------------------------------------------------------------
# LED Number    |  1  |  2   |  3   |  4   |  5   |  6   |  7   |  8   |  9   |
# --------------|-----|------|------|------|------|------|------|------|------|
LEDTestArray1 = ["ON" , "ON" , "OFF", "OFF", "OFF", "OFF","OFF" ,"OFF" ,"OFF" ]
LEDTestArray2 = ["OFF", "ON" , "ON" , "OFF", "OFF", "OFF", "OFF", "OFF","OFF" ]
LEDTestArray3 = ["OFF", "OFF", "ON" , "ON" , "OFF", "OFF", "OFF", "OFF", "OFF"]
LEDTestArray4 = ["OFF", "OFF", "OFF", "ON" , "ON" , "OFF", "OFF", "OFF", "OFF"]
LEDTestArray5 = ["OFF", "OFF", "OFF", "OFF", "ON" , "ON" , "OFF", "OFF", "OFF"]
LEDTestArray6 = ["OFF", "OFF", "OFF", "OFF", "OFF", "ON" , "ON" , "OFF", "OFF"]
LEDTestArray7 = ["OFF", "OFF", "OFF", "OFF", "OFF", "OFF", "ON" , "ON" , "OFF"]
LEDTestArray8 = ["OFF", "OFF", "OFF", "OFF", "OFF", "OFF", "OFF", "ON" , "ON" ]

arrayOfArrays = [LEDTestArray1,
                 LEDTestArray2,
                 LEDTestArray3,
                 LEDTestArray4,
                 LEDTestArray5,
                 LEDTestArray6,
                 LEDTestArray7,
                 LEDTestArray8,
                 LEDTestArray7,
                 LEDTestArray6,
                 LEDTestArray5,
                 LEDTestArray4,
                 LEDTestArray3,
                 LEDTestArray2]

################################################################################
# End Create Array of LED States
################################################################################

try:
    
    ledArrayRef = 0
    arrayLength = len(arrayOfArrays)
    global continueToRun
    continueToRun = True
    while continueToRun:      

        counter = 0
        while counter < arrayLength:
            
            PiPort.setOutputArray(arrayOfArrays[ledArrayRef])
            counter += 1

            if PiPort.checkInput()[0]:
                ledArrayRef += 1
                ledArrayRef %= 14

            if PiPort.checkInput()[1] == False:
                continueToRun = False
                #break
                sys.exit()
                
            time.sleep(0.04)


except Exception:
    if debug:
        print "exception generated and caught"



