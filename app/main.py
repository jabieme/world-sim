from fastapi import FastAPI
from .services.world_service import create_world
from .api.world_routes import world_router
app = FastAPI(title="World Simulation API")

app.include_router(world_router)




