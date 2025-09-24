from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd
import os
from dotenv import load_dotenv

# ==== CARREGA VARIÁVEIS DE AMBIENTE ====
load_dotenv()
USUARIO = os.getenv("USUARIO")
SENHA = os.getenv("SENHA")
REGIAO = os.getenv("REGIAO", "528")  # default 528

# ==== CONFIGURAÇÕES ====
URL_LOGIN = "https://www.sgaf.org.br/site/default.aspx"

# ==== INICIA O CHROME ====
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 30)

# LOGIN
driver.get(URL_LOGIN)
driver.find_element(By.ID, "login").send_keys(USUARIO)
driver.find_element(By.NAME, "senha").send_keys(SENHA)
driver.find_element(By.ID, "ctl00_ContentPlaceHolder1_btSubmit").click()
print("✅ Login realizado com sucesso!")

# (continua igual seu código de navegação, scraping e exportação...)
