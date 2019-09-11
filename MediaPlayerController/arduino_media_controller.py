import serial
import time
import potplayer
from pynput import keyboard
from pynput.keyboard import Key, Controller

key_press = Controller()

volume_max = 1300
volume_min = 4000

volume_data = 801
volume_range = volume_min - volume_max
volume_section = 5


ISON = False
ser = serial.Serial('COM3', baudrate=115200, timeout=1)
time.sleep(3)
while 1:
    arduinoData = ser.readline()
    print(arduinoData)
    data = arduinoData.decode("utf-8").rstrip()

    print(data)
    if data == 'a':
        time.sleep(1)
        if ISON:
            ISON = False
        else:
            ISON = True
        if ISON:
            potplayer.run(r"music\\amelie_ost.mp3")
        if not ISON:
            potplayer.kill()

    if data == 'b':
        key_press.press('m')
        key_press.release('m')
    if data == 'd':
        key_press.press(Key.space)
        key_press.release(Key.space)
    if data == 'c':
        key_press.press(Key.left)
        key_press.release(Key.left)
    if data == 'e':
        key_press.press(Key.right)
        key_press.release(Key.right)

        # at 100% volume
    # if volume_data < (volume_range / 5):
    #     key_press.press(Key.up)
    #     key_press.press(Key.up)
    #     key_press.press(Key.up)
    #     key_press.press(Key.up)
    #     key_press.release(Key.up)
    #     print("volume at 80%-100%")
    #     # at 80% volume
    # if volume_data > (volume_range / 5) and volume_data <= (volume_range / 5) * 2:
    #
    #     print("volume at 60%-80%")
    #     # at 60% volume
    # if volume_data > (volume_range / 5) * 2 and volume_data <= (volume_range / 5) * 3:
    #     print("volume at 40%-60%")
    #     # at 40% volume
    # if volume_data > (volume_range / 5) * 3 and volume_data <= (volume_range / 5) * 4:
    #     print("volume at 20%-40%")
    #     # at 20% volume
    # if volume_data >= (volume_range / 5) * 4:
    #     print("volume at 0%-20%")

        # potplayer.run(r"music\\amelie_ost.mp3")




def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False


# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener: listener.join()
