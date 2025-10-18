from pydantic import BaseModel
from enum import Enum

class Status(Enum):
    WAITING = 1
    STARTED = 2
    FINISHED = 3

class JobResponse(BaseModel):
    status: Status
    job_id: int
    result: str | None 