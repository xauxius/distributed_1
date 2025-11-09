import asyncio
from pydantic import BaseModel
import time
from queue import Queue
from tempfile import SpooledTemporaryFile

from data_models import Status, Job
from config import config
from services import AzureClient

class JobScheduler:
    def __init__(self, azure_service: AzureClient):
        self.q: Queue[int] = Queue()
        self.t_start = time.time() - config.WAIT_TIME
        self.jobs: dict[int, Job] = {}

        self.azure_service = azure_service

        self.current_job_id = 0

    async def periodic_check(self):
        while True:
            await self.process_queue()
            await asyncio.sleep(config.CHECK_INTERVAL)

    async def process_queue(self):
        if self.is_job_ready() and not self.q.empty():
            self.t_start = time.time()

            job_id = self.q.get()
            job = self.jobs[job_id]
            
            caption = await self.azure_service.get_image_caption(job.image)
            job.result = caption
            job.status = Status.FINISHED if caption is not None else Status.FAILED

    def create_job(self, username: str, image: bytes) -> Job:
        job_id = self.get_new_job_id()

        status = self.check_status()
        job = Job(
            username=username,
            job_id=job_id,
            status=status,
            image=image,
            result=None
        )

        self.jobs[job_id] = job
        self.q.put(job_id)

        return job

    def get_job(self, job_id) -> Job | None:
        job = self.jobs.get(job_id)
        return job

    def check_status(self) -> Status:
        if self.is_job_ready() and self.q.empty():
            return Status.STARTED
        else:
            return Status.WAITING
        
    def get_jobs_by_user(self, username: str) -> list[Job]:
        filtered_jobs: list[Job] = []

        for key in self.jobs:
            job = self.jobs[key]
            if job.username == username:
                filtered_jobs.append(job)
        
        return filtered_jobs

    def is_job_ready(self) -> bool:
        return time.time() - self.t_start > config.WAIT_TIME

    def get_new_job_id(self) -> int:
        job_id = self.current_job_id
        self.current_job_id += 1
        return job_id    