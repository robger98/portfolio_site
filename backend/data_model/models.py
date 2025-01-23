from pydantic import BaseModel
from uuid import UUID

class Message(BaseModel):
    # user_id: UUID
    role: str
    content: str