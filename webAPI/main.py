from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, UploadFile
import asyncio

from services.azure import AzureService

app = FastAPI()
azure = AzureService()

async def periodic_check():
    while True:
        azure.periodic_check()
        await asyncio.sleep(1)

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(periodic_check())

@app.get("/test")
def test():
    return "hello world"

@app.post("/image")
def create_image_job(image: UploadFile):
    caption = azure.get_image_caption(image.file)
    return {"caption": caption}

@app.get("image/{job_id}")
def get_image_results(job_id: int):
    