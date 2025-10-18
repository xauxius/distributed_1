import os

from azure.ai.vision.imageanalysis.aio import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

PRIMARY_KEY = os.getenv("PRIMARY_KEY")
URL = os.getenv("URL")

class AzureClient:
    def __init__(self):
        self.client = ImageAnalysisClient(endpoint=URL, credential=AzureKeyCredential(PRIMARY_KEY))

    async def get_image_caption(self, image):
        result = await self.client.analyze(image_data=image, visual_features=[VisualFeatures.CAPTION])
        
        return result.caption.text