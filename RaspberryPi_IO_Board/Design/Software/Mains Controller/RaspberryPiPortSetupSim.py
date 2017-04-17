#!/usr/bin/python

########################################################################################
# Import Statements 
########################################################################################
# import RPi.GPIO as GPIO
from time import *
import RaspberryPiSimLEDDriver as myPort 


########################################################################################
# Name: initializeIO
# Comment: Setup GPIO Inputs and Outputs
#---------------------------------------------------------------------------------------
"""
   This function sets up the input and output pins of the GPIO
   as follows
    Input Pins:   12,16,18,22
    Outputs Pins: 3,5,7,11,13,15,19,21,23
"""
########################################################################################

def initializeIO():
##   import RPi.GPIO as GPIO
##   #-------- Inputs ----------#
##   GPIO.setup(12, GPIO.IN)
##   GPIO.setup(16, GPIO.IN)
##   GPIO.setup(18, GPIO.IN)
##   GPIO.setup(22, GPIO.IN)
##   #-------- Outputs ---------#
##   GPIO.setup(3, GPIO.OUT)
##   GPIO.setup(5, GPIO.OUT)
##   GPIO.setup(7, GPIO.OUT)
##   GPIO.setup(11, GPIO.OUT)
##   GPIO.setup(13, GPIO.OUT)
##   GPIO.setup(15, GPIO.OUT)
##   GPIO.setup(19, GPIO.OUT)
##   GPIO.setup(21, GPIO.OUT)
##   GPIO.setup(23, GPIO.OUT)
    
    global myLEDFrame
    myLEDFrame = myPort.MyFrame()

########################################################################################
# End initalizeIO
########################################################################################


########################################################################################
# Name: setAllOutputsLow
# Comment: Set all GPIO Outputs to low
#---------------------------------------------------------------------------------------
"""
   This function sets all GPIO output pins to low
    Outputs Pins: 3,5,7,11,13,15,19,21,23
"""
########################################################################################

def setAllOutputsLow():
    global myLEDFrame
    myLEDFrame.red_LED1_Control(False)    ##   Equivalent to GPIO.output(3, False)
    myLEDFrame.red_LED2_Control(False)    ##   Equivalent to  GPIO.output(5, False)
    myLEDFrame.red_LED3_Control(False)    ##   Equivalent to GPIO.output(7, False)
    myLEDFrame.yellow_LED1_Control(False) ##   Equivalent to GPIO.output(11, False)
    myLEDFrame.yellow_LED2_Control(False) ##   Equivalent to GPIO.output(13, False)
    myLEDFrame.yellow_LED3_Control(False) ##   Equivalent to GPIO.output(15, False)
    myLEDFrame.green_LED1_Control(False)  ##   Equivalent to GPIO.output(19, False)
    myLEDFrame.green_LED2_Control(False)  ##   Equivalent to GPIO.output(21, False)
    myLEDFrame.green_LED3_Control(False)  ##   Equivalent to GPIO.output(23, False)

########################################################################################
# End setAllOutputsLow
########################################################################################

########################################################################################
# Name: setAllOutputsHigh
# Comment: Set all GPIO Outputs to High
#---------------------------------------------------------------------------------------
"""
   This function sets all GPIO output pins to high
    Outputs Pins: 3,5,7,11,13,15,19,21,23
"""
########################################################################################

def setAllOutputsHigh():
    global myLEDFrame
    myLEDFrame.red_LED1_Control(True)     ##   Equivalent to GPIO.output(3, True)
    myLEDFrame.red_LED2_Control(True)     ##   Equivalent to GPIO.output(5, True)
    myLEDFrame.red_LED3_Control(True)     ##   Equivalent to GPIO.output(7, True)
    myLEDFrame.yellow_LED1_Control(True)  ##   Equivalent to GPIO.output(11, True)
    myLEDFrame.yellow_LED2_Control(True)  ##   Equivalent to GPIO.output(13, True)
    myLEDFrame.yellow_LED3_Control(True)  ##   Equivalent to GPIO.output(15, True)
    myLEDFrame.green_LED1_Control(True)   ##   Equivalent to GPIO.output(19, True)
    myLEDFrame.green_LED2_Control(True)   ##   Equivalent to GPIO.output(21, True)
    myLEDFrame.green_LED3_Control(True)   ##   Equivalent to GPIO.output(23, True)

########################################################################################
# End setAllOutputsHigh
########################################################################################

