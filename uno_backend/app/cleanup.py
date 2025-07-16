import asyncio
from .config import session_expiry_time, garbage_clean_every
from .state import sessions
from datetime import datetime, timedelta

SESSION_EXPIRATION_TIME = timedelta(hours=session_expiry_time)

async def clean_sessions():
    while True:
        time_now = datetime.now()
        expired_sessions = [session for session in sessions if time_now - sessions[session]['created_at'] > SESSION_EXPIRATION_TIME and not sessions[session]['in_game']]
        for session_id in expired_sessions:
            del sessions[session_id]
        await asyncio.sleep(garbage_clean_every*60*60)
