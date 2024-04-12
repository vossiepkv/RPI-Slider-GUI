##imports 
from tkinter import * 
import tkinter.font 
from gpiozero import LED
import RPi.GPIO
from gpiozero import PWMLED
RPi.GPIO.setmode(RPi.GPIO.BCM)

##Hardware definition  

ledRed = PWMLED(17) ## board pin 11
ledBlue = PWMLED(27) ## board pin 13
ledGreen = PWMLED(22) ## board pin 15

##GUI Definitions 
win = Tk()
win.title("Multi LED PWM Slider")
myfont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")
myFontTitle = tkinter.font.Font(family = 'Helvetica', size = 22, weight = "bold")

# Slider change function
def update_led(led, value):
    led.value = value


##Event Functions

def close():
  RPi.GPIO.cleanup()
  win.destroy()


##Widgets 

titleText = Label(win, text = "Multi-Color LED Slider", font = myFontTitle)
titleText.grid(row=0, column=2, pady=10)

Label(win, text="Red LED", font=myfont, fg="red").grid(row=1, column=1)
red_slider = Scale(win, from_=0, to=1, resolution=0.01, orient=HORIZONTAL, command=lambda value: update_led(ledRed, float(value)))
red_slider.grid(row=2, column=1)

Label(win, text="Blue LED", font=myfont, fg="blue").grid(row=1, column=2)
blue_slider = Scale(win, from_=0, to=1, resolution=0.01, orient=HORIZONTAL, command=lambda value: update_led(ledBlue, float(value)))
blue_slider.grid(row=2, column=2)

Label(win, text="Green LED", font=myfont, fg="green").grid(row=1, column=3)
green_slider = Scale(win, from_=0, to=1, resolution=0.01, orient=HORIZONTAL, command=lambda value: update_led(ledGreen, float(value)))
green_slider.grid(row=2, column=3)

Label(win, text="Change the brightness of your LED's with the silders above", font=myfont).grid(row=3, column=2, pady=20)

##Exit button
exitButton = Button(win, text = 'Exit', font = myfont, command = close, bg = 'red', height = 1, width = 6)
exitButton.grid(row= 4, column=3, pady=10)

win.protocol("WM_DELETE_WINDOW", close) 

win.mainloop()
