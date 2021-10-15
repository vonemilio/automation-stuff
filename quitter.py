from pynput.keyboard import Listener, KeyCode, Controller, Key

from ahk import AHK, keys 

ahk = AHK()

exit_key = KeyCode(char='[')
quitter_key = KeyCode(char='=')

def on_press(key):
    if key == quitter_key:
        print('Quitting ....')
        ahk.key_press(keys.ESCAPE)
        ahk.key_press('l')
        ahk.key_press(keys.ENTER)
        print('Done quitting....')
    elif key == exit_key:
        print('stopping')
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()