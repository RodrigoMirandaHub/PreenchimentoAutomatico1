# 🤖 Automação RPA Challenge

Este projeto automatiza o preenchimento do desafio do site [RPA Challenge](https://rpachallenge.com/) utilizando **Python**, **Selenium** e **Pandas**.

---

## ⚙️ Como usar

### 1. Instale as dependências:

```bash
pip install selenium pandas openpyxl
2. Coloque o chromedriver.exe na pasta drivers/
Certifique-se de que a versão do ChromeDriver seja compatível com seu navegador Chrome.

📄 Prepare uma planilha Excel chamada clientes.xlsx com as seguintes colunas:
Nome

Sobrenome

Empresa

Cargo

Endereco

Email

Telefone

▶️ Execute o script:
bash
Copy
Edit
python PreenchimentoAutomatico.py
O script:

Abre o navegador

Acessa o site

Clica em "Start"

Preenche automaticamente os dados da planilha

🧠 Observações

Ao final, o script espera que você pressione Enter antes de fechar o navegador, para que você possa visualizar o resultado.

✍️ Autor
Rodrigo Miranda
GitHub
