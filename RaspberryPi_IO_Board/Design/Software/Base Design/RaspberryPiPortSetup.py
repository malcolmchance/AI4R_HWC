##############################################################
# Import Statements 
##############################################################
# Raspbian install RPi.GPIO directly 
# using apt-get as follows:
#
# sudo apt-get update
# sudo apt-get -y install python-rpi.gpio
##############################################################

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD) # Refer to pin number


##############################################################
# Name: initializeIO
# Comment: Setup GPIO Inputs and Outputs
#-------------------------------------------------------------
"""
   This function sets up the input and output pins of the GPIO
   as follows
     Input Pins:   12,16,18,22
    Outputs Pins: 3,5,7,11,13,15,19,21,23
"""
##############################################################
def initializeIO():
   #import RPi.GPIO as GPIO
   #-------- Inputs ----------#
   GPIO.setup(12, GPIO.IN)
   GPIO.setup(16, GPIO.IN)
   GPIO.setup(18, GPIO.IN)
   GPIO.setup(22, GPIO.IN)
   #-------- Outputs ---------#
   GPIO.setup(3, GPIO.OUT)
   GPIO.setup(5, GPIO.OUT)
   GPIO.setup(7, GPIO.OUT)
   GPIO.setup(11, GPIO.OUT)
   GPIO.setup(13, GPIO.OUT)
   GPIO.setup(15, GPIO.OUT)
   GPIO.setup(19, GPIO.OUT)
   GPIO.setup(21, GPIO.OUT)
   GPIO.setup(23, GPIO.OUT)


##############################################################
# Name: setAllOutputsLow
# Comment: Set all GPIO Outputs to low
#-------------------------------------------------------------
"""
   This function sets all GPIO output pins to low
    Outputs Pins: 3,5,7,11,13,15,19,21,23
"""
##############################################################
def setAllOutputsLow():
   GPIO.output(3, False)
   GPIO.output(5, False)
   GPIO.output(7, False)
   GPIO.output(11, False) 
   GPIO.output(13, False) 
   GPIO.output(15, False)
   GPIO.output(19, False)
   GPIO.output(21, False) 
   GPIO.output(23, False)


##############################################################
# Name: setAllOutputsHigh
# Comment: Set all GPIO Outputs to High
#-------------------------------------------------------------
"""
   This function sets all GPIO output pins to high
    Outputs Pins: 3,5,7,11,13,15,19,21,23
"""
##############################################################
def setAllOutputsHigh():
    GPIO.output(3, True)
    GPIO.output(5, True)
    GPIO.output(7, True)
    GPIO.output(11, True) 
    GPIO.output(13, True)
    GPIO.output(15, True)
    GPIO.output(19, True)
    GPIO.output(21, True) 
    GPIO.output(23, True)


##############################################################
# Name: setOutput
# Comment: Set all GPIO Outputs to low or high
#-------------------------------------------------------------
"""
   This function sets all GPIO output pins to low
    Outputs Pins: 3,5,7,11,13,15,19,21,23
"""
##############################################################
def setOutput(output, onoff):
   #----------------------------------------------------------
   # Debug Print Statements
   #----------------------------------------------------------
   #print "output =", output
   #print "state =", onoff

   #-----------------------------------------------------------
   # Error Checking on output port
   # Valid values are 3,5,7,11,13,15,19,21,23
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
   # Set output true or false
   #-----------------------------------------------------------
   if onoff == "ON" or onoff == "on":
      GPIO.output(output, True)
   if onoff == "OFF" or onoff == "off":
      GPIO.output(output, False)   


##############################################################
# Name: setMappedOutput
# Comment: Set all GPIO Outputs to low or high
# Outputs are in the range 1 thru 9.
#-------------------------------------------------------------
"""
   This function sets all GPIO output pins to low
    Outputs Pins: 3,5,7,11,13,15,19,21,23
"""
##############################################################
def setMappedOutput(output, onoff):
   #----------------------------------------------------------
   # Debug Print Statements
   #----------------------------------------------------------
   #print "output =", output
   #print "state =", onoff

   #-----------------------------------------------------------
   # Error Checking on output port
   # Valid values are 1,2,3,4,5,6,7,8,9
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
   # Map the pin number to the output
   #-----------------------------------------------------------
   if output == 1:
      pin = 3
   if output == 2:
      pin = 5
   if output == 3:
      pin = 7
   if output == 4:
      pin = 11
   if output == 5:
      pin = 13
   if output == 6:
      pin = 15
   if output == 7:
      pin = 19
   if output == 8:
      pin = 21
   if output == 9:
      pin = 23
   #-----------------------------------------------------------
   # Set output true or false
   #-----------------------------------------------------------      
   if onoff == "ON" or onoff == "on":
      GPIO.output(pin, True)
   if onoff == "OFF" or onoff == "off":
      GPIO.output(pin, False)   


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
# Name: checkInput
# Comment: Check status of inputs 1,2,3 and 4
#---------------------------------------------------------------------------------------
"""
   Check status of inputs 1,2,3 and 4
"""
########################################################################################
##def checkInput():
##    # Create inputList[0,1,2,3]
##    inputList = [ True, True, True, True]
##    if GPIO.input(12) == True:              #if myLEDFrame.isPressed_button_1() == True:
##        inputList[0] = False
##    if GPIO.input(16) == True:              #if myLEDFrame.isPressed_button_2() == True:
##        inputList[1] = False        
##    if GPIO.input(18) == True:              #if myLEDFrame.isPressed_button_3() == True:
##        inputList[2] = False
##    if GPIO.input(22) == True:              #if myLEDFrame.isPressed_button_4() == True:
##        inputList[3] = False
##    return inputList
