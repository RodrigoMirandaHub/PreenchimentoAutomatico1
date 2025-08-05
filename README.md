##Automação RPA Challenge
Este projeto automatiza o preenchimento do desafio do site rpaChallenge utilizando Python, Selenium e Pandas.

##Como usar
Instale as dependências:

bash
Copiar
Editar
pip install selenium pandas openpyxl
Coloque o chromedriver.exe na pasta drivers/ (verifique se a versão do ChromeDriver é compatível com seu navegador Chrome).

##Prepare uma planilha Excel chamada clientes.xlsx com as seguintes colunas:

Nome

Sobrenome

Empresa

Cargo

Endereco

Email

Telefone

Execute o script:

bash
Copiar
Editar
python PreenchimentoAutomatico.py

O script abrirá o navegador, acessará o site, clicará em Start e preencherá automaticamente os dados da planilha.

##Observações
O script utiliza WebDriverWait para esperar que os elementos da página estejam carregados antes de interagir, o que é mais confiável que usar time.sleep().

Após o preenchimento, o script espera que você pressione Enter antes de fechar o navegador, para que você possa visualizar o resultado.