from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services import input_recognizer, ai_simulator
import logging

router = APIRouter()
logger = logging.getLogger("uvicorn")

class InputRequest(BaseModel):
    content: str
    input_type: str

class ResponseRequest(BaseModel):
    question: str

@router.post("/recognize_input")
async def recognize_input(request: InputRequest):
    try:
        logger.info(f"Received input: {request}")
        result = input_recognizer.recognize(request.content, request.input_type)
        if result is None:
            raise HTTPException(status_code=400, detail="Invalid input type")
        return {"recognized_input": result}
    except Exception as e:
        logger.error(f"Error in recognize_input: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/generate_response")
async def generate_response(request: ResponseRequest):
    try:
        logger.info(f"Received question: {request}")
        response = ai_simulator.generate_response(request.question)
        return {"ai_response": response}
    except Exception as e:
        logger.error(f"Error in generate_response: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))