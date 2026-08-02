from pydantic import BaseModel


class RecommendationRequest(BaseModel):
    city: str
    garden_size: str
    sunlight: str
    maintenance: str
