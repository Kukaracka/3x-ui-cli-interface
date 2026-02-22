import os
from dotenv import load_dotenv

load_dotenv()
HOST = os.getenv("HOST")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

XUI_EXTERNAL_IP = "your.domain.com"
SERVER_PORT = 56478
VERIFY_SSL = False
MAIN_REMARK = "console"
INBOUND_ID = 2
VERIFY_SSL = False  # для локальной разработки
