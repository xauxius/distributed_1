import os
import queue
import time

from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

from constants import WAITING

PRIMARY_KEY = os.getenv("PRIMARY_KEY")
URL = os.getenv("URL")
WAIT_TIME = 10

class AzureService:
    def __init__(self):
        self.client = ImageAnalysisClient(endpoint=URL, credential=AzureKeyCredential(PRIMARY_KEY))
        self.q = queue.Queue()
        self.t_start = time.time() - WAIT_TIME
        self.results = {}

        self.current_job_id = 0

    def get_image_caption(self, user_id, image):
        if time.time() - t_start < WAIT_TIME:
            job_id = self.current_job_id
            self.current_job_id += 1
            self.q.enqueue({"user_id": user_id, "image": image, "job_id": job_id})
            return WAITING

        if len(q) == 0:
            self.t_start = time.time()
            result = self.client.analyze(image_data=image, visual_features=[VisualFeatures.CAPTION])
            job_id = self.current_job_id
            self.current_job_id += 1

            return {"job_id": job_id, "caption": result.caption.text}

    def periodic_check(self):
        if time.time() - t_start > WAIT_TIME:
            if len(q) > 0:
                self.t_start = time.time()

                job = q.dequeue()
                user_id = job["user_id"]
                image = job["image"]
                job_id = job["job_id"]
                
                result = self.client.analyze(image_data=image, visual_features=[VisualFeatures.CAPTION])
                
                self.results[job_id] = result.caption.text


    def get_results(self, job_id):
        if job_id in results:
            return results[job_id]
        else:
            return WAITING