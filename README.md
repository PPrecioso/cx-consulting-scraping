# CX Consulting Scraper

This project was developed to automate the collection and display of services, detailed descriptions and features offered on the website of [CX Consulting](https://www.cxconsulting.com.br/).  
Additionally, it allows you to automatically translate all information into **Portuguese, English or Spanish**, making it easier to view in different languages directly on the terminal.
---

## ✨ What the project does

- Automatically accesses the CX Consulting website.
- Collects the titles of each service.
- Captures detailed descriptions.
- Lists all the features of each service.
- Translates all information into the selected language (**Portuguese, English, or Spanish**).
- Displays everything in a formatted and organized manner on the terminal.
  
---

## 🛠️ Technologies used
- [Python 3.13+](https://www.python.org/)  
- [Selenium](https://pypi.org/project/selenium/) – Browser automation
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/) – HTML data extraction
- [Colorama](https://pypi.org/project/colorama/) – Color display in the terminal
- [Deep-Translator](https://pypi.org/project/deep-translator/) – Text translation
- [Google Chrome + ChromeDriver](https://chromedriver.chromium.org/) – Browser and driver for Selenium 

---

## ⚙️ How to configure

### Create and activate the virtual environment

```bash
python -m venv venv

.\venv\Scripts\Activate.ps1   # Windows
# or
source venv/bin/activate      # Linux/Mac
```

### Install the dependencies
```bash
pip install -r requirements.txt
```

## ▶️ Running
```bash
python main.py
```

---

**In the terminal, you can choose the language:**

```bash
Select a language / Selecione um idioma / Seleccione un idioma:
1 - Portuguese
2 - English
3 - Spanish
```

**After selecting, the program will display something like:**

```bash
Accessing the page...

=== CX Consulting ===
=== Services ===

📌 IT Outsourcing
  On-demand teams with high technical and cultural performance to accelerate delivery and scale your operation.
    • Allocation of validated specialists (Dev, QA, PO, UX, Cloud, Data, etc.)
    • Flexible models: remote, hybrid or on-site as needed
    • Dedicated or shared management, with delivery and efficiency KPIs
...
--------------------------------------------------
```

## 💡 Notes

- The scraper uses Selenium, so it will open Chrome in headless mode (without a window).
- Loading time may vary depending on your internet connection.
- Translation is done automatically using Deep-Translator.
