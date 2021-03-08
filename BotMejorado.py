import pyautogui as pg
import webbrowser as web
import time
import pandas as pd

data = pd.read_csv("datos.csv")
data_dict = data.to_dict('list')
celulares = data_dict['celular']
first = True
for celular in celulares:
  print(celular)
  web.open("https://web.whatsapp.com/send?phone="+celular)
  #   time.sleep(8)
  if first:
      time.sleep(3)
      first=False
  time.sleep(8)
  pg.write('Hola, esto es un mensaje automatico')
  pg.press('enter')
  time.sleep(6)
  pg.hotkey('ctrl','w')