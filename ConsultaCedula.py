import pyautogui
import webbrowser as web
import time as tm
import pandas as pd


def posventa():

    web.open_new_tab("http://staff.tigo.com.co/CRMPortal/auth/portal/default/Postventa")
    tm.sleep(2)
    pyautogui.click(102, 731)  # Transacciones
    pyautogui.click(116, 802)  # Mod Linea
    pyautogui.scroll(-200)
    pyautogui.click(187, 995)  # Mod Linea
    pyautogui.click(1617, 503)  # Campo linea
    tm.sleep(1)
    pyautogui.press('down')
    pyautogui.press('enter')


def consultaCedula():
    web.open_new_tab("http://staff.tigo.com.co/CRMPortal/auth/portal/default/Consultas")
    tm.sleep(2)
    pyautogui.click(103, 566)  # Consulta Pos
    tm.sleep(0.1)
    pyautogui.click(113, 616)  # Integral
    tm.sleep(0.1)
    pyautogui.click(215, 834)  # Nueva p
    tm.sleep(0.5)
    if contador==0:
        pyautogui.click(1440, 477)  # Limpiar
        tm.sleep(1)
    pyautogui.click(1154, 493)  # Campo linea
    pyautogui.hotkey('ctrl', 'v')
    tm.sleep(0.2)
    pyautogui.click(1338, 484)  # Buscar
    tm.sleep(4)
    pyautogui.moveTo(944, 640)#Pos ini
    pyautogui.mouseDown();
    pyautogui.moveTo(1185, 640)  # Pos fin del click
    pyautogui.mouseUp()
    pyautogui.hotkey('ctrl', 'c')
    tm.sleep(0.1)
    pyautogui.click(1440, 477)  # Limpiar
    pyautogui.click(1432, 488)  # Limpiar
    pyautogui.hotkey('ctrl', 'w')

def pegarEnTabla():
    pyautogui.click(399, 16)#Pestaña
    tm.sleep(0.2)
    pyautogui.press('right')
    pyautogui.hotkey('ctrl', 'v')

def bajarYcopiarIz():
    pyautogui.press('down')
    pyautogui.press('left')
    pyautogui.hotkey('ctrl', 'c')

def bajarYcopiarDer():
    pyautogui.press('down')
    pyautogui.press('right')
    pyautogui.hotkey('ctrl', 'c')





#Main
tm.sleep(2)
contador = 0
filas = 5
pyautogui.click(164, 400) #Maximo 6 pestañas
while(contador<filas):
    bajarYcopiarIz()
    consultaCedula()
    pegarEnTabla()
    contador=contador+1

