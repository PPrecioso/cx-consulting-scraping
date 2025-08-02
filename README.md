#  CX Consulting Scraper

Este projeto foi criado para automatizar a coleta dos **serviços, descrições e funcionalidades** oferecidas no site da [CX Consulting](https://www.cxconsulting.com.br/).  
Com ele, você pode visualizar rapidamente tudo que a empresa disponibiliza de forma organizada.

---

##  O que o projeto faz
-  Acessa automaticamente o site da CX Consulting.  
-  Coleta os títulos dos serviços.  
-  Captura as descrições de cada serviço.  
-  Lista todas as funcionalidades associadas.  
-  Exibe tudo de forma direta no terminal.  

---

## 🛠️ Tecnologias utilizadas
- [Python 3.13+](https://www.python.org/)  
- [Selenium](https://pypi.org/project/selenium/)  
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)  
- [Requests](https://pypi.org/project/requests/)  
- ChromeDriver ou EdgeDriver  

---

## 📂 Estrutura do projeto
```plaintext
CX-Consulting-Scraper/
│
├── main.py              # Script principal
├── requirements.txt     # Dependências do projeto
└── README.md            # Documentação
```

---

## ⚙️ Como configurar

### Criar e ativar o ambiente virtual
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1   # Windows
# ou
source venv/bin/activate      # Linux/Mac
```
---

### Instalar as dependências
```bash
pip install -r requirements.txt
```
---

## ▶️ Como executar
```bash
python main.py
```
---

Se tudo estiver certo, você verá algo assim no terminal:

```plaintext
Acessando a página...

=== Serviços ===

Outsourcing de TI  
 Times sob demanda, com alta performance técnica e cultural para acelerar a entrega e escalar sua operação.  
  ➤ Funcionalidades:
    - Alocação de especialistas validados (Dev, QA, PO, UX, Cloud, Data, etc.)
    - Modelos flexíveis: remoto, híbrido ou presencial conforme sua necessidade
    - Gestão dedicada ou compartilhada, com KPIs de entrega e eficiência
    ...
--------------------------------------------------
