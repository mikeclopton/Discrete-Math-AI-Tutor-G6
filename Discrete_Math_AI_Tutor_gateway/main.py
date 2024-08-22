from fastapi import FastAPI
from routes import router
import uvicorn
import logging

app = FastAPI(title="AI Discrete Math Tutor API Gateway Prototype")

app.include_router(router)

@app.on_event("startup")
async def startup_event():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("uvicorn")
    logger.info("Starting up server...")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
