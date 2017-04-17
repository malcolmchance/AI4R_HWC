#!/usr/bin/python

################################################################################
# Import Statements 
################################################################################
import time
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)


#-------------------------------------------------------------------------------
# Uncomment for used with Raspberry Pi Board
#-------------------------------------------------------------------------------
import RaspberryPiPortSetup as PiPort # imports RPi.GPIO as GPIO

#-------------------------------------------------------------------------------
# Uncomment for used with Raspberry Pi Simulator
#-------------------------------------------------------------------------------
#import RaspberryPiPortSetupSim as PiPort # imports RPi.GPIO as GPIO

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


################################################################################
# Initialize E-mail
################################################################################

def send_email():
    fromaddr = "notarealname@gmail.com"
    toaddr = "notarealname@yahoo.com"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Test of Python Send Mail"
    body = "This is a test from raspberrypi."
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.starttls()
    server.login(fromaddr, "notarealpassword")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()


################################################################################
# Initialize Interrupt
################################################################################
def my_callback(channel):
    print "falling edge detected on switch 1\n"
def my_callback2(channel):
    print "falling edge detected on switch 2\n"
    
def add_events():
    # when a falling edge is detected on port 12 (Input 1)
    GPIO.add_event_detect(16, GPIO.FALLING, callback=my_callback, bouncetime=300)
    # when a falling edge is detected on port 23 (Input 2)
    GPIO.add_event_detect(18, GPIO.FALLING, callback=my_callback2, bouncetime=300)
    
def del_events():
    GPIO.remove_event_detect(16)
    GPIO.remove_event_detect(18)

################################################################################
# Main Loop Route
################################################################################
raw_input("Press Enter when ready\n>")
add_events()
try:
    print "Alarm has been armed"
    GPIO.wait_for_edge(12, GPIO.FALLING)
    print "Intrusion Detection!!."
    print "Lights are flashing and en e-mail has been sent"
    send_email()
    for count in range (3):
        del_events()
        PiPort.setAllOutputsHigh()
        print "FLASH"
        time.sleep(.5)
        PiPort.setAllOutputsLow()
        time.sleep(.5)
        for counter in range(len(arrayOfArrays)):
            PiPort.setOutputArray(arrayOfArrays[counter])
            time.sleep(0.09)

except KeyboardInterrupt:
   PiPort.setAllOutputsLow()
   print "Ctrl-C exception caught. All outputs set to low"

except Exception:
   if debug:
      print "exception generated and caught"

PiPort.setAllOutputsLow()


