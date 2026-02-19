from pydantic import BaseModel
from datetime import datetime, timezone
from world import RegionConfig

class RegionState(RegionConfig):
    food_shortage: bool
    energy_shortage: bool

class WorldStateSnapshot(BaseModel):
    run_id: str
    day: int
    regions: list[RegionState]