from typing import List
from datetime import datetime, timezone

from pydantic import BaseModel, Field


class TradeLinkConfig(BaseModel):
    from_region_id: str
    to_region_id: str
    capacity: float #flow of resources per day
    efficiency: float = Field(..., ge=0, le=1) #0-1
    resources: list[str]

class RegionConfig(BaseModel):
    region_id: str
    name: str
    population: int
    employment_rate: float = Field(0.46, ge=0, le=1)  # 0-1
    food_supply: float
    energy_supply: float
    price_index: float = 1.0  # start at 1.0
    stability: float = Field(0.85, ge=0, le=1) # 0-1 start at 0.85

class WorldCreateResponse(BaseModel):
    name: str
    regions: list[RegionConfig]
    trade_links: list[TradeLinkConfig]


class WorldOutResponse(WorldCreateResponse):
    world_id: str
    created_at: datetime = datetime.now(timezone.utc)

def create_world(region: RegionConfig):
    return region