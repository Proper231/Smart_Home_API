from __future__ import print_function
import requests
import datetime
import os.path
from pprint import pprint
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from pprint import pprint
from Google import Create_Service, convert_to_RFC_datetime

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']

#authenticate user
def authenticate_google():

    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)


    except HttpError as error:
        print('An error occurred: %s' % error)

    return service

SERVICE = authenticate_google()

#request
request_body = {
    'summary' : 'Smart home test'
}

#add calander
def create_calendar(name_calendar):
    request_body = {
        'summary' : name_calendar
    }
    response = SERVICE.calendars().insert(body=request_body).execute()
    print(response)




#delete calander
def delete_calendar(ID):
    SERVICE.calendars().delete(calendarId = ID).execute()

#list calanders    
'''
def list_calendars():
    page_token = None
    while True:
        calendar_list = SERVICE.calendarList().list(pageToken=page_token).execute()
        for calendar_list_entry in calendar_list['items']:
            print(calendar_list_entry['summary'])
        page_token = calendar_list.get('nextPageToken')
        if not page_token:
            break
'''
'''
def list_calendars():
    c_list =SERVICE.calendarList().list().execute()
    for calendar_list_entry in c_list['items']:
                print (calendar_list_entry['summary'])
'''
def list_calendars():
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

    pprint(calendarItems)


def update_Calendar(oldName, newName, desc, location):
    oldName = oldName
    response = SERVICE.calendarList().list().execute()
    calendarItems = response.get('items')
    myCalendar = filter(lambda x: oldName in x['summary'], calendarItems)
    myCalendar = next(myCalendar, 'end')
    print(myCalendar)


    myCalendar['summary'] = newName
    myCalendar['description'] == desc
    myCalendar['location'] == location


    SERVICE.calendars().update(calendarId = myCalendar['id'], body = myCalendar).execute()


#update_Calendar('chicken', 'testing', 'hello world', 'paris, france')
#create an Event
'''
colors = SERVICE.colors().get().execute()
pprint(colors)

hour_adjustment = -8
event_request_body = {

    'start' : {
        'datetime' : convert_to_RFC_datetime(2023, 6, 22, 1, 12 + hour_adjustment, 30 ),
        'timeZome' : 'Europe, Spain'
    },
    'end': {
        'datetime' : convert_to_RFC_datetime(2023, 6, 22, 1, 14 + hour_adjustment, 30 ),
        'timeZome' : 'Europe, Spain'
    },

    'summary' : "weird test", 
    'description' : 'Testing',
    'colorId' : 5,
    'status' : 'confirmed',
    'transparency' : 'opaque',
    'visibiltiy' : 'private',
    'location' : 'Zaragoza, Spain'
}
'''
def add_event (summary, location, description, startTime, endtime):
    event = {
    'summary': summary,
    'location': location,
    'description': description,
    'start': {
        'dateTime': startTime,
        'timeZone': 'Europe/Madrid',
    },
    'end': {
        'dateTime': endtime,
        'timeZone': 'Europe/Madrid',
    },
    'reminders': {
        'useDefault': False,
        'overrides': [
        {'method': 'email', 'minutes': 24 * 60},
        {'method': 'popup', 'minutes': 10},
        ],
    },
    }

    event = SERVICE.events().insert(calendarId='primary', body=event).execute()
    print ('Event created: %s' % (event.get('htmlLink')))
#time format
#'2023-06-28T09:00:00'


add_event('testing add event', 'univerity', 'testing', '2023-06-28T09:15:00', '2023-06-28T21:30:00')
