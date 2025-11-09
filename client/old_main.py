from PIL import Image
import requests
from dotenv import load_dotenv
import os
import sys

load_dotenv()

WEB_API_BASE_URL: str = os.getenv("WEB_API_BASE_URL") or sys.exit("No URL configured")

img = Image.open("data/img1.jpg")

# r = requests.get(API_BASE_URL+"/test")
with open("data/img1.jpg", "rb") as img_file:
    files = {"image": img}
    print(type(img))
    r = requests.post(WEB_API_BASE_URL+"/image-analysis", data={"username": "steve"}, files=files)

    print(r.text)