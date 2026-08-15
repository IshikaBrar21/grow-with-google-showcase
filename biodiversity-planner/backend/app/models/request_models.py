from pydantic import BaseModel


class RecommendationRequest(BaseModel):
    region: str
    soil_type: str
    sunlight: str
    moisture: str
