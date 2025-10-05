import os
import queue

from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

PRIMARY_KEY = os.getenv("PRIMARY_KEY")
URL = os.getenv("URL")

class AzureService:
    def __init__(self):
        self.client = ImageAnalysisClient(endpoint=URL, credential=AzureKeyCredential(PRIMARY_KEY))
        self.q = queue.Queue()
        self.t_start 

    def get_image_caption(self, image):
        result = self.client.analyze(image_data=image, visual_features=[VisualFeatures.CAPTION])
        return result.caption.text