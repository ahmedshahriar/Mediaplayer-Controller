# import keyboard
import serial
import time
import potplayer
"""reference"""
# https://pyglet.readthedocs.io/en/pyglet-1.3-maintenance/
# https://pyautogui.readthedocs.io/en/latest/
# https://stackoverflow.com/questions/136734/key-presses-in-python
# https://github.com/michaelgundlach/mp3play

# error : reconnect the arduino

"""example"""

# keyboard.write('A',delay=0)

# if(pyautogui.press("p")):
#             potplayer.run("amelie_ost.mp3")


ser = serial.Serial('COM3', baudrate=115200, timeout=1)
time.sleep(3)
while 1:
    arduinoData = ser.readline()
    print(arduinoData)
