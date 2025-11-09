from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, UploadFile, Form, File, HTTPException
import asyncio

from services import AzureClient, JobScheduler
from data_models import JobResponse, CreateJobRequest, ManyJobsResponse

app = FastAPI()
azure = AzureClient()
scheduler = JobScheduler(azure)

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(scheduler.periodic_check())

@app.get("/test")
def test():
    return "hello world"

@app.post("/image-analysis")
async def create_image_job(username: str = Form(...), image: UploadFile = File(...)):
    print(image.filename)
    image_data = await image.read()
    job = scheduler.create_job(username, image_data)
    job_response = JobResponse.map_from_job(job)
    return job_response
    

@app.get("/image-analysis/single/{job_id}")
def get_image_results(job_id: int):
    job = scheduler.get_job(job_id)

    if job:
        job_response = JobResponse.map_from_job(job)
        return job_response
    else:
        raise HTTPException(status_code=404, detail="Job not found")

@app.get("/image-analysis/all/{username}")
def get_all_results(username: str):
    jobs = scheduler.get_jobs_by_user(username)

    jobs_response = ManyJobsResponse.map_all(jobs)
    return jobs_response