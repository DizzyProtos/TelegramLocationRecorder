import pickle
from datetime import datetime
from os import path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import constants
from Models.Locations import LocationCreateModel, LocationResponceModel, LocationUpdateModel


class GoogleSheetService:
    def __init__(self):
        self.SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        self.append_range = 'locations!A:E'
        self.all_data_range = 'locations'

        creds = None
        if path.exists(constants.google_token_file):
            with open(constants.google_token_file, 'rb') as token:
                creds = pickle.load(token)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(constants.google_credentials_path, self.SCOPES)
                creds = flow.run_local_server(port=0)
            with open(constants.google_token_file, 'wb') as token:
                pickle.dump(creds, token)

        self.service = build('sheets', 'v4', credentials=creds)

    def add_new_location(self, location: LocationCreateModel):
        values = [[
            location.chat_link,
            str(location.lat),
            str(location.long),
            '',
            datetime.now().timestamp()
        ]]
        body = {
            'values': values
        }
        request = self.service.spreadsheets().values().append(
            spreadsheetId=constants.google_sheet_id, range=self.append_range,
            valueInputOption='RAW', insertDataOption='INSERT_ROWS', body=body
        )
        responce = request.execute()
        is_successful = False
        row_number = 0
        if responce is not None and responce['updates']['updatedCells'] != 0:
            is_successful = True
            row_number = int(responce['updates']['updatedRange'][-1])
        return LocationResponceModel(
            is_succesful=is_successful,
            row_number=row_number
        )

    def get_last_comment_cell_by_chat_id(self, chat_link: str):
        request = self.service.spreadsheets().values().get(
            spreadsheetId=constants.google_sheet_id, range=self.all_data_range
        )
        rows = request.execute()
        last_row_number = 1
        for i, row in enumerate(rows['values']):
            if len(row) < 4:
                continue
            if row[0] == chat_link and row[3] == '':
                last_row_number = i + 1
        return 'locations!D{}:D{}'.format(last_row_number, last_row_number)

    def add_comment_for_last_location(self, location_update: LocationUpdateModel):
        comment_cell = self.get_last_comment_cell_by_chat_id(location_update.chat_link)
        body = {
            'values': [[location_update.comment]]
        }
        request = self.service.spreadsheets().values().update(
            spreadsheetId=constants.google_sheet_id, range=comment_cell,
            valueInputOption='RAW', body=body
        )
        responce = request.execute()
        return True
