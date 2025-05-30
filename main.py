from typing import Optional
from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

# Background job function
async def background_job():
    while True:
        print("Running background task...")
        await asyncio.sleep(10)  # simulate periodic job

# Run background job on startup
@app.on_event("startup")
async def startup_event():
    print("App is starting up...")
    asyncio.create_task(background_job())
