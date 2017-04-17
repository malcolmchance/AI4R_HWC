#############################################################################################################
#                                   Import Statements
#############################################################################################################
from Tkinter import *
from time import *

#############################################################################################################
#                                   Start of Class MyFrame
#############################################################################################################
class MyFrame(Frame):

    # Enable or disable debug print statements.
    # set debug = True to enable
    global debug
    debug = False

    #========================================================================================================
    #                                   Class Constructor
    #========================================================================================================

    def __init__(self):
        Frame.__init__(self)

        #---------------------------------------------------------------------------------------------------
        # Use of 'master' access base class attribute (geometry/title) of Frame
        #---------------------------------------------------------------------------------------------------
        self.master.geometry("190x500")                                                        # Set Window Size
        self.master.title("LEDs and Buttons")                                                  # Set Window Name

        #---------------------------------------------------------------------------------------------------
        # Set Canvas Size and Add Canvas to Frame
        #---------------------------------------------------------------------------------------------------
        self.myCanvasLeft=Canvas(width=60, height=500, bg="blue")                              # Set Canvas Size
        self.myCanvasLeft.grid(row = 0, column = 0)                                            # Add Canvas to left of Frame

        #---------------------------------------------------------------------------------------------------
        # Create Custom Colors
        #---------------------------------------------------------------------------------------------------     
        self.myLiteRed    = '#ff0000'                                                          # define color - lightred
        self.myDarkRed    = '#8b0000'                                                          # define color - darkred
        self.myLiteYellow = '#ffff00'                                                          # define color - lightyellow 
        self.myDarkYellow = '#8b8b00'                                                          # define color - darkyellow
        self.myLiteGreen  = '#008000'                                                          # define color - lightygreen 
        self.myDarkGreen  = '#006400'                                                          # define color - darkgreen
        self.myLiteViolet = '#ee82ee'                                                          # define color - lightviolet 
        self.myDarkViolet = '#9400d3'                                                          # define color - darkyviolet

        #---------------------------------------------------------------------------------------------------
        # Create LEDs to the left of the Frame
        #---------------------------------------------------------------------------------------------------    

        self.myRedLED1    = self.myCanvasLeft.create_oval(10, 30,  50, 70,  fill="red")        # Create Oval on Canvas
        self.myRedLED2    = self.myCanvasLeft.create_oval(10, 80,  50, 120, fill="red")        # Create Oval on Canvas
        self.myRedLED3    = self.myCanvasLeft.create_oval(10, 130, 50, 170, fill="red")        # Create Oval on Canvas
        
        self.myAmberLED1  = self.myCanvasLeft.create_oval(10, 180, 50, 220, fill="yellow")     # Create Oval on Canvas
        self.myAmberLED2  = self.myCanvasLeft.create_oval(10, 230, 50, 270, fill="yellow")     # Create Oval on Canvas
        self.myAmberLED3  = self.myCanvasLeft.create_oval(10, 280, 50, 320, fill="yellow")     # Create Oval on Canvas
        
        self.myGreenLED1  = self.myCanvasLeft.create_oval(10, 330, 50, 370, fill="green")      # Create Oval on Canvas
        self.myGreenLED2  = self.myCanvasLeft.create_oval(10, 380, 50, 420, fill="green")      # Create Oval on Canvas
        self.myGreenLED3  = self.myCanvasLeft.create_oval(10, 430, 50, 470, fill="green")      # Create Oval on Canvas

        #---------------------------------------------------------------------------------------------------
        # Add grid for buttons to middle of frame and add the buttons
        #---------------------------------------------------------------------------------------------------
        self.grid(row = 0, column = 1)                                                            # Add Frame

        #---------------------------------------------------------------------------------------------------
        # Create top and bottom label text strings and set text
        #---------------------------------------------------------------------------------------------------
        self.topLabelText = StringVar()
        self.bottomLabelText = StringVar()
        self.topLabelText.set("LED Status")
        self.bottomLabelText.set("Button Status")
        
        #---------------------------------------------------------------------------------------------------
        # Create button label text strings and set text
        #---------------------------------------------------------------------------------------------------     
        self.redButtonText = StringVar()
        self.yellowButtonText = StringVar()
        self.greenButtonText = StringVar()
        self.violetButtonText = StringVar()
        self.redButtonText.set("Input 1 - High")
        self.yellowButtonText.set("Input 2 - High")
        self.greenButtonText.set("Input 3 - High")
        self.violetButtonText.set("Input 4 - High")

        #---------------------------------------------------------------------------------------------------
        # Set button state to un-pressed
        #---------------------------------------------------------------------------------------------------
        self.button_1_Pressed = False                                                         # set button state to un-pressed
        self.button_2_Pressed = False                                                         # set button state to un-pressed
        self.button_3_Pressed = False                                                         # set button state to un-pressed
        self.button_4_Pressed = False                                                         # set button state to un-pressed

        #---------------------------------------------------------------------------------------------------
        # Draw buttons
        #---------------------------------------------------------------------------------------------------          
        Label(self,  textvariable = self.topLabelText, width = 16, height = 4, fg = "white", bg = "blue").grid(row=0, sticky=W+E)
        self.drawRedButton(self.myLiteRed)
        self.drawYellowButton(self.myLiteYellow)
        self.drawGreenButton(self.myLiteGreen)
        self.drawVioletButton(self.myLiteViolet)
        Label(self,  textvariable = self.bottomLabelText, width = 16, height = 4, fg = "white", bg = "blue").grid(row=5, sticky=W+E)

        #---------------------------------------------------------------------------------------------------
        # Create Space to the right of the Frame
        #---------------------------------------------------------------------------------------------------
        self.myCanvasRight=Canvas(width=20, height=410, bg="blue")                               # Set Canvas Size
        self.myCanvasRight.grid(row = 0, column = 2)                                             # Add Canvas to right  of Frame

    #========================================================================================================
    #                                   Class Methods
    #========================================================================================================

    #--------------------------------------------------------------------------------------------------------
    # Draw Button Methods
    #--------------------------------------------------------------------------------------------------------

    def drawButton(self, btn_text, btn_color, btn_command, btn_row):
        """ draw_Button(self, btn_text, btn_color, btn_command, btn_row):
                btn_text     - Text to show on button.
                btn_color    - Color of Button
                btn_command  - command to be performed by button
                btn_row      - Row where button is to be placed.
        """

        Button(self, textvariable = btn_text, width = 16, height = 5, bg = btn_color, bd = 5, command = btn_command).grid(row=btn_row, sticky=W+E)

    def drawRedButton(self, btn_color):
        self.drawButton(btn_text = self.redButtonText,    btn_color = btn_color, btn_command = self.click_button_1, btn_row = 1)
        
    def drawYellowButton(self, btn_color):
        self.drawButton(btn_text = self.yellowButtonText, btn_color = btn_color, btn_command = self.click_button_2, btn_row = 2)
        
    def drawGreenButton(self, btn_color):
        self.drawButton(btn_text = self.greenButtonText,  btn_color = btn_color, btn_command = self.click_button_3, btn_row = 3)
        
    def drawVioletButton(self, btn_color):
        self.drawButton(btn_text = self.violetButtonText, btn_color = btn_color, btn_command = self.click_button_4, btn_row = 4)
        
    #--------------------------------------------------------------------------------------------------------
    # Button_1 Click Method
    #--------------------------------------------------------------------------------------------------------
    def click_button_1(self):
        if debug:
            print "Pressed button_1"                                        
        self.bottomLabelText.set("Button 1 Pressed")                
        if self.button_1_Pressed == True:                   # If button currently pressed then:
           self.button_1_Pressed = False                    #   Set its state to unpressed
           self.redButtonText.set("Input 1 - High")         #   Set the button text to show high state
           self.drawRedButton(self.myLiteRed)               #   Set the button color to light
        elif self.button_1_Pressed == False:                # If button currently UNpressed then:
           self.button_1_Pressed = True                     #   Set its state to pressed
           self.redButtonText.set("Input 1 - Low")          #   Set the button text to show low state
           self.drawRedButton(self.myDarkRed)               #   Set the button color to dark
        else:
            print "Error in click_button_1"

    #--------------------------------------------------------------------------------------------------------
    # Button_1 Check Method
    #--------------------------------------------------------------------------------------------------------
    def isPressed_button_1(self):
        if self.button_1_Pressed == True:
            return True
        elif self.button_1_Pressed == False:
            return False
        else:
            print "Error in function isPressed_button_1"

   #--------------------------------------------------------------------------------------------------------
    # Button_2 Click Method
    #--------------------------------------------------------------------------------------------------------
    def click_button_2(self):
        if debug:
            print "Pressed button_2"                                        
        self.bottomLabelText.set("Button 2 Pressed")                
        if self.button_2_Pressed == True:                   # If button currently pressed then:
           self.button_2_Pressed = False                    #   Set its state to unpressed
           self.yellowButtonText.set("Input 2 - High")      #   Set the button text to show high state
           self.drawYellowButton(self.myLiteYellow)         #   Set the button color to light
        elif self.button_2_Pressed == False:                # If button currently UNpressed then:
           self.button_2_Pressed = True                     #   Set its state to pressed
           self.yellowButtonText.set("Input 2 - Low")       #   Set the button text to show low state
           self.drawYellowButton(self.myDarkYellow)            #   Set the button color to dark
        else:
            print "Error in click_button_2"

    #--------------------------------------------------------------------------------------------------------
    # Button_2 Check Method
    #--------------------------------------------------------------------------------------------------------
    def isPressed_button_2(self):
        if self.button_2_Pressed == True:
            return True
        elif self.button_2_Pressed == False:
            return False
        else:
            print "Error in function isPressed_button_2"


   #--------------------------------------------------------------------------------------------------------
    # Button_3 Click Method
    #--------------------------------------------------------------------------------------------------------
    def click_button_3(self):
        if debug:
            print "Pressed button_3"                                        
        self.bottomLabelText.set("Button 3 Pressed")                
        if self.button_3_Pressed == True:                   # If button currently pressed then:
           self.button_3_Pressed = False                    #   Set its state to unpressed
           self.greenButtonText.set("Input 3 - High")       #   Set the button text to show high state
           self.drawGreenButton(self.myLiteGreen)           #   Set the button color to light
        elif self.button_3_Pressed == False:                # If button currently UNpressed then:
           self.button_3_Pressed = True                     #   Set its state to pressed
           self.greenButtonText.set("Input 3 - Low")        #   Set the button text to show low state
           self.drawGreenButton(self.myDarkGreen)            #   Set the button color to dark
        else:
            print "Error in click_button_3"

    #--------------------------------------------------------------------------------------------------------
    # Button_3 Check Method
    #--------------------------------------------------------------------------------------------------------
    def isPressed_button_3(self):
        if self.button_3_Pressed == True:
            return True
        elif self.button_3_Pressed == False:
            return False
        else:
            print "Error in function isPressed_button_3"


   #--------------------------------------------------------------------------------------------------------
    # Button_4 Click Method
    #--------------------------------------------------------------------------------------------------------
    def click_button_4(self):
        if debug:
            print "Pressed button_4"                                        
        self.bottomLabelText.set("Button 4 Pressed")                
        if self.button_4_Pressed == True:                   # If button currently pressed then:
           self.button_4_Pressed = False                    #   Set its state to unpressed
           self.violetButtonText.set("Input 4 - High")      #   Set the button text to show high state
           self.drawVioletButton(self.myLiteViolet)         #   Set the button color to light
        elif self.button_4_Pressed == False:                # If button currently UNpressed then:
           self.button_4_Pressed = True                     #   Set its state to pressed
           self.violetButtonText.set("Input 4 - Low")       #   Set the button text to show low state
           self.drawVioletButton(self.myDarkViolet)         #   Set the button color to dark
        else:
            print "Error in click_button_4"

    #--------------------------------------------------------------------------------------------------------
    # Button_4 Check Method
    #--------------------------------------------------------------------------------------------------------
    def isPressed_button_4(self):
        if self.button_4_Pressed == True:
            return True
        elif self.button_4_Pressed == False:
            return False
        else:
            print "Error in function isPressed_button_4"

        
    #--------------------------------------------------------------------------------------------------------
    # Red LED 1 Control Method
    #--------------------------------------------------------------------------------------------------------
    def red_LED1_Control(self, ONOFF):
        if debug:
            print "red_LED1_Control(%s)" % ONOFF
        self.topLabelText.set("Red LED 1 (%s)" % ONOFF)

        if ONOFF == True:
            self.myCanvasLeft.itemconfig(self.myRedLED1, fill = self.myLiteRed)
        elif ONOFF == False:
            self.myCanvasLeft.itemconfig(self.myRedLED1, fill = self.myDarkRed)
        else:
            print "Error in function red_LED1_Control"
        self.myCanvasLeft.update()

    #--------------------------------------------------------------------------------------------------------
    # Red LED 2 Control Method
    #--------------------------------------------------------------------------------------------------------
    def red_LED2_Control(self, ONOFF):
        if debug:
            print "red_LED2_Control(%s)" % ONOFF
        self.topLabelText.set("Red LED 2 (%s)" % ONOFF)

        if ONOFF == True:
            self.myCanvasLeft.itemconfig(self.myRedLED2, fill = self.myLiteRed)
        elif ONOFF == False:
            self.myCanvasLeft.itemconfig(self.myRedLED2, fill = self.myDarkRed)
        else:
            print "Error in function red_LED2_Control"
        self.myCanvasLeft.update()

    #--------------------------------------------------------------------------------------------------------
    # Red LED 3 Control Method
    #--------------------------------------------------------------------------------------------------------
    def red_LED3_Control(self, ONOFF):
        if debug:
            print "red_LED3_Control(%s)" % ONOFF
        self.topLabelText.set("Red LED 3 (%s)" % ONOFF)

        if ONOFF == True:
            self.myCanvasLeft.itemconfig(self.myRedLED3, fill = self.myLiteRed)
        elif ONOFF == False:
            self.myCanvasLeft.itemconfig(self.myRedLED3, fill = self.myDarkRed)
        else:
            print "Error in function red_LED3_Control"
        self.myCanvasLeft.update()

    #--------------------------------------------------------------------------------------------------------
    # Yellow LED 1 Control Method
    #--------------------------------------------------------------------------------------------------------
    def yellow_LED1_Control(self, ONOFF):
        if debug:
            print "yellow_LED1_Control(%s)" % ONOFF
        self.topLabelText.set("Yellow LED 1 (%s)" % ONOFF)

        if ONOFF == True:
            self.myCanvasLeft.itemconfig(self.myAmberLED1, fill = self.myLiteYellow)
        elif ONOFF == False:
            self.myCanvasLeft.itemconfig(self.myAmberLED1, fill = self.myDarkYellow)
        else:
            print "Error in function yellow_LED1_Control"

        self.myCanvasLeft.update()

    #--------------------------------------------------------------------------------------------------------
    # Yellow LED 2 Control Method
    #--------------------------------------------------------------------------------------------------------
    def yellow_LED2_Control(self, ONOFF):
        if debug:
            print "yellow_LED2_Control(%s)" % ONOFF
        self.topLabelText.set("Yellow LED 2 (%s)" % ONOFF)

        if ONOFF == True:
            self.myCanvasLeft.itemconfig(self.myAmberLED2, fill = self.myLiteYellow)
        elif ONOFF == False:
            self.myCanvasLeft.itemconfig(self.myAmberLED2, fill = self.myDarkYellow)
        else:
            print "Error in function yellow_LED2_Control"

        self.myCanvasLeft.update()

    #--------------------------------------------------------------------------------------------------------
    # Yellow LED 3 Control Method
    #--------------------------------------------------------------------------------------------------------
    def yellow_LED3_Control(self, ONOFF):
        if debug:
            print "yellow_LED3_Control(%s)" % ONOFF
        self.topLabelText.set("Yellow LED 3 (%s)" % ONOFF)

        if ONOFF == True:
            self.myCanvasLeft.itemconfig(self.myAmberLED3, fill = self.myLiteYellow)
        elif ONOFF == False:
            self.myCanvasLeft.itemconfig(self.myAmberLED3, fill = self.myDarkYellow)
        else:
            print "Error in function yellow_LED3_Control"

        self.myCanvasLeft.update()
        
    #--------------------------------------------------------------------------------------------------------
    # Green LED 1 Control Method
    #--------------------------------------------------------------------------------------------------------
    def green_LED1_Control(self, ONOFF):
        if debug:
            print "green_LED1_Control(%s)" % ONOFF
        self.topLabelText.set("Green LED 1 (%s)" % ONOFF)

        if ONOFF == True:
            self.myCanvasLeft.itemconfig(self.myGreenLED1, fill = self.myLiteGreen)
        elif ONOFF == False:
            self.myCanvasLeft.itemconfig(self.myGreenLED1, fill = self.myDarkGreen)
        else:
            print "Error in function green_LED1_Control"

        self.myCanvasLeft.update()

    #--------------------------------------------------------------------------------------------------------
    # Green LED 2 Control Method
    #--------------------------------------------------------------------------------------------------------
    def green_LED2_Control(self, ONOFF):
        if debug:
            print "green_LED2_Control(%s)" % ONOFF
        self.topLabelText.set("Green LED 2 (%s)" % ONOFF)

        if ONOFF == True:
            self.myCanvasLeft.itemconfig(self.myGreenLED2, fill = self.myLiteGreen)
        elif ONOFF == False:
            self.myCanvasLeft.itemconfig(self.myGreenLED2, fill = self.myDarkGreen)
        else:
            print "Error in function green_LED2_Control"

        self.myCanvasLeft.update()

    #--------------------------------------------------------------------------------------------------------
    # Green LED 3 Control Method
    #--------------------------------------------------------------------------------------------------------
    def green_LED3_Control(self, ONOFF):
        if debug:
            print "green_LED3_Control(%s)" % ONOFF
        self.topLabelText.set("Green LED 3 (%s)" % ONOFF)

        if ONOFF == True:
            self.myCanvasLeft.itemconfig(self.myGreenLED3, fill = self.myLiteGreen)
        elif ONOFF == False:
            self.myCanvasLeft.itemconfig(self.myGreenLED3, fill = self.myDarkGreen)
        else:
            print "Error in function green_LED3_Control"

        self.myCanvasLeft.update()

#############################################################################################################
#                                   Main Program
#############################################################################################################

def main():
    #frameMyFrame = MyFrame()
    #frameMyFrame. mainloop()
    MyFrame().mainloop()
    #print

if __name__ == "__main__":
    main()

#############################################################################################################

