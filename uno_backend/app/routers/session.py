from fastapi import HTTPException, Request, APIRouter
import httpx
from ..services.session import SessionManager
from ..utils import generate_session_key
from ..config import valid_pfp
from datetime import datetime
import random
import os

turnstile_secret = os.getenv('TURNSTILE_SECRET')

router = APIRouter()

@router.post("/get_session")
async def get_session(request: Request):
    try:
        data = await request.json()
        
        if 'turnstile_response' not in data or 'name' not in data:
            raise HTTPException(status_code=400, detail="Missing required fields.")
        
        async with httpx.AsyncClient() as client:
            response = await client.post(
                'https://challenges.cloudflare.com/turnstile/v0/siteverify',
                data={
                    'secret': turnstile_secret,
                    'response': data['turnstile_response'],
                    'remoteip': request.client.host,
                },
            )
            verification = response.json()
            
            if verification.get('success'):
                name = data['name'][:12]  # Limit name length to 12 characters
                pfp = data['pfp']
                if pfp not in valid_pfp:
                    pfp = random.choice(valid_pfp)
                session_id = generate_session_key()
                my_data = {
                    'name': name,
                    'pfp': pfp,
                    'in_game': False,
                    'created_at': datetime.now()
                }
                SessionManager(session_id).add(**my_data)
                return {"success": "true", "sessionid": session_id}
            else:
                raise HTTPException(status_code=400, detail="Verification failed.")
   

    except:
        raise HTTPException(status_code=403, detail="Invalid Request")