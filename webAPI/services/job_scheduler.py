import asyncio
# from pydantic import BaseModel
import time
from queue import Queue
from tempfile import SpooledTemporaryFile

from data_models import Status
from constants import WAIT_TIME

class Job:
    user_id: int
    job_id: int
    status: Status
    image: SpooledTemporaryFile
    result: str | None

class JobScheduler:
    def __init__(self, azure_service):
        self.q = Queue()
        self.t_start = time.time() - WAIT_TIME
        self.jobs = {}

        self.azure_service = azure_service

        self.current_job_id = 0

    async def check(self):
        if self.is_job_ready() and not self.q.empty():
            self.t_start = time.time()

            job_id = q.dequeue()
            job = self.jobs[job_id]
            
            caption = await self.azure_service.get_image_caption(job.image)

            self.jobs[job_id] = caption

            return 

    def create_job(user_id, image):
        pass

    def is_job_ready(self):
        return time.time() - self.t_start > WAIT_TIME

    def get_new_job_id(self):
        job_id = self.current_job_id
        self.current_job_id += 1
        return job_id

    def enqueue_job(self, user_id, job_id, image):
        job_id = self.get_new_job_id()
        self.q.enqueue({"user_id": user_id, "image": image, "job_id": job_id})

    