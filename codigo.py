#abrir o sistema da empresa
#https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time     
pyautogui.PAUSE = 1.5

#abrir o navegador  (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

#entrar no site do sistema

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

#aqui pode ser que ele demore alguns segundos para carregar o site
time.sleep(3)

#fazer login

pyautogui.click(x=-1268, y=374)
pyautogui.write("alvis.cleo@gmail.com")

pyautogui.press("tab")
pyautogui.write("123456")

pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)         

#abrir/importar a base de dados de produtos para cadastrar

import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela)

#cadastrar um produto

for linha in tabela.index:  
          
        codigo = str(tabela.loc[linha, "codigo"])
        #clica no campo do código do produto
        pyautogui.click(x=-1301, y=251)
        #preencher o codigo
        pyautogui.write(codigo)
        #passar para o próximo campo
        pyautogui.press("tab")
        #marca
        pyautogui.write( str(tabela.loc[linha, "marca"]))
        #passar para o próximo campo
        pyautogui.press("tab")
        #tipo
        pyautogui.write( str(tabela.loc[linha, "tipo"]))
        #passar para o próximo campo
        pyautogui.press("tab")
        #categoria
        pyautogui.write( str(tabela.loc[linha,"categoria"]))
        #passar para o próximo campo
        pyautogui.press("tab")
        #preço
        pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
        #passar para o próximo campo
        pyautogui.press("tab")
        #custo
        pyautogui.write(str(tabela.loc[linha, "custo"]))
        #passar para o próximo campo
        pyautogui.press("tab")
        #obs
        obs = str(tabela.loc[linha, "obs"])
        if obs != "nan":
                pyautogui.write(obs)
        #passar para o próximo campo
        pyautogui.press("tab")
        #apertar o botão
        pyautogui.press("enter")

        pyautogui.scroll(5000)
