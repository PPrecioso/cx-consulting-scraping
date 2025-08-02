from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from colorama import Fore, Style, init
from deep_translator import GoogleTranslator
import time

init(autoreset=True)

URL = "https://www.cxconsulting.com.br/"

# Language options
languages = {
    "1": {"name": "Portuguese", "services": "Serviços", "bullet": "•", "code": "pt"},
    "2": {"name": "English", "services": "Services", "bullet": "•", "code": "en"},
    "3": {"name": "Spanish", "services": "Servicios", "bullet": "•", "code": "es"}
}

# Language selection menu
print(Fore.BLUE + "Select a language / Selecione um idioma / Seleccione un idioma:")
print("1 - Portuguese")
print("2 - English")
print("3 - Spanish")

choice = input(Fore.YELLOW + "Enter the option number: ").strip()

if choice not in languages:
    print(Fore.RED + "Invalid option. Defaulting to Portuguese.")
    choice = "1"

selected_lang = languages[choice]

# Translator instance
translator = GoogleTranslator(source="auto", target=selected_lang["code"])

# Configure Chrome 
service = Service()
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(service=service, options=options)

print(Fore.BLUE + "Accessing the page...")
driver.get(URL)
time.sleep(5)

# Get HTML and close browser
soup = BeautifulSoup(driver.page_source, "html.parser")
driver.quit()

# Select service blocks
services = soup.select("div.bg-white\\/5")

if not services:
    print(Fore.RED + "No services found. Check the selectors.")
else:
    print(Fore.BLUE + f"\n=== CX Consulting ===\n")
    print(Fore.BLUE + f"=== {selected_lang['services']} ===\n")

    for service in services:
        title = service.select_one("h3.text-xl")
        if title:
            print(Style.BRIGHT + Fore.WHITE + f"📌 {translator.translate(title.get_text(strip=True))}")

        description = service.select_one("p.text-gray-300.mb-6")
        if description:
            print(Fore.LIGHTWHITE_EX + f"  {translator.translate(description.get_text(strip=True))}")

        features = service.select("ul.space-y-2 li")
        if features:
            for item in features:
                print(Fore.YELLOW + f"    {selected_lang['bullet']} " + Fore.LIGHTWHITE_EX + translator.translate(item.get_text(strip=True)))

        print(Fore.BLUE + "\n" + "-" * 50 + "\n")
