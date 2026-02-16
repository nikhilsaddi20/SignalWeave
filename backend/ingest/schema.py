from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class AuthEvent(BaseModel):
    timestamp: datetime
    event_type: str
    user: Optional[str] = None
    ip: Optional[str] = None
    host: Optional[str] = None