from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
#import pandas as pd
import pygsheets
import bs4, requests
import datetime
import socket
import stun
from pprint import pprint
from googleapiclient import discovery


def main():
    external_ip, localip = getip()
    googelsheets(external_ip,localip)
    myIP = googelsheets(external_ip,localip)
    domainupdate(myIP)

def getip():
    nat_type, external_ip, external_port = stun.get_ip_info()
    g = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    g.connect(("8.8.8.8", 80))
    localip = g.getsockname()[0]
    external_ip = external_ip.replace('\'','')
    return external_ip, localip

def googelsheets(external_ip,localip):
  SCOPES = ['https://www.googleapis.com/auth/spreadsheets' + "https://www.googleapis.com/auth/drive" + "https://www.googleapis.com/auth/drive.file"]
  creds = None
  if os.path.exists('token.pickle'):
      with open('token.pickle', 'rb') as token:
          creds = pickle.load(token)
  if not creds or not creds.valid:
      if creds and creds.expired and creds.refresh_token:
          creds.refresh(Request())
      else:
          flow = InstalledAppFlow.from_client_secrets_file(
              '/opt/Scripts/credentials.json', SCOPES)
          creds = flow.run_local_server(port=0)
      # Save the credentials for the next run
      with open('token.pickle', 'wb') as token:
          pickle.dump(creds, token)

  service = build('sheets', 'v4', credentials=creds)
# The ID of the spreadsheet to update.
  spreadsheet_id = '1A6Z-PEu7epzraYr-LyW32MfEe7ZkitK1KtiGuGZrDxI'  # TODO: Update placeholder value.
  time= datetime.datetime.now()
  range_ = 'A2'
  value_input_option = 'RAW'
  value_range_body = {
    "values": [
      [
        external_ip,time.strftime("%d-%m-%Y %H:%M:%S"),localip
      ]
    ],
    "range": "A2"
  }
  myIP=external_ip.replace('\'','')
  request = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id, range=range_, valueInputOption=value_input_option, body=value_range_body)
  response = request.execute()
  return myIP


def domainupdate(myIP):
    API_HOST = 'dns.ardis.ru'
    DOMAIN = 'xxxxx.ru'
    IP1 = myIP
    EMAIL = 'xx@p-xxx.com'
    LOGIN = 'xxxxx:xxxx'
    PASS = 'xxxx'
    response = requests.get('https://'+API_HOST+'/dnsmgr?func=domain.record.edit&elid=&plid='+DOMAIN+'&name=%40&ttl=3600&rtype=a&ip='+IP1+'&domain=&srvdomain=&priority=&weight=&port=&value=&email=&caa_flags=0&caa_tag=issue&caa_value_domain=&caa_value_email=&ds_key_tag=&ds_algorithm=8&ds_digest_type=1&ds_digest=&clicked_button=ok&progressid=false&sok=ok&authinfo='+LOGIN+':'+PASS+'&out=json')
    response1 = requests.get('https://cp.p-dns.com/dnsmgr?func=domain.record.get&elid=madxleon.ru&plid=madxleon.ru&clicked_button=ok&progressid=false&sok=ok&authinfo=$LOGIN:$PASS&out=json')
    pprint(response1)
    pprint(myIP)
    return

main()
