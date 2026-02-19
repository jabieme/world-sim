# USED AS THE CONTROLLER

from fastapi import APIRouter

from app.models.world import RegionConfig, WorldOutResponse, WorldCreateResponse

from app.services.world_service import create_world
world_router = APIRouter()

@world_router.post("/worlds")
def create_world(created_world: WorldCreateResponse) :
    world = create_world(created_world)
    return
@world_router.get("/health")
def health():
    return {"status": "ok"}
