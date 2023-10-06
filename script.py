import pandas
import pyautogui
import time


pyautogui.PAUSE = 0.3

search_navegator = input("Digite o nome do navegador que deseja usar: ")
user_email = input("Digite seu email: ")
user_password = input("Digite sua senha: ")

time.sleep(5)


print("Estou iniciando automação...")

pyautogui.press("win")
pyautogui.write(search_navegator)
pyautogui.press("enter")

time.sleep(2)

link_search = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.write(link_search)
pyautogui.press("enter")

time.sleep(10)

print("Esperando os site carregar...")
pyautogui.press("tab")
pyautogui.write(user_email)
pyautogui.press("tab")
pyautogui.write(user_password)
pyautogui.press("tab")
pyautogui.press("enter")

print("Login finalizado")
print("Iniciando cadastro!")

table = pandas.read_csv("prods.csv")

for row in table.index:

    codigo = table.loc[row, "codigo"]
    marca = table.loc[row, "marca"]
    tipo = table.loc[row, "tipo"]
    categoria = table.loc[row, "categoria"]
    preco_unitario = table.loc[row, "preco_unitario"]
    custo = table.loc[row, "custo"]
    obs = table.loc[row, "obs"]

    time.sleep(3)
    pyautogui.click()
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    pyautogui.press(str(preco_unitario))
    pyautogui.press("tab")
    pyautogui.write(str(custo))
    pyautogui.press("tab")
    pyautogui.write(str(obs))
    pyautogui.press("tab")
    pyautogui.press("enter")


    pyautogui.scroll(50000)



