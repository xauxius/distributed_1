import os
import sys
from dotenv import load_dotenv

load_dotenv()

class Config:
    WAITING = "wait"
    WAIT_TIME = 10
    CHECK_INTERVAL = 1

    PRIMARY_KEY: str
    AZURE_URL: str

    def __init__(self):
        self.PRIMARY_KEY = os.getenv("PRIMARY_KEY") or self._missing("PRIMARY_KEY")
        self.AZURE_URL = os.getenv("AZURE_URL") or self._missing("AZURE_URL")
    
    @staticmethod
    def _missing(var_name: str):
        sys.exit(f"Missing required environment variable: {var_name}")

config = Config()