#!/usr/bin/python

################################################################################
# Import Statements 
################################################################################
import time

#-------------------------------------------------------------------------------
# Uncomment for used with Raspberry Pi Board
#-------------------------------------------------------------------------------
#import RPi.GPIO as GPIO
#GPIO.setmode(GPIO.BOARD)
#import RaspberryPiPortSetup as PiPort # imports RPi.GPIO as GPIO

#-------------------------------------------------------------------------------
# Uncomment for used with Raspberry Pi Simulator
#-------------------------------------------------------------------------------
#import RaspberryPiPortSetupSim as PiPort # imports RPi.GPIO as GPIO
import RaspberryPiPortSetup as PiPort # imports RPi.GPIO as GPIO

#-------------------------------------------------------------------------------
# Enable or disable debug print statements. Set 'debug = True' to enable
#-------------------------------------------------------------------------------
global debug
debug = False

#-------------------------------------------------------------------------------
# Initialize ports and set all output ports state to low.
#-------------------------------------------------------------------------------
PiPort.initializeIO()
PiPort.setAllOutputsLow()
inputState = [False, False, False,False]

################################################################################
# Create Array of LED States
################################################################################

###------------------------------------------------------------------------------
### LED Number    |  1  |  2   |  3   |  4   |  5   |  6   |  7   |  8   |  9   |
### --------------|-----|------|------|------|------|------|------|------|------|
##LEDTestArray1 = ["ON" , "ON" , "ON" , "ON" , "ON" , "ON" , "ON" , "ON" , "ON" ]
##LEDTestArray2 = ["ON" , "OFF", "ON" , "OFF", "ON" , "OFF", "ON" , "OFF", "ON" ]
##LEDTestArray3 = ["OFF", "ON" , "OFF", "ON" , "OFF", "ON" , "OFF", "ON ", "OFF"]
##LEDTestArray4 = ["OFF", "OFF", "OFF", "OFF", "OFF", "OFF", "OFF", "OFF", "OFF"]

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
#    while True:
#            PiPort.setAllOutputsHigh()
#            time.sleep(.5)
            PiPort.setAllOutputsLow()
#            time.sleep(.5)
        ##    PiPort.setOutput(3, "on")
        ##    time.sleep(0.1)
        ##    PiPort.setOutput(5, "ON")
        ##    time.sleep(0.1)
        ##    PiPort.setOutput(7, "on")
        ##    time.sleep(0.1)
        ##    PiPort.setOutput(11, "on")
        ##    time.sleep(0.1)
        ##    PiPort.setOutput(13, "on")
        ##    time.sleep(0.1)
        ##    PiPort.setOutput(15, "on")
        ##    time.sleep(0.1)
        ##    PiPort.setOutput(19, "on")
        ##    time.sleep(0.1)
        ##    PiPort.setOutput(21, "on")
        ##    time.sleep(0.1)
        ##    PiPort.setOutput(23, "on")
        ##    time.sleep(0.1)
        ##
        ##    PiPort.setMappedOutput(1, "off")
        ##    time.sleep(0.1)
        ##    PiPort.setMappedOutput(2, "off")
        ##    time.sleep(0.1)
        ##    PiPort.setMappedOutput(3, "off")
        ##    time.sleep(0.1)
        ##    PiPort.setMappedOutput(4, "off")
        ##    time.sleep(0.1)
        ##    PiPort.setMappedOutput(5, "off")
        ##    time.sleep(0.1)
        ##    PiPort.setMappedOutput(6, "off")
        ##    time.sleep(0.1)
        ##    PiPort.setMappedOutput(7, "off")
        ##    time.sleep(0.1)
        ##    PiPort.setMappedOutput(8, "off")
        ##    time.sleep(0.1)
        ##    PiPort.setMappedOutput(9, "off")
        ##    time.sleep(0.1)
        

        ### Checking Input States

#        for counter in range(len(arrayOfArrays)): 
#            PiPort.setOutputArray(arrayOfArrays[counter])
#
            time.sleep(0.04)


except Exception:
    if debug:
        print "exception generated and caught"



