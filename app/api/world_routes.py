# USED AS THE CONTROLLER

from fastapi import APIRouter

from app.models.world import RegionConfig, WorldOutResponse, WorldCreateResponse

from app.services.world_service import *
world_router = APIRouter()

@world_router.get("/worlds")
def get_new_world()-> WorldOutResponse:
    return create_new_world()
@world_router.get("/health")
def health():
    return {"status": "ok"}
