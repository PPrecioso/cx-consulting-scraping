from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from colorama import Fore, Style, init
import time

# Inicializa o colorama
init(autoreset=True)

# URL do site da CX
URL = "https://www.cxconsulting.com.br/"

# Configura o Chrome
service = Service()
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(service=service, options=options)

print("Acessando a página...")
driver.get(URL)

# Aguarda carregar todo o conteúdo dinâmico
time.sleep(5)

# Captura o HTML da página e fecha o navegador
soup = BeautifulSoup(driver.page_source, "html.parser")
driver.quit()

# Busca os blocos de serviços
servicos = soup.select("div.bg-white\\/5")

if not servicos:
    print("Nenhum serviço encontrado. Verifique os seletores.")
else:
    print(f"\n{Fore.BLUE}=== CX Consulting ==={Style.RESET_ALL}\n")
    print(f"\n{Fore.BLUE}=== Serviços ==={Style.RESET_ALL}\n")
    for servico in servicos:

        titulo = servico.select_one("h3.text-xl")
        if titulo:
            print(f"{Fore.BLUE} {titulo.get_text(strip=True)}{Style.RESET_ALL}")

        descricao = servico.select_one("p.text-gray-300.mb-6")
        if descricao:
            print(f"{Fore.YELLOW}  {descricao.get_text(strip=True)}{Style.RESET_ALL}")

        funcoes = servico.select("ul.space-y-2 li")
        if funcoes:
            print("  ➤ Funcionalidades:")
            for item in funcoes:
                print(f"    - {item.get_text(strip=True)}")

        print("\n" + "-" * 50 + "\n")
