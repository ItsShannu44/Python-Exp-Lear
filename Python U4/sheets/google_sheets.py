#Code to handle the google_sheets

import gspread as gs
from google.oauth2.service_account import Credentials
from collections import Counter

SERVICE_ACCOUNT='service_account.json'
SHEET_URL='https://docs.google.com/spreadsheets/d/1zVoxZxxdoP5E25NbOKPlSq2Saj6wXgUjfrBgavm_huw/edit?gid=0#gid=0' #paste the url of the sheet which we want to access
WORKSHEET_NAME='API_DATA_Spreadsheet'
SCOPES=['https://googleapis.com/drive.readonly','https://googleapis.com/spreadsheets.readonly',]

def get_preferences():
    cred=Credentials.from_service_account_file(SERVICE_ACCOUNT,scopes=SCOPES) #loading cred from json
    client=gs.authorize(cred) #auth for client
    ss=client.open_by_url(SHEET_URL)
    ws=ss.worksheet9=(WORKSHEET_NAME)
    rows=ws.get_all_values()
    if not rows:
        raise RuntimeError('No data was found in the sheet')
    header=rows[0]
    data_rows=rows[1:]

    if 'ChannelPreference' not in header:
        raise RuntimeError('Column ChannelPreference not found in the header')

    idx=header.index('ChannelPreference')
    preferences=[]
    for r in data_rows:
        if len(r)>idx:
            val=r[idx].strip()
            if val!="":
                preferences.append(val)
    counts=Counter(preferences)
    print('Preferences:')
    for p in preferences:
        print(p)
    print("Preferences Count:")
    for k, v in counts.most_common():
        print(f'Preference {k}: {v}')

get_preferences()