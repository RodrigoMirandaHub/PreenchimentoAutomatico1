import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Caminho para o driver do Chrome
caminho_driver = "drivers/chromedriver.exe"
service = Service(caminho_driver)
navegador = webdriver.Chrome(service=service)

# Acessa o site do desafio
navegador.get("https://www.rpachallenge.com/")
print("✅ Página carregada com sucesso.")

# Espera até o botão Start estar visível e clicável (por no máximo 15 segundos)
try:
    botao_start = WebDriverWait(navegador, 15).until(
        EC.element_to_be_clickable((By.XPATH, '//button[text()="Start"]'))
    )
    botao_start.click()
    print("✅ Botão Start clicado.")
except Exception as erro:
    print("❌ Erro ao encontrar o botão Start:", erro)
    navegador.quit()
    exit()

# Carrega os dados do Excel
tabela = pd.read_excel("clientes.xlsx")

# Loop para preencher os dados de cada linha
for linha in tabela.index:
    nome = tabela.loc[linha, "Nome"]
    sobrenome = tabela.loc[linha, "Sobrenome"]
    empresa = tabela.loc[linha, "Empresa"]
    cargo = tabela.loc[linha, "Cargo"]
    endereco = tabela.loc[linha, "Endereco"]
    email = tabela.loc[linha, "Email"]
    telefone = str(tabela.loc[linha, "Telefone"])

    navegador.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelFirstName"]').send_keys(nome)
    navegador.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelLastName"]').send_keys(sobrenome)
    navegador.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelCompanyName"]').send_keys(empresa)
    navegador.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelRole"]').send_keys(cargo)
    navegador.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelAddress"]').send_keys(endereco)
    navegador.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelEmail"]').send_keys(email)
    navegador.find_element(By.CSS_SELECTOR, '[ng-reflect-name="labelPhone"]').send_keys(telefone)

    navegador.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

# Depois de preencher tudo
print("✅ Preenchimento automático finalizado.")
input("Pressione Enter para fechar o navegador...")

navegador.quit()
