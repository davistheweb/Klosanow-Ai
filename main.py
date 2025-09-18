import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from utils.chat import Klosanow_Chat

load_dotenv()

app =  FastAPI(title="Klosanow Ai")

app.add_middleware(
    CORSMiddleware,
    allow_origins = [f'{os.getenv('CORS_ALLOWED_ORIGINS')}'],
    allow_credentials= False,
    allow_methods = ['POST'],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return "Welcome to klosanow AI"


class chatKlosanowAiRequest(BaseModel):
    message: str 

@app.post('/chat')
async def chatWithKlosanowAi(req: chatKlosanowAiRequest):
    text = req.message
    if not text:
        return JSONResponse(content={"error": 'No text provided' }, status_code=400)
    try:
        print('Message: ', req.message)
        genai_response = Klosanow_Chat(text)
        return JSONResponse(content={'message': genai_response}, status_code=200)
    except Exception as e:
        print(str(e))
        return JSONResponse(content={'message': str(e)}, status_code=500)