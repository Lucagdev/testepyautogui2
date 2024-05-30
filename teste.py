from pyvirtualdisplay import Display
import pyautogui
import time

# Iniciar o display virtual
display = Display(0)
display.start()

# Seu código PyAutoGUI aqui
time.sleep(2)  # Tempo para garantir que o display virtual está pronto
pyautogui.write('Hello world!')
pyautogui.press('enter')

# Parar o display virtual
display.stop()
