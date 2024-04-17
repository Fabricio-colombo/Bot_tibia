import keyboard
import time

def press_f11():
    keyboard.press_and_release('f11')
    
def press_f12():
    keyboard.press_and_release('f12')

def press_arrows():
    keyboard.press_and_release('left_arrow')
    time.sleep(0.1)
    keyboard.press_and_release('right_arrow')
    time.sleep(0.1)
    keyboard.press_and_release('up_arrow')
    time.sleep(0.1)
    keyboard.press_and_release('down_arrow')
    time.sleep(0.1)

time.sleep(5)
while True:
    press_f11()
    time.sleep(1)
    press_f12()
    time.sleep(1)
    press_arrows()
    time.sleep(1)
