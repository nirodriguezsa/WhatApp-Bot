import pyautogui as pg
import webbrowser as web
import time as tm
import pandas as pd

data = pd.read_csv("datos.csv")
data_dict = data.to_dict('list')
celulares = data_dict['celular']
direcciones = data_dict['direccion']
cedulas = data_dict['cedula']
informacion = zip(celulares,direcciones,cedulas)
first = True

for celular,direcciones,cedulas in informacion:
    web.open("https://api.whatsapp.com/send?phone=+57"+str(celular)+"&text=¡Hola!, mi nombre es Nicolas, asesor de Tigo, su servicio hogar instalado en la dirección "+direcciones+" bajo cédula "+str(cedulas)+" tiene un un *beneficio único*, que consiste en adquirir un plan móvil con nosotros, con el primer mes gratis y el doble de megas en planes desde 45 mil pesos con ¡*50 GB* y minutos ilimitados! Escríbame si desea conocer más acerca de este beneficio o si le gustaría que un asesor se comunicara para darle todos los detalles.")
    tm.sleep(2)
    if first:
        tm.sleep(8)
        first=False
    tm.sleep(4)
    pg.press("enter")
    tm.sleep(1)
    pg.hotkey('alt','tab')
    tm.sleep(0.2)
    pg.hotkey('ctrl', 'w')
print("Script ejecutado correctamente")