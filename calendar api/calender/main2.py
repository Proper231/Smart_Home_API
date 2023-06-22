from __future__ import print_function

import datetime
import os.path
from pprint import pprint
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

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
#response = SERVICE.calendars().insert(body=request_body).execute()
#print(response)



#delete calander
#SERVICE.calendars().delete(calendarId='ou1lal223ls2p2fdcdjb3p99jc@group.calendar.google.com').execute()

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

c_list =SERVICE.calendarList().list().execute()
for calendar_list_entry in c_list['items']:
            print (calendar_list_entry['summary'])
