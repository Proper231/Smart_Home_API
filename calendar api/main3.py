from pprint import pprint
from Google import Create_Service

CLIENT_SECRET_FILE = 'credentials.json'
API_NAME = 'calendar'
API_VERSION = 'V3'
SCOPES = ['https://www.googleapis.com/auth/calendar']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

#request


#add calendar
def create_calendar(request_body):
    response = service.calendars().insert(body=request_body).execute()
    print(response)


#delete calander
def delete_calendar(calendarId):
    service.calendars().delete(calendarId).execute()

"test token for security"    
'''
#list calanders    
def list_calendars():
    page_token = None
    while True:
        calendar_list = service.calendarList().list(pageToken=page_token).execute()
        for calendar_list_entry in calendar_list['items']:
            print (calendar_list_entry['summary'])
        page_token = calendar_list.get('nextPageToken')
        if not page_token:
            break
'''

#same as above but without token
def list_calendars():
    c_list = service.calendarList().list().execute()
    for calendar_list_entry in c_list['items']:
                print (calendar_list_entry['summary'])
