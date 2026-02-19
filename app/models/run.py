from pydantic import BaseModel
from datetime import datetime, timezone


class RunBaseResponse(BaseModel):
    world_id: str
    seed: int | None=None
    run_name: str | None=None

class RunSummary(RunBaseResponse):
    run_id: str
    current_day: int
    status: str | None=None
    created_at: datetime = datetime.now(timezone.utc)