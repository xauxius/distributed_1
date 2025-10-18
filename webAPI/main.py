from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, UploadFile
import asyncio

from services.azure import AzureClient
from services.job_scheduler import JobScheduler

CHECK_INTERVAL = 1

app = FastAPI()
azure = AzureClient()
scheduler = JobScheduler(azure)

async def periodic_check():
    while True:
        scheduler.check()
        await asyncio.sleep(CHECK_INTERVAL)

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(periodic_check())

@app.get("/test")
def test():
    return "hello world"

@app.post("/image")
async def create_image_job(image: UploadFile):
    image_data = await image.read()
    caption = await azure.get_image_caption(image_data)
    print(type(image_data))
    return {"caption": caption}

@app.get("image/{job_id}")
def get_image_results(job_id: int):
    pass