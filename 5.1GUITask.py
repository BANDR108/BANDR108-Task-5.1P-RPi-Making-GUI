##imports 
from tkinter import * 
import tkinter.font 
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

##Hardware definition

ledRed = LED(17) ## board pin 11
ledYellow = LED(27) ## board pin 13
ledGreen = LED(22) ## board pin 15

##GUI Definitions 
win = Tk()
win.title("LED Toggler")
myfont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

##Event Functions
def redToggle():
  if ledRed.is_lit:
    ledRed.off()
    LEDRedButton["text"] = "Turn  LED On"
  else:
    ledRed.on()
    LEDRedButton["text"] = "Turn Red LED Off"

def yellowToggle():
  if ledYellow.is_lit:
    ledYellow.off()
    LEDYellowButton["text"] = "Turn Blue LED On"
  else:
    ledYellow.on()
    LEDYellowButton["text"] = "Turn Blue LED Off"

def greenToggle():
  if ledGreen.is_lit:
    ledGreen.off()
    LEDGreenButton["text"] = "Turn Green LED On"
  else:
    ledGreen.on()
    LEDGreenButton["text"] = "Turn Green LED Off"

def close():
  RPi.GPIO.cleanup()
  win.destroy()


##Widgets 

LEDRedButton = Button(win, text = 'Turn Red LED On', font = myfont, command = redToggle, bg = 'bisque2', height = 1, width = 24)
LEDRedButton.grid(row=0, column=1)

LEDYellowButton = Button(win, text = 'Turn Yellow LED On', font = myfont, command = yellowToggle, bg = 'bisque2', height = 1, width = 24)
LEDYellowButton.grid(row=0, column=2)

LEDGreenButton = Button(win, text = 'Turn Green LED On', font = myfont, command = greenToggle, bg = 'bisque2', height = 1, width = 24)
LEDGreenButton.grid(row=0, column=3)


##Exit button
exitButton = Button(win, text = 'Exit', font = myfont, command = close, bg = 'red', height = 1, width = 6)
exitButton.grid(row= 1, column=3)

win.protocol("WM_DELETE_WINDOW", close) 

win.mainloop()
