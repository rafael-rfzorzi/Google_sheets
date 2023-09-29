import gspread

class Google_data_auth:
    def login_data(self):
        self.spreadsheet_login_code = 'Enter authentication information here'
        self.keyjson = {
            "type": "service_account",
            "project_id": "Enter authentication information here",
            "private_key_id": "Enter authentication information here",
            "private_key": "Enter authentication information here",
            "client_email": "Enter authentication information here",
            "client_id": "Enter authentication information here",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_x509_cert_url": "Enter authentication information here",
            "universe_domain": "googleapis.com"}
        self.gc = gspread.service_account_from_dict(self.keyjson)