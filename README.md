# Bot Discord com Integração ao Google Calendar

Este é um bot para Discord que permite listar e criar eventos diretamente no Google Calendar, utilizando comandos no servidor Discord.

---

## Funcionalidades

- **Listar eventos do Google Calendar**: Mostra todos os eventos do mês atual.
- **Adicionar eventos ao Google Calendar**: Cria eventos no calendário através de comandos personalizados no Discord.

---

## Preview do funcionamento
![](preview/preview.gif)

***_Tá bem ruim mas dar para ver! kkk_

---


## Requisitos

### Tecnologias Utilizadas

- [Python 3.10+](https://www.python.org/)
- [Discord.py](https://discordpy.readthedocs.io/)
- [Google API Client](https://developers.google.com/api-client-library/python)
- [dotenv](https://pypi.org/project/python-dotenv/)

### Crie seu ambiente virtual (.env) e ative

Crie seu ambiente virtual com o seguinte comando:

```bash
python -m venv .venv
```

Após ative o mesmo:
```bash
.venv\Scripts\activate
```


### Dependências

Instale as dependências necessárias com o seguinte comando:

```bash
pip install -r requirements.txt
```

### Crie uma pasta 
```
na raiz do projeto chamada: credenciais
```


### Configuração do Ambiente

1. Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```env
# Caminho para o arquivo de token gerado pelo Google API
#(Esse arquivo vem automatico após a primeira autenticação do google)
TOKEN_CALENDAR='.\\credenciais\\token.json' 

# Caminho para o arquivo de credenciais baixado do Google Cloud Console
CREDENCIAIS_CALENDAR='.\\credenciais\\nome_do_arquivo.json'

#Token do bot Discord
TOKEN_DISCORD = SEU_TOKEN_DO_DISCORD
```

2. Substitua `SEU_TOKEN_DO_DISCORD` pelo token do seu bot Discord. Para mais informações sobre como criar um bot Discord, consulte a [documentação oficial](https://discord.com/developers/docs/intro).

3. Configure as credenciais da API Google:
   - Crie um projeto no [Google Cloud Console](https://console.cloud.google.com/).
   - Ative a API do Google Calendar.
   - Baixe o arquivo `credentials.json` e mova-o para o caminho especificado no `.env`.

* Recomendo ver esse tutorial gerado pelo ChatGPT:[Clique aqui]( https://chatgpt.com/share/67694807-9d60-8003-8b91-2c560b3d0d0d)
<br/> _OBS: Vá até a parte 2 e coloque o seu email na parte de "usuários de testes"_


## Como Usar

1. **Iniciar o Bot**

   Execute o script principal:

   ```bash
   python main.py
   ```

2. **Comandos Disponíveis**

   - **`/listar`**: Lista todos os eventos do mês atual no Google Calendar.
   - **`/agendar`**: Cria um novo evento no Google Calendar.
     - **Parâmetros:**
       - `titulo` (obrigatório): Título do evento.
       - `inicio` (obrigatório): Horário de início no formato `AAAA-MM-DDTHH:MM`.
       - `termino` (obrigatório): Horário de término no formato `AAAA-MM-DDTHH:MM`.
       - `descricao` (opcional): Descrição do evento.
       - `local` (opcional): Localização do evento.

---

## Estrutura do Projeto

```
.
├── calendar_google
│   ├── autenticacao_google.py  # Autenticação com a API do Google Calendar
│   ├── listar_eventos.py       # Funções para listar eventos do calendário
│   └── criar_evento.py         # Funções para criar eventos no calendário
├── cogs
│   ├── slash_agenda_lista.py   # comando slash no discord para listar eventos da agenda do mês atual
│   ├── slash_agenda.py         # comando slash no discord para abrir modal para criar evento, com ou sem horário
├── credenciais                 # Onde vão ficar os arquivos token e credenciais do google
├── main.py                     # Arquivo principal para executar o bot
├── requirements.txt            # Dependências do projeto
├── .env                        # Arquivo de configuração do ambiente
└── README.md                   # Documentação do projeto
```

---

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

1. Fork o repositório.
2. Crie uma branch para sua feature ou correção.
   ```bash
   git checkout -b minha-feature
   ```
3. Commit suas alterações.
   ```bash
   git commit -m "Adicionando minha feature"
   ```
4. Suba as alterações para o seu fork.
   ```bash
   git push origin minha-feature
   ```
5. Abra um Pull Request.

---

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---
