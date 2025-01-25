import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from rich import print

from backend.data_model.models import Message
from . import llm_manager

app = FastAPI()

origins = [
    "http://localhost:3000",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, 
    allow_credentials=True, 
    allow_methods=["*"], 
    allow_headers=["*"],
)

memory_db = {"Messages": []}

@app.get('/messages', response_model=List[Message])
def get_messages():
    return []

@app.post('/send', response_model=Message)
def send(messages: List[Message]):
    print(messages[-1])
    memory_db["Messages"] = messages
    response = llm_manager.send(messages)
    memory_db["Messages"].append(response)
    return response
    # return messages[-1]

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)