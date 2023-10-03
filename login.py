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

