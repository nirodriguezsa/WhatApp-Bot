import pyautogui as pg
import webbrowser as web
import time as tm
import pandas as pd

def attachPDF():
    #Change the x, y position for each click, using the currentMouseX, currentMouseY = pg.position () function
    pg.click(762, 1330) #Attach
    tm.sleep(1)
    pg.click(767, 1019)  #Clik on type Document
    tm.sleep(2)
    pg.click(146, 306)  #Open mis documentos
    tm.sleep(1)
    pg.click(342, 569)  #Select PDF
    tm.sleep(1)
    pg.click(1723, 1242)  # Open
    tm.sleep(5)
    pg.click(2053, 1183)  # Send



data = pd.read_csv("Test.csv")
data_dict = data.to_dict('list')
celulares = data_dict['celular']
#duo = zip(celulares,mensajes)
first = True
for numero in celulares:
    web.open("https://web.whatsapp.com/send?phone="+numero+"&text=¡Hola! Mi nombre es Nicolas, asesor de Tigo, su línea " + numero[3:] + " tiene un beneficio único, que consiste en un descuento a su plan actual por adquirir una _segunda línea pospago_, en resumen, *por el mismo precio que esta pagando actualmente, tendría ¡dos líneas pospago!* Escríbame si desea conocer más acerca de este beneficio.")
    if first:
        tm.sleep(3)
        first = False
    tm.sleep(8)
    pg.press("enter")
    attachPDF()
    tm.sleep(7)
    pg.hotkey('ctrl','w')
print("Script ejecutado correctamente")