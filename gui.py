import tkinter as tk
from threading import Thread

from pynput.keyboard import Listener, KeyCode

from clicker import ButtonController, start_stop_key, exit_key

START_STOP_KEY = '`'
EXIT_KEY = ']'

window = tk.Tk()
greeting = tk.Label(text="Automation")
greeting.pack()

bc = ButtonController(window)

button_start = tk.Button(
    text="Start",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
    command=bc.toggle_on,
)

button_stop = tk.Button(
    text="Stop",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
    command=bc.toggle_off,
)

button_exit = tk.Button(
    text="Exit",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
    command=bc.exit,
)

button_start.pack()
button_stop.pack()
button_exit.pack()

click_thread = bc.click_thread

def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()

listener = Listener(on_press=on_press)
listener.start()

window.mainloop()