import tkinter as tk

from clicker import ButtonController

START_STOP_KEY = '`'
EXIT_KEY = ']'

window = tk.Tk()
greeting = tk.Label(text="Automation")
greeting.pack()

bc = ButtonController(window)

button = tk.Button(
    text="Start/Stop",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
    command=bc.start_stop,
)

button_exit = tk.Button(
    text="Exit",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
    command=bc.exit,
)

button.pack()
button_exit.pack()

def handle_key_press(event):
    if (event.char == EXIT_KEY):
        print('Exiting, caught \']\'')
        bc.exit()
    if (event.char == START_STOP_KEY):
        print('Caught start key')
        bc.start_stop()

window.bind('<KeyRelease>', handle_key_press)
window.mainloop()
