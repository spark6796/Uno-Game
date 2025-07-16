from pydantic import BaseModel

class HostRequest(BaseModel):
    session_id: str

class PublicJoinRequest(BaseModel):
    session_id: str

class JoinRequest(BaseModel):
    session_id: str
    game_id: str