from fastapi import FastAPI

app = FastAPI(title="World Simulation API")

@app.get("/health")
def health():
    return {"status": "ok"}