########################################################################################
# Name: setOutput
# Comment: Set all GPIO Outputs to low or high
#---------------------------------------------------------------------------------------
"""
   This function sets all GPIO output pins to low
    Outputs Pins: 3,5,7,11,13,15,19,21,23
"""
########################################################################################

def setOutput(output, onoff):
   global myLEDFrame
   #----------------------------------------------------------
   # Debug Print Statements
   #----------------------------------------------------------
   #print "output =", output
   #print "state =", onoff

   #-----------------------------------------------------------
   # Error Checking on output port
   # Valid values are 3, 5, 7, 11, 13, 15, 19, 21, 23
   # LED Equivalents  1, 2, 3,  4,  5,  6,  7,  8,  9 
   #-----------------------------------------------------------
   if output != 3 and output != 5 and output != 7 and output != 11 and output != 13 and output != 15 and output != 19 and output != 21 and output != 23:
      return "Invalid Port"
   #-----------------------------------------------------------
   # Error Checking on output state
   # Valid values are on, ON, off, OFF
   #-----------------------------------------------------------
   if onoff != "ON" and onoff != "on" and onoff != "OFF" and onoff != "off":
      return "Invalid value"
   #-----------------------------------------------------------
   # Set output true
   #-----------------------------------------------------------
   if onoff == "ON" or onoff == "on":
      # Turn output on
      if output == 3:
         myLEDFrame.red_LED1_Control(True)
      if output == 5:
         myLEDFrame.red_LED2_Control(True)    
      if output == 7:
         myLEDFrame.red_LED3_Control(True)
      if output == 11:
         myLEDFrame.yellow_LED1_Control(True)
      if output == 13:
         myLEDFrame.yellow_LED2_Control(True)
      if output == 15:
         myLEDFrame.yellow_LED3_Control(True)
      if output == 19:
         myLEDFrame.green_LED1_Control(True)
      if output == 21:
         myLEDFrame.green_LED2_Control(True)
      if output == 23:
         myLEDFrame.green_LED3_Control(True)
            
   #-----------------------------------------------------------
   # Set output false
   #-----------------------------------------------------------
   if onoff == "OFF" or onoff == "off":
      if output == 3:
         myLEDFrame.red_LED1_Control(False)
      if output == 5:
         myLEDFrame.red_LED2_Control(False)    
      if output == 7:
         myLEDFrame.red_LED3_Control(False)
      if output == 11:
         myLEDFrame.yellow_LED1_Control(False)
      if output == 13:
         myLEDFrame.yellow_LED2_Control(False)
      if output == 15:
         myLEDFrame.yellow_LED3_Control(False)
      if output == 19:
         myLEDFrame.green_LED1_Control(False)
      if output == 21:
         myLEDFrame.green_LED2_Control(False)
      if output == 23:
         myLEDFrame.green_LED3_Control(False)
 

########################################################################################
# End setOutput
########################################################################################

########################################################################################
# Name: setMappedOutput
# Comment: Set all GPIO Outputs to low or high
# Outputs are in the range 1 thru 9.
#---------------------------------------------------------------------------------------
"""
   This function sets all GPIO output pins to low
    Outputs Pins: 3,5,7,11,13,15,19,21,23
"""
########################################################################################

def setMappedOutput(output, onoff):
   global myLEDFrame
   #----------------------------------------------------------
   # Debug Print Statements
   #----------------------------------------------------------
   #print "output =", output
   #print "state =", onoff

   #-----------------------------------------------------------
   # Error Checking on output port
   # Valid values are 1, 2, 3,  4,  5,  6 ,7,   8,  9 
   # GPIO Equivalents 3, 5, 7, 11, 13, 15, 19, 21, 23
   # LED Equivalents  1, 2, 3,  4,  5,  6,  7,  8,  9 
   #-----------------------------------------------------------
   if output != 1 and output != 2 and output != 3 and output != 4 and output != 5 and output != 6 and output != 7 and output != 8 and output != 9:
      return "Invalid Port"
   #-----------------------------------------------------------
   # Error Checking on output state
   # Valid values are on, ON, off, OFF
   #-----------------------------------------------------------
   if onoff != "ON" and onoff != "on" and onoff != "OFF" and onoff != "off":
      return "Invalid value"
   #-----------------------------------------------------------
   # Set output true
   #-----------------------------------------------------------
   if onoff == "ON" or onoff == "on":
      # Turn output on
      if output == 1:
         myLEDFrame.red_LED1_Control(True)
      if output == 2:
         myLEDFrame.red_LED2_Control(True)    
      if output == 3:
         myLEDFrame.red_LED3_Control(True)
      if output == 4:
         myLEDFrame.yellow_LED1_Control(True)
      if output == 5:
         myLEDFrame.yellow_LED2_Control(True)
      if output == 6:
         myLEDFrame.yellow_LED3_Control(True)
      if output == 7:
         myLEDFrame.green_LED1_Control(True)
      if output == 8:
         myLEDFrame.green_LED2_Control(True)
      if output == 9:
         myLEDFrame.green_LED3_Control(True)
            
   #-----------------------------------------------------------
   # Set output false
   #-----------------------------------------------------------
   if onoff == "OFF" or onoff == "off":
      if output == 1:
         myLEDFrame.red_LED1_Control(False)
      if output == 2:
         myLEDFrame.red_LED2_Control(False)    
      if output == 3:
         myLEDFrame.red_LED3_Control(False)
      if output == 4:
         myLEDFrame.yellow_LED1_Control(False)
      if output == 5:
         myLEDFrame.yellow_LED2_Control(False)
      if output == 6:
         myLEDFrame.yellow_LED3_Control(False)
      if output == 7:
         myLEDFrame.green_LED1_Control(False)
      if output == 8:
         myLEDFrame.green_LED2_Control(False)
      if output == 9:
         myLEDFrame.green_LED3_Control(False)  

