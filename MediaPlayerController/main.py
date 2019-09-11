from pynput import keyboard
from pynput.keyboard import Key, Controller
import potplayer

volume_max = 1000
volume_min = 0

volume_data = 100
volume_range = volume_max - volume_min
volume_section = 5


# initiate object
key_press = Controller()
playlist = potplayer.PlayList()



def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
        # start potplayer

        if key.char == 'p':
            potplayer.run(r"music\\amelie_ost.mp3")

        # volume control potplayer
        if (key.char == 'w'):
            key_press.press(Key.up)
            key_press.release(Key.up)
        if (key.char == '-'):
            key_press.press(Key.left)
            key_press.release(Key.left)
        if (key.char == 'v'):
            key_press.press(Key.down)
            key_press.release(Key.down)
        if (key.char == 'd'):
            key_press.press(Key.right)
            key_press.release(Key.right)

        # play / pause
        if (key.char == 'r'):
            key_press.press(Key.space)
            key_press.release(Key.space)
        # mute / unmute
        if (key.char == 'o'):
            key_press.press('m')
            key_press.release('m')
        if (key.char == 'q'):
            potplayer.kill()

        # with key_press.pressed(Key.shift):
        #     if (key.char == 'm'):
        #         key_press.press('m')
        #         key_press.release('m')

        # at 0% volume
        if volume_data <= (volume_range / 5):
            key_press.press(Key.up)
            key_press.press(Key.up)
            key_press.press(Key.up)
            key_press.press(Key.up)
            key_press.release(Key.up)
            print("volume at 0%-20%")
        # at 20% volume
        if volume_data > (volume_range / 5) and volume_data <= (volume_range / 5) * 2:
            print("volume at 20%-40%")
        # at 40% volume
        if volume_data > (volume_range / 5) * 2 and volume_data <= (volume_range / 5) * 3:
            print("volume at 40%-60%")
        # at 60% volume
        if volume_data > (volume_range / 5) * 3 and volume_data <= (volume_range / 5) * 4:
            print("volume at 60%-80%")
        # at 100% volume
        if volume_data > (volume_range / 5) * 4:
            print("volume at 80%-100%")

    except AttributeError:
        print('special key {0} pressed'.format(key))


def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        potplayer.kill()
        return False


# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener: listener.join()
