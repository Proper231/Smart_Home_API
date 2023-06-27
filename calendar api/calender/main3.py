from pprint import pprint
from Google import Create_Service, convert_to_RFC_datetime

CLIENT_SECRET_FILE = 'credentials.json'
API_NAME = 'calendar'
API_VERSION = 'V3'
SCOPES = ['https://www.googleapis.com/auth/calendar']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

#request
#request_body = {
#     'summary' :'Smart Home Test'
#}

#add calendar
def create_calendar(name_calendar):
    request_body = {
        'summary' : name_calendar
    }
    response = service.calendars().insert(body=request_body).execute()
    print(response)


#delete calander
def delete_calendar(ID):
    service.calendars().delete(calendarId = ID).execute()

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
#testing page token
'''
response = SERVICE.calendarList().list(
    maxResults = 250,
    showDeleted = False,
    showHidden = False
).execute()

calendarItems = response.get('items')
nextPageToken = response.get('nextPageToken')

while nextPageToken:
    response = SERVICE.calendarList().list(
        MaxResults = 250,
        showDeleted = False,
        showHidden = False,
        PageToken = nextPageToken
    ).execute()
    calendarItems.extend(response.get('items'))
    nextPageToken = response.get('nextPageToken')

print(calendarItems)
'''

#same as above but without token
def list_calendars():
    response = service.calendarList().list().execute()
    for calendar_list_entry in response['items']:
                print (calendar_list_entry['summary'])


def update_Calendar(oldName, newName, desc, location):
    oldName = oldName
    response = service.calendarList().list().execute()
    calendarItems = response.get('items')
    myCalendar = filter(lambda x: oldName in x['summary'], calendarItems)
    myCalendar = next(myCalendar)
    print(myCalendar)


    myCalendar['summary'] = 'tester'
    myCalendar['description'] == '2nd test'
    myCalendar['location'] == 'where'


    service.calendars().update(calendarId = myCalendar['id'], body = myCalendar).execute()

list_calendars()