from evdev import InputDevice, categorize, ecodes
import psutil
from subprocess import Popen

#creates object 'gamepad' to store the data
#you can call it whatever you like
# you will need to check /dev/input for your specific device name like eventXX
gamepad = InputDevice('/dev/input/event15')

#button code variables (change to suit your device)
# More information from https://core-electronics.com.au/tutorials/using-usb-and-bluetooth-controllers-with-python.html
button1 = 316
button2 = 315

# Process to look for to kill when BOTH keys are pressed
procName = '/usr/games/PCSX2'

#loop and filter by event code and print the mapped label
for event in gamepad.read_loop():
    if event.type == ecodes.EV_KEY:
        if event.value == 1:
            # Button 1 pressed
            if event.code == button1:
                for event2 in gamepad.read_loop():
                    # button 2 pressed
                    if event2.code == button2:
                        print("PS Button and Start Pressed")
                        for process in psutil.process_iter():
                            if procName in process.cmdline():
                                print('Process found. Terminating it.')
                                process.terminate()
                                exit()
                                break