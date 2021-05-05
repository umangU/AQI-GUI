#importing relevant libraries
from tkinter import *
import tkinter as tk
ozone = sulfur = other = None
ozoneAQI = sulfurAQI = otherAQI = None
AQI = None

#calculating AQI
def calculate_AQI():
    global AQI
    global ozoneAQI
    global sulfurAQI
    global otherAQI

    try:
        inputVal = ozone.get()
        ozoneAQI = 100 * (inputVal/8.0)

        inputVal = sulfur.get()
        sulfurAQI = 100 * (inputVal/20.0)

        inputVal = other.get()
        otherAQI = 100 * (inputVal/25.0)

        if(ozoneAQI > sulfurAQI and ozoneAQI > otherAQI):
            AQI.set(ozoneAQI)
        elif(sulfurAQI > ozoneAQI and sulfurAQI > otherAQI):
            AQI.set(sulfurAQI)
        elif(otherAQI > sulfurAQI and otherAQI > ozoneAQI):
            AQI.set(otherAQI)

    except:
        pass

#root window
root = tk.Tk()
root.title("AQI GUI")
root.geometry("500x200+25+25")

ozone = tk.DoubleVar()
sulfur = tk.DoubleVar()
other = tk.DoubleVar()

AQI = tk.DoubleVar()

AQI.set(0.0)


labelOz = tk.Label(root, text="Ozone: ")
entryOz = tk.Entry(root, textvariable=ozone)
labelSulfur = tk.Label(root, text="Sulfur Dioxide: ")
entrySulfur = tk.Entry(root, textvariable=sulfur)
labelOther = tk.Label(root, text="Particles less than 2.5 micrometre diameter: ")
entryOther = tk.Entry(root, textvariable=other)
labelOz.grid(row=0, column=0)
entryOz.grid(row=0, column=1)
labelSulfur.grid(row=1, column=0)
entrySulfur.grid(row=1, column=1)
labelOther.grid(row=2, column=0)
entryOther.grid(row=2, column=1)

button1 = Button(root,text='Calculate AQI', command=calculate_AQI, font='Verdana',fg='blue')
button1.grid(row=3, column=0)

labelAQI = tk.Label(root, text="AQI: ")
labelAQI.grid(row=4, column=0)
labelDisplay = tk.Label(root, textvariable=AQI)
labelDisplay.grid(row=4, column=1)
