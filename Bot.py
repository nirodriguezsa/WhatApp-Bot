import pyautogui as pg
import webbrowser as web
import time as tm
import pandas as pd

data = pd.read_csv("datos.csv")
data_dict = data.to_dict('list')
celulares = data_dict['celular']
first = True


for celular in celulares:
    web.open("https://api.whatsapp.com/send?phone=+57"+str(celular)+"&text=¡Hola! Soy Nicolas asesor de Tigo, nos enteramos que pasaste tu línea con otro operador _Claro_, y nos encantaría que volvieras! es por ello que te damos una excelente oferta con planes desde *$35.000* con 15 GB de internet y 2 meses al 50% de descuento. Si te interesa escríbeme y te cuento los detalles!")
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