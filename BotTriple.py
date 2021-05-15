import pyautogui as pg
import webbrowser as web
import time as tm
import pandas as pd

chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
data = pd.read_csv("datos.csv")
data_dict = data.to_dict('list')
celulares = data_dict['celular']
nombres = data_dict['nombre']
direcciones = data_dict['direccion']
informacion = zip(celulares,nombres,direcciones)
first = True

for celular,nombre,direccion in informacion:
    url = "https://api.whatsapp.com/send?phone=+57"+str(celular)+"&text=¡Hola "+nombre+"! Mi nombre es Nicolas, asesor de ventas Tigo, quiero contarte que tienes una _super oferta_ para que actives un plan pospago con tu línea "+str(celular)+" ya que por tener los servicios de hogar en la dirección "+direccion+", te damos *doble de GIGAS* en el plan móvil que tomes desde 45 mil pesos con el *PRIMER MES GRATIS* y 2 meses *al 50% de descuento*. También recibes una promo para tu hogar y es que *duplicamos tus MB* de velocidad sin costo adicional! Escríbeme si te interesa esta oferta"
    web.get(chrome_path).open(url)
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