########################################################################################
# End setOutput
########################################################################################

########################################################################################
# Name: setOutputArray
# Comment: Set LEDs using nine element array
#---------------------------------------------------------------------------------------
"""
   Set LEDs using nine element array
"""
########################################################################################
def setOutputArray(LEDArray):
    if len(LEDArray) != 9:
        print "error in LEDArray length"
        return
    for counter in range(len(LEDArray)):
        setMappedOutput((counter+1), LEDArray[counter])


########################################################################################
# End checkInput
########################################################################################

########################################################################################
# Name: checkInputs
# Comment: Check status of inputs 1,2,3 and 4
#---------------------------------------------------------------------------------------
"""
   Check status of inputs 1,2,3 and 4
"""
########################################################################################
def checkInput():
    global myLEDFrame
    # Create inputList[0,1,2,3]
    inputList = [ True, True, True, True]
    if myLEDFrame.isPressed_button_1() == True:             # if GPIO.input(12) == True:
        inputList[0] = False
    if myLEDFrame.isPressed_button_2() == True:             # if GPIO.input(16) == True:
        inputList[1] = False        
    if myLEDFrame.isPressed_button_3() == True:             # if GPIO.input(18) == True:
        inputList[2] = False
    if myLEDFrame.isPressed_button_4() == True:             # if GPIO.input(22) == True:
        inputList[3] = False
    return inputList

########################################################################################
# End checkInput
########################################################################################





########################################################################################
# Name: Main
# Comment: Provides Default Run and used as test harness for this file
#---------------------------------------------------------------------------------------
"""
   Provides Default Run and used as test harness for this file
"""
########################################################################################

def main():
    myLEDFrame = myPort.MyFrame()
    while True:
        myLEDFrame.red_LED1_Control(False)
        myLEDFrame.red_LED2_Control(False)
        myLEDFrame.red_LED3_Control(False)
        
        myLEDFrame.yellow_LED1_Control(False)
        myLEDFrame.yellow_LED2_Control(False)
        myLEDFrame.yellow_LED3_Control(False)
        
        myLEDFrame.green_LED1_Control(False)
        myLEDFrame.green_LED2_Control(False)
        myLEDFrame.green_LED3_Control(False)

        
        
        if myLEDFrame.isPressed_button_1() == True:
            print "Button 1 pressed - message from main"
        if myLEDFrame.isPressed_button_2() == True:
            print "Button 2 pressed - message from main"
        if myLEDFrame.isPressed_button_3() == True:
            print "Button 3 pressed - message from main"
        if myLEDFrame.isPressed_button_4() == True:
            print "Button 4 pressed - message from main"
         
        sleep(.5)
        myLEDFrame.red_LED1_Control(True)
        myLEDFrame.red_LED2_Control(True)
        myLEDFrame.red_LED3_Control(True)
        
        myLEDFrame.yellow_LED1_Control(True)
        myLEDFrame.yellow_LED2_Control(True)
        myLEDFrame.yellow_LED3_Control(True)
        
        myLEDFrame.green_LED1_Control(True)
        myLEDFrame.green_LED2_Control(True)
        myLEDFrame.green_LED3_Control(True)
        sleep(.5)

#---------------------------------------------------------------------------------------
#  Run Main is this fils is not called from another module.
#---------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()

########################################################################################
# End Main
########################################################################################
