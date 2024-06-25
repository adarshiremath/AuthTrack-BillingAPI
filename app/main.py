from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

from app.api.endpoints import auth, users, billing

app = FastAPI()

# Properly set up Instrumentator before the application starts
instrumentator = Instrumentator()
instrumentator.instrument(app).expose(app)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(billing.router, prefix="/billing", tags=["billing"])

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
