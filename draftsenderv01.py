import os.path

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.compose']

creds = None

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
    # create gmail api client
    service = build('gmail', 'v1', credentials=creds)
    tosend = service.users().drafts().list(userId="me", q="mission").execute()
    drafts = tosend["drafts"]
    print("# of drafts: " + str(tosend["resultSizeEstimate"]))

    for email in drafts:
        try:
            sent = service.users().drafts().send(userId="me", body=email).execute()
            print("sent message: " + str(sent["id"]))
        except HttpError as error:
            print("Email not sent:" + str(email["id"]) + str(error))
        finally:
            continue

except HttpError as error:
    print(F'An error occurred: {error}')