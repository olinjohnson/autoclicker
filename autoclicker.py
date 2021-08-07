import time
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener

delay = 0.01
button = Button.left
startstopkey = 'h'
exitkey = 'k'

class Mouse():
    def __init__(self):
        self.delay = delay
        self.running = True
        self.clicking = False
        self.mouse = Controller()
        self.button = button
        
    def start_stop_clicking(self):
        if self.clicking == True:
            self.clicking = False
        else:
            self.clicking = True
    
    def stop(self):
        self.running = False
            
    def run(self):
        while self.running:
            if self.clicking:
                self.mouse.click(button=self.button)
                time.sleep(delay)
    
def on_press(key):
    try:
        if key.char == startstopkey:
            print('Toggling clicking')
            m.start_stop_clicking()
        elif key.char == exitkey:
            print('Stopping clicking and key listener')
            m.stop()
            listener.stop()
    except:
        print('Invalid key')
    
listener = Listener(on_press=on_press)
listener.start()

m = Mouse()
m.run()

listener.join()
