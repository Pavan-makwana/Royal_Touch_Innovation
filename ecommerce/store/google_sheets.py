import gspread
import os
from oauth2client.service_account import ServiceAccountCredentials
from django.conf import settings
from datetime import datetime
from dotenv import load_dotenv

# .env file se variables load karne ke liye
load_dotenv()

def save_to_sheet(name, product, quantity, phone, email, message=""):
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]

    # .env se dictionary format mein credentials taiyar karna
    creds_dict = {
        "type": os.getenv("GS_TYPE"),
        "project_id": os.getenv("GS_PROJECT_ID"),
        "private_key_id": os.getenv("GS_PRIVATE_KEY_ID"),
        # Private key ke '\n' ko handle karna zaroori hai
        "private_key": os.getenv("GS_PRIVATE_KEY").replace('\\n', '\n'),
        "client_email": os.getenv("GS_CLIENT_EMAIL"),
        "client_id": os.getenv("GS_CLIENT_ID"),
        "auth_uri": os.getenv("GS_AUTH_URI"),
        "token_uri": os.getenv("GS_TOKEN_URI"),
        "auth_provider_x509_cert_url": os.getenv("GS_AUTH_PROVIDER_CERT_URL"),
        "client_x509_cert_url": os.getenv("GS_CLIENT_X509_CERT_URL")
    }

    try:
        # Dictionary se credentials load karna
        creds = ServiceAccountCredentials.from_json_keyfile_dict(creds_dict, scope)
        client = gspread.authorize(creds)
        
        # Tumhari original sheet ka naam
        sheet = client.open("Royal Touch Product Requests").sheet1

        sheet.append_row([
            datetime.now().strftime("%Y-%m-%d %H:%M"),
            name,
            product,
            quantity,
            phone,
            email,
            message
        ])
        return True
    except Exception as e:
        print(f"Google Sheets Error: {e}")
        return False