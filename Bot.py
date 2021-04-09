import pyautogui as pg
import webbrowser as web
import time as tm
import pandas as pd

data = pd.read_csv("Test.csv")
data_dict = data.to_dict('list')
celulares = data_dict['celular']
first = True

for celular in celulares:
    web.open("https://api.whatsapp.com/send?phone="+celular+"&text=Hola que tal")
    if first:
        tm.sleep(3)
        first=False
    tm.sleep(8)
    pg.press("enter")
    tm.sleep(2)
    pg.hotkey('ctrl', 'w')
print("Script ejecutado correctamente")