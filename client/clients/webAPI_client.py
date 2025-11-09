from io import BufferedReader
import requests

class WebAPIClient:
    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    def get_jobs_by_user(self, username: str):
        url = f"{self.base_url}/image-analysis/all/{username}"

    def get_single_job(self, job_id: int):
        url = f"{self.base_url}/image-analysis/single/{job_id}"

    def create_analysis_job(self, username: str, image: BufferedReader):
        url = f"{self.base_url}/image-analysis/"
        files = {"image": image}

        r = requests.post(url, data={"username": username}, files=files)

        

    