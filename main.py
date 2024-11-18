import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
import io
import cleaner


host = os.environ.get("host_name")  
user = os.environ.get("user_name")  
password = os.environ.get("password") 
database = os.environ.get("database")


scope = ["https://www.googleapis.com/auth/drive"]

# Load credentials from the downloaded JSON key file

credentials = ServiceAccountCredentials.from_json_keyfile_name('digital-explorers-041.json', scope)

# Build the Google Drive service
drive_service = build('drive', 'v3', credentials=credentials)

# Define your folder ID from Google Drive (You can get it from the folder URL)
folder_id = '1IvBc64vw5kIBsR82jqYqtQQBxa_2mvcJ'

# Fetch the list of CSV files in the folder
results = drive_service.files().list(q=f"'{folder_id}' in parents and mimeType='text/csv'",
                                     spaces='drive',
                                     fields='files(id, name)').execute()

files = results.get('files', [])

# Check if the folder contains files
if not files:
    print('No files found in the folder.')
else:
    print(f"Found {len(files)} files in the folder.")
