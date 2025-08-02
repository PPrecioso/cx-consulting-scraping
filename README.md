# CX Consulting Scraper

Este projeto foi desenvolvido para automatizar a coleta e exibição dos serviços, descrições detalhadas e características oferecidos no site da [CX Consulting](https://www.cxconsulting.com.br/).  
Além disso, ele permite traduzir automaticamente todas as informações para **Português, Inglês ou Espanhol**, facilitando a visualização em diferentes idiomas diretamente no terminal.

---

## ✨ O que o projeto faz
- Acessa automaticamente o site da CX Consulting.  
- Coleta os títulos de cada serviço.  
- Captura as descrições detalhadas.  
- Lista todas as características de cada serviço.  
- Traduz todas as informações para o idioma selecionado (**Português, Inglês ou Espanhol**).  
- Exibe tudo de forma formatada e organizada no terminal.  

---

## 🛠️ Tecnologias utilizadas
- [Python 3.13+](https://www.python.org/)  
- [Selenium](https://pypi.org/project/selenium/) – Automação do navegador  
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/) – Extração de dados do HTML  
- [Colorama](https://pypi.org/project/colorama/) – Exibição colorida no terminal  
- [Deep-Translator](https://pypi.org/project/deep-translator/) – Tradução de texto  
- [Google Chrome + ChromeDriver](https://chromedriver.chromium.org/) – Navegador e driver para o Selenium  

---

## ⚙️ Como configurar

### Criar e ativar o ambiente virtual
```bash
python -m venv venv

.\venv\Scripts\Activate.ps1   # Windows
# ou
source venv/bin/activate      # Linux/Mac
```

### Instalar as dependências
```bash
pip install -r requirements.txt
```

## ▶️ Executando
```bash
python main.py
```

---

**No terminal, você poderá escolher o idioma:**

```bash
Select a language / Selecione um idioma / Seleccione un idioma:
1 - Portuguese
2 - English
3 - Spanish
```

**Após selecionar, o programa exibirá algo como:**

```bash
Accessing the page...

=== CX Consulting ===
=== Services ===

📌 IT Outsourcing
  On-demand teams with high technical and cultural performance to accelerate delivery and scale your operation.
    • Allocation of validated specialists (Dev, QA, PO, UX, Cloud, Data, etc.)
    • Flexible models: remote, hybrid or on-site as needed
    • Dedicated or shared management, with delivery and efficiency KPIs
--------------------------------------------------
```

## 💡 Observações

- O scraper utiliza Selenium, então abrirá o Chrome em modo headless (sem janela).
- O tempo de carregamento pode variar dependendo da sua conexão com a internet.
- A tradução é feita automaticamente usando Deep-Translator.
