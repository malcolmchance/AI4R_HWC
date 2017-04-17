#!/usr/bin/python
##############################################################
# Import Statements 
##############################################################
import time

#-------------------------------------------------------------
# Uncomment for used with Raspberry Pi Board
#-------------------------------------------------------------
#import RPi.GPIO as GPIO
#import RaspberryPiPortSetup as PiPort # imports RPi.GPIO as GPIO

#-------------------------------------------------------------
# Uncomment for used with Raspberry Pi Simulator
#-------------------------------------------------------------
import RaspberryPiPortSetupSim as PiPort # imports RPi.GPIO as GPIO

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
    while True:
        ##    PiPort.setAllOutputsHigh()
        ##    time.sleep(.5)
        ##    PiPort.setAllOutputsLow()
        ##    time.sleep(.5)
        ##    PiPort.setOutput(3, "on")
        ##    time.sleep(.5)
        ##    PiPort.setMappedOutput(1, "off")


        ### Checking Input States
        ##    inputState = PiPort.checkInput()
        ##
        ##    for counter in range (0,len(inputState),1):
        ##        #print "Input(" + (counter + 1) + ") = " + inputState(counter)
        ##        print "Input(%s) = %s" % ((counter + 1), inputState[counter])



        ##for counter in range(len(arrayOfArrays)):
        ##    PiPort.setOutputArray(arrayOfArrays[counter])
        ##    time.sleep(0.04)


         
        PiPort.setMappedOutput(3, "on")
        time.sleep(0.5)
        PiPort.setMappedOutput(3, "off")
        time.sleep(0.5)

except Exception:

    print "exception generated and caught"







