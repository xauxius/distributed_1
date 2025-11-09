import os
import sys
from dotenv import load_dotenv

load_dotenv()

class Config:
    WEB_API_BASE_URL: str
    IMAGES_PATH: str
    
    def __init__(self):
        self.WEB_API_BASE_URL = os.getenv("WEB_API_BASE_URL") or self._missing("WEB_API_BASE_URL")
        self.IMAGES_PATH = os.getenv("IMAGES_PATH") or self._missing("IMAGES_PATH")
    
    @staticmethod
    def _missing(var_name: str):
        sys.exit(f"Missing required environment variable: {var_name}")

config = Config()