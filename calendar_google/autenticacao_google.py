import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

#variáveis de sistema
from dotenv import load_dotenv

SCOPES = ['https://www.googleapis.com/auth/calendar']


# Carregar variáveis de ambiente
load_dotenv(dotenv_path=".env")

def authenticate_google():
    """Autentica o usuário no Google API e retorna as credenciais."""
    creds = None
    token_path = os.getenv('TOKEN_CALENDAR', 'token.json')
    credentials_path = os.getenv('CREDENCIAIS_CALENDAR', 'credentials.json')

    if os.path.exists(token_path):
        creds = Credentials.from_authorized_user_file(token_path, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(credentials_path):
                raise FileNotFoundError(f"Arquivo de credenciais '{credentials_path}' não encontrado. \n")

            flow = InstalledAppFlow.from_client_secrets_file(credentials_path, SCOPES)
            creds = flow.run_local_server(port=0)

        with open(token_path, 'w') as token:
            token.write(creds.to_json())

    return creds
