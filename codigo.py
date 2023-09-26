# Passo a passo do projeto.
# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui # para intalar = pip install pyautogui (no terminal)
import time

# Abrir o chrome 

pyautogui.PAUSE = 0.3

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Entrar no link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# Esperar o site carregar
time.sleep(3)

# Passo 2: fazer login.
pyautogui.click(x=620, y=363)
pyautogui.write("botautomacao@gmail.com")

pyautogui.press("tab") # passar para o campo de senha
pyautogui.write("minhasenha")

pyautogui.press("tab") # passar para o botão que conclui o login
pyautogui.press("enter")

time.sleep(3)

# passo 3: importar a base de dados de produtos.
# instalar pandas = pip install pandas numpy openpyxl (no terminal)
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index: #(identação "dar um "tab" no que for para executar varias vezes)
    #for coluna in tabela.colunms: (tambem pode ser feito assim)
    # Passo 4: cadastrar 1 produto.
    pyautogui.click(x=575, y=250) # clicando para iniciar cadastro do produto.

    codigo = tabela.loc[linha, "codigo"]
    marca = tabela.loc[linha, "marca"]
    tipo = tabela.loc[linha, "tipo"]
    categoria = tabela.loc[linha, "categoria"]
    preco_unitario = tabela.loc[linha, "preco_unitario"]
    custo = tabela.loc[linha, "custo"]
    

    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    pyautogui.write(str(preco_unitario))
    pyautogui.press("tab")
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs): # if(se) colocando uma condição para corriguir o erro. 
        #se não é "nan" como está na tabela "pandas", então escreve...
        pyautogui.write(str(obs))

    pyautogui.press("tab") # passando para o botão de salvar cadastro
    pyautogui.press("enter") # cadastrando o produto

    pyautogui.scroll(50000)

    #ou tambem pode ser feito assim

    # codigo = tabela.loc[linha, "codigo"]

    # pyautogui.write(str(codigo))
    # pyautogui.write(str(tabela.loc[linha, "marca"]))
    # pyautogui.press("tab")
    # pyautogui.write(str(tabela.loc[linha, "tipo"]))
    # pyautogui.press("tab")
    # pyautogui.write(str(tabela.loc[linha, "categoria"]))
    # pyautogui.press("tab")
    # pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    # pyautogui.press("tab")
    # pyautogui.write(str(tabela.loc[linha, "custo"]))
    # pyautogui.press("tab")
    # obs = tabela.loc[linha, "obs"]


# Passo 5: repetir o cadastro para todos os produtos.