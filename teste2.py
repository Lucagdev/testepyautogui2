from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configurar as opções do Chrome para executar em modo headless
chrome_options = Options()
#chrome_options.add_argument("--headless=new")

# Configurar o serviço do ChromeDriver usando o WebDriver Manager
webdriver_service = Service(ChromeDriverManager().install())

# Inicializar o driver do Chrome
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# Navegar para o Google
driver.get("https://www.google.com")
driver.maximize_window()
# Localizar o campo de pesquisa e digitar "notebook usado comprar"
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("notebook usado comprar")

# Submeter o formulário de pesquisa
search_box.submit()
time.sleep(3)
driver.save_screenshot("google.png")
time.sleep(2)
# Fechar o navegador
driver.quit()