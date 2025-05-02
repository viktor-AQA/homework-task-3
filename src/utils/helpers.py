import os
from dotenv import load_dotenv


load_dotenv()

AUTH_HEADERS = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json"
}

API_HEADERS = {
    "Content-Type": "application/json",
    "Accept": "application/json"
}

AUTH_DATA = {
    "username": os.getenv("AUTH_USERNAME"),
    "password": os.getenv("AUTH_PASSWORD"),
    "scope": "",
    "client_id": "",
    "client_secret": ""
}
