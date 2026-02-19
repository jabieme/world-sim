from pydantic import BaseModel, Field
from enum import Enum

class EventType(Enum):
    SUPPLY_SHOCK="SUPPLY_SHOCK"
    DEMAND_SHOCK="DEMAND_SHOCK"


class EventBaseResponse(BaseModel):
    event_type: EventType
    region_id: str
    resource: str
    severity: float = Field(..., ge=0, le=1)  # 0-1
    start_day: int
    duration_days: int

class EventResponse(EventBaseResponse):
    event_id: str
    end_day: int

# class ActiveEvent(BaseModel):
#     event_type: EventType
#     region_id: str
#     resource: str
#     if event_type.DEMAND_SHOCK:
#         supply_multiplier:float
#     else:
#         demand_multiplier: float
