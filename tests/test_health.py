from fastapi.testclient import TestClient
from app.main import app
from app.services.world_service import create_regions
from app.models.world import RegionConfig
client = TestClient(app)

region = RegionConfig(
        region_id="RG-CENTRAL-1",
        name = "Test_Name",
        population = 100000,
        employment_rate = 1.0,
        food_supply = 1.0,
        energy_supply = 1.0,
        price_index = 1.0,
        stability = 1.0,
    )

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status":"ok"}

def test_create_region():
    test = create_regions()
    assert region == test