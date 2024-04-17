import pyautogui
import time

def press_f11():
    pyautogui.press('f11')
    
def press_f12():
    pyautogui.press('f12')

def press_ctrl_arrow():
        pyautogui.keyDown('ctrl')
        pyautogui.press('left')
        pyautogui.keyUp('ctrl')
        time.sleep(0.1)

        pyautogui.keyDown('ctrl')
        pyautogui.press('right')
        pyautogui.keyUp('ctrl')
        time.sleep(0.1)

        pyautogui.keyDown('ctrl')
        pyautogui.press('up')
        pyautogui.keyUp('ctrl')
        time.sleep(0.1)

        pyautogui.keyDown('ctrl')
        pyautogui.press('down')
        pyautogui.keyUp('ctrl')
        time.sleep(0.1)
    
time.sleep(5)
try:
    print('Programa iniciado')
    while True:
        press_f11()
        time.sleep(1)
        press_f12()
        time.sleep(1)
        press_ctrl_arrow()
        time.sleep(1)
except pyautogui.FailSafeException:
    print('Programa encerrado')
