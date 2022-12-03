from __future__ import print_function
import pickle
import os.path
import psycopg2
import pandas as pd
import pygsheets
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from pprint import pprint
from googleapiclient import discovery
from decimal import Decimal
import json
conn = psycopg2.connect(dbname='otrs', user='xxx', 
                        password='xxx', host='xx.xxx.xxx.x')
value = 0
cursor = conn.cursor()
cursor.execute('''select  cquota, cquota_2, period  from customer_company
where customer_id in ('Altuera','EOS', 'IDCollect','Ingos','leto', 'MoneyMan', 'multicarta', 'PremiumTorg', 'Twino')
order by customer_id''', (value,))
records = cursor.fetchall()
cursor.close()
conn.close()
pprint(records)
json_Altuera = json.dumps(records[0], ensure_ascii=False, default=str)
json_Altuera = json_Altuera.replace(']','').replace('[','').replace('"','').replace('.00','')
json_EOS = json.dumps(records[1], ensure_ascii=False, default=str)
json_EOS = json_EOS.replace(']','').replace('[','').replace('"','').replace('.00','')
json_IDCollect = json.dumps(records[2], ensure_ascii=False, default=str)
json_IDCollect= json_IDCollect.replace(']','').replace('[','').replace('"','').replace('.00','')
json_Ingos = json.dumps(records[3], ensure_ascii=False, default=str)
json_Ingos = json_Ingos.replace(']','').replace('[','').replace('"','').replace('.00','')
json_leto = json.dumps(records[4], ensure_ascii=False, default=str)
json_leto = json_leto.replace(']','').replace('[','').replace('"','').replace('.00','')
json_MoneyMan = json.dumps(records[5], ensure_ascii=False, default=str)
json_MoneyMan = json_MoneyMan.replace(']','').replace('[','').replace('"','').replace('.00','')
json_multicarta = json.dumps(records[6], ensure_ascii=False, default=str)
json_multicarta = json_multicarta.replace(']','').replace('[','').replace('"','').replace('.00','')
json_PremiumTorg = json.dumps(records[7], ensure_ascii=False, default=str)
json_PremiumTorg = json_PremiumTorg.replace(']','').replace('[','').replace('"','').replace('.00','')
json_Twino = json.dumps(records[8], ensure_ascii=False, default=str)
json_Twino = json_Twino.replace(']','').replace('[','').replace('"','').replace('.00','')


json_data = json.dumps(records, ensure_ascii=False, default=str)
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
creds = None
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'F:\WorkSpace\Learn\Python\credentials.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)

service = build('sheets', 'v4', credentials=creds)
# The ID of the spreadsheet to update.
spreadsheet_id = '1T-0ufqSUEogDlTnP5sST-kdeBEjteL0iJElL1uzHEh4'  # TODO: Update placeholder value.
range_ = "K2"
value_input_option = 'RAW'

value_range_body = {
  "values": [[json_Altuera],[json_EOS],[json_IDCollect],[json_Ingos],[json_leto],[json_MoneyMan],[json_multicarta],[json_PremiumTorg],[json_Twino]
              ]
}

request = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id, range=range_, valueInputOption=value_input_option, body=value_range_body )
response = request.execute()
pprint(response)


















