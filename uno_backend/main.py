from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.game import router as game_router
from app.routers.session import router as session_router
from app.cleanup import clean_sessions
import os
from dotenv import load_dotenv
import asyncio 

load_dotenv()

origin = os.getenv('ORIGIN')
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(game_router)
app.include_router(session_router)

@app.on_event('startup')
async def app_startup():
    asyncio.create_task(clean_sessions())

@app.get('/')
async def root(): 
    return {"message": "Uno Game API!"}
