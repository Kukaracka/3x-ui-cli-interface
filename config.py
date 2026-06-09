import os
from dotenv import load_dotenv

load_dotenv()
HOST = os.getenv("HOST")
HOST_SUB = os.getenv("HOST_SUB")
INBOUND_ID = os.getenv("INBOUND_ID")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

VERIFY_SSL = False
MAIN_REMARK = "console"
INBOUND_ID = 2
