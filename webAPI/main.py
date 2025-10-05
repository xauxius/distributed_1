from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, UploadFile

from services.azure import AzureService

app = FastAPI()
azure = AzureService()

@app.get("/test")
def test():
    return "hello world"

@app.post("/image")
def image(image: UploadFile):
    caption = azure.get_image_caption(image.file)
    return {"caption": caption}