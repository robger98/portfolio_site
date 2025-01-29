from pydantic import BaseModel
from uuid import UUID
from typing import Self
class Message(BaseModel):
    # user_id: UUID
    role: str
    content: str

class GitElement(BaseModel):
    name: str = ''
    is_dir: bool
    size: int = 0
    full_path: str
    children: list[Self] = []
    parent_name: str | None = None
    error: str | None = None

    def __init__(self, **data):
        super().__init__(**data)
        self.name = self.full_path.split('/')[-1]

    def add_child(self, child: Self):
        split_path = child.full_path.split('/')
        self._add_child(child, split_path)

    def _add_child(self, child: Self, split_path):
        self.size += child.size
        if len(split_path) == 1:
            child.parent_name = self.name
            self.children.append(child)
            return
        for c in self.children:
            if c.name == split_path[0]:
                c._add_child(child, split_path[1:])
                return

class GitFile(BaseModel):
    name: str
    language: str
    path: str
    size: int
    html_url: str
    content: str