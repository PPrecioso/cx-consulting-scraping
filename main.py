from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import time

URL = "https://www.cxconsulting.com.br/"

# Inicializa o navegador
service = Service()  # Vai usar o ChromeDriver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Roda sem abrir janela
driver = webdriver.Chrome(service=service, options=options)

print("Acessando a página...")
driver.get(URL)
time.sleep(5)  # Espera carregar o conteúdo dinâmico

# Captura o HTML renderizado
soup = BeautifulSoup(driver.page_source, "html.parser")
driver.quit()

servicos = soup.select("div.bg-white\\/5")
if not servicos:
    print("Nenhum serviço encontrado. Verifique os seletores.")
else:
    print("\n=== Serviços ===\n")
    for servico in servicos:
        titulo = servico.select_one("h3.text-xl")
        if titulo:
            print(f"📌 {titulo.get_text(strip=True)}")

        descricao = servico.select_one("p.text-gray-300.mb-6")
        if descricao:
            print(f"  {descricao.get_text(strip=True)}")

        funcoes = servico.select("ul.space-y-2 li")
        if funcoes:
            print("  ➤ Funcionalidades:")
            for item in funcoes:
                print(f"    - {item.get_text(strip=True)}")
        print("\n" + "-"*50 + "\n")
