from PIL import Image
import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL")

img = Image.open("data/img1.jpg")

# r = requests.get(API_BASE_URL+"/test")
with open("data/img1.jpg", "rb") as img_file:
    files = {"image": img_file}
    r = requests.post(API_BASE_URL+"/image", files=files)

    print(r.text)