from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Scopes for Google Calendar
SCOPES = ['https://www.googleapis.com/auth/calendar']

# Authenticate and create a service
def main():
    creds = None
    # Load credentials from file or authenticate if not available
    flow = InstalledAppFlow.from_client_secrets_file("C:/Users/Robert Frank/Desktop/Coding\Python/UntisToCalender/src/credentials.json", SCOPES)
    creds = flow.run_console(port=0)

    service = build('calendar', 'v3', credentials=creds)

    # List the next 10 events from the primary calendar
    events_result = service.events().list(calendarId='primary', maxResults=10).execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])

if __name__ == '__main__':
    main()