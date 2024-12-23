import datetime
from googleapiclient.discovery import build
from calendar_google.autenticacao_google import authenticate_google

def listagem_calendar():
    """Lista os eventos do calendário do mês atual."""
    # Obtém as credenciais
    creds = authenticate_google()

    # Conexão com a API do Google Calendar
    service = build('calendar', 'v3', credentials=creds)

    # Obter a data atual com timezone UTC
    now = datetime.datetime.now(datetime.timezone.utc)
    start_of_month = datetime.datetime(now.year, now.month, 1).isoformat() + 'Z'
    next_month = now.month % 12 + 1
    end_of_month = datetime.datetime(now.year + (now.month // 12), next_month, 1).isoformat() + 'Z'

    # Convertendo o número do mês para o nome dele em Português
    meses_em_portugues = [
        "", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ]
    nome_mes = meses_em_portugues[now.month]

    # Buscar eventos no calendário principal
    events_result = service.events().list(
        calendarId='primary',
        timeMin=start_of_month,
        timeMax=end_of_month,
        singleEvents=True,
        orderBy='startTime'
    ).execute()
    events = events_result.get('items', [])

    # Retornar eventos formatados
    if not events:
        return f"Nenhum evento encontrado para o mês de {nome_mes}/{now.year}."
    else:
        eventos_formatados = [f"{event['start'].get('dateTime', event['start'].get('date'))} - {event['summary']}" for event in events]
        return f"Eventos para o mês de {nome_mes}/{now.year}:\n" + "\n".join(eventos_formatados)
