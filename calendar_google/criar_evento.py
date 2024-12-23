from googleapiclient.discovery import build
from calendar_google.autenticacao_google import authenticate_google


def criar_evento(start_datetime, end_datetime, summary, description="", location="", all_day=False):
    """Cria um evento no Google Calendar."""
    try:
        service = build('calendar', 'v3', credentials=authenticate_google())

        if all_day:
            # Configura evento de dia inteiro
            event = {
                'summary': summary,
                'location': location,
                'description': description,
                'start': {
                    'date': start_datetime.strftime('%Y-%m-%d'),
                    'timeZone': 'America/Sao_Paulo',
                },
                'end': {
                    'date': end_datetime.strftime('%Y-%m-%d'),
                    'timeZone': 'America/Sao_Paulo',
                },
            }
        else:
            # Configura evento com horários específicos
            event = {
                'summary': summary,
                'location': location,
                'description': description,
                'start': {
                    'dateTime': start_datetime.isoformat(),
                    'timeZone': 'America/Sao_Paulo',
                },
                'end': {
                    'dateTime': end_datetime.isoformat(),
                    'timeZone': 'America/Sao_Paulo',
                },
                'reminders': {
                    'useDefault': False,
                    'overrides': [
                        {'method': 'email', 'minutes': 24 * 60},
                        {'method': 'popup', 'minutes': 10},
                    ],
                },
            }

        created_event = service.events().insert(calendarId='primary', body=event).execute()
        return created_event.get('htmlLink')
    except Exception as e:
        print(f"Erro ao criar evento: {e}")
        return None
