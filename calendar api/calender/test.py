from pprint import pprint
from Google import Create_Service

CLIENT_SECRET_FILE = 'credentials.json'
API_NAME = 'calendar'
API_VERSION = 'V3'
SCOPES = ['https://www.googleapis.com/auth/calendar']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

#request


request_body = {
    'summary' : 'Smart home test'
}

response = service.calendars().insert(body=request_body).execute()
print(response)
