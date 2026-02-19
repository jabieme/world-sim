from enum import Enum
from typing import Optional

from pydantic import BaseModel

class MetricKey(Enum, Optional):
    STABILITY = "STABILITY"
    PRICE_INDEX = "PRICE_INDEX"
    FOOD_SUPPLY = "FOOD_SUPPLY"
    ENERGY_SUPPLY = "ENERGY_SUPPLY"

class RegionMetricPoint(BaseModel):
    day: int
    region_id: str
    stability: float
    price_index: float
    food_supply: float
    energy_supply: float

class MetricResponse(BaseModel):
    run_id: str
    points: list[RegionMetricPoint]