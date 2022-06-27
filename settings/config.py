import os

# google api
API: list = ["https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]
KEY: str = "service_account.json"
SHEETS_ID: str = "1sGHQJbqp8FTRafJuMtyDR_aNh6kVGp_27Fj-yG7TqBY"
USA_UNIQUE_CODE: str = "R01235"

# database
localhost = os.getenv("HOST")
user = "developer_1"
port = "5432"
password = os.getenv("PASSWORD")
db_name = "test"

pass
