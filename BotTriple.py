import pyautogui as pg
import webbrowser as web
import time as tm
import pandas as pd

data = pd.read_csv("datos.csv")
data_dict = data.to_dict('list')
celulares = data_dict['celular']
planes = data_dict['plan']
anios = data_dict['tiempo']
informacion = zip(celulares,planes,anios)
first = True

for celular,plan,anio in informacion:
    web.open("https://web.whatsapp.com/send?phone="+celular+"&text=¡Hola! Mi nombre es Nicolas, asesor de Tigo, su línea " + celular[3:] + " tiene un plan "+plan+ " con más de "+str(anio)+" años de antigüedad y por ello cuenta con un *beneficio único*, que consiste en un descuento a su plan actual por adquirir una _segunda línea pospago_, en resumen, *por el mismo precio que esta pagando actualmente, tendría ¡dos líneas pospago!* Escríbame si desea conocer más acerca de este beneficio o si le gustaría que un asesor se comunicara para darle todos los detalles.")
    if first:
        tm.sleep(3)
        first=False
    tm.sleep(8)
    pg.press("enter")
    tm.sleep(2)
    pg.hotkey('ctrl', 'w')
print("Script ejecutado correctamente")