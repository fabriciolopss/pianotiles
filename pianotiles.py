import pyautogui
import keyboard
import time
import win32api, win32con
jogoComeçou = True
noPianotiles = False

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

                         
print ("Bot funcionando, aperte Y quando começar um jogo de piano tiles e aperte X para cancelar o funcionamento do bot")

while jogoComeçou:
    while not keyboard.is_pressed("space") and noPianotiles == True:
        try:
            if pyautogui.pixel(910,669)[0] == 0: 
                click(910,669)
            if pyautogui.pixel(1060,669)[0] == 0: 
                click(1060,669)
            if pyautogui.pixel(1200,669)[0] == 0: 
                click(1200,669)
            if pyautogui.pixel(1342,669)[0] == 0: 
                click(1342,669)
        except:
            print("Erro!")
        if keyboard.is_pressed("x"):
            quit()
    if keyboard.is_pressed("Y"): 
        noPianotiles = True