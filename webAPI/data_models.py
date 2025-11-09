from typing_extensions import Unpack
from pydantic import BaseModel, ConfigDict
from enum import Enum

def status_to_str(status):
    match status:
        case Status.WAITING:
            return "waiting"
        case Status.STARTED:
            return "started"
        case Status.FINISHED:
            return "finished"
        case Status.FAILED:
            return "failed"
        case _:
            return "unknown"

class Status(Enum):
    WAITING = 1
    STARTED = 2
    FINISHED = 3
    FAILED = 4

class Job(BaseModel):
    username: str
    job_id: int
    status: Status
    image: bytes
    result: str | None

class JobResponse(BaseModel):
    # model_config = ConfigDict(exclude_none=True)
    job_id: int
    status: str
    result: str | None = None

    @staticmethod
    def map_from_job(job: Job):
        return JobResponse(
            job_id = job.job_id,
            status = status_to_str(job.status),
            result = job.result
        )

class ManyJobsResponse(BaseModel):
    jobs: list[JobResponse]

    @staticmethod
    def map_all(jobs: list[Job]):
        jobs_response: list[JobResponse] = [JobResponse.map_from_job(job) for job in jobs]
        return ManyJobsResponse(jobs=jobs_response)


class CreateJobRequest(BaseModel):
    user_id: int