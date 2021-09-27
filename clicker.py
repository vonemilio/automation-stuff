import pynput
import random

import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

#delay = 0.001
delay = 0.001
button = Button.right
start_stop_key = KeyCode(char='`')
exit_key = KeyCode(char=']')

def generate_random_range():
    return random.uniform(0.001, 0.003)

class ClickMouse(threading.Thread):
    def __init__(self, mouse, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.mouse = mouse
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                self.mouse.click(self.button)
                time.sleep(self.delay())
            time.sleep(0.1)


class ButtonController:
    def __init__(self, window):
       self.window = window
       self.start_clicker()

    def start_clicker(self):
        mouse = Controller()
        self.click_thread = ClickMouse(mouse, generate_random_range, button)
        self.click_thread.start()

    def start_stop(self):
        if self.click_thread.running:
            self.click_thread.stop_clicking()
            print('Stopping clicker')
        else:
            self.click_thread.start_clicking()
            print('Starting clicker')
    
    def exit(self):
        self.click_thread.exit()
        self.window.quit()