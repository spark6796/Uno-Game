from ..state import sessions

class SessionManager:
    def __init__(self, session_id: str) -> None:
        self.session_id = session_id

    def is_legit(self) -> bool:
        return self.session_id in sessions

    def remove(self) -> None:
        if self.is_legit():
            del sessions[self.session_id]

    def join_game(self) -> None:
        if self.is_legit():
            sessions[self.session_id]['in_game'] = True

    def add(self, **kwargs) -> None:
        sessions[self.session_id] = {}
        for key, value in kwargs.items():
            sessions[self.session_id][key] = value

    def get_name(self) -> str:
        return sessions[self.session_id].get('name', 'Unknown')
    
    def get_pfp(self) -> str:
        return sessions[self.session_id].get('pfp', 'pfp/0.jpeg')

    def in_game(self) -> bool:
        return sessions[self.session_id].get('in_game', False)