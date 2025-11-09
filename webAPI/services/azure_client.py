import os

from azure.ai.vision.imageanalysis.aio import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential

from config import config

class AzureClient:
    def __init__(self):
        self.client = ImageAnalysisClient(endpoint=config.AZURE_URL, credential=AzureKeyCredential(config.PRIMARY_KEY))

    async def get_image_caption(self, image) -> str | None:
        result = await self.client.analyze(image_data=image, visual_features=[VisualFeatures.CAPTION])
        
        return result.caption.text if result.caption is not None else None