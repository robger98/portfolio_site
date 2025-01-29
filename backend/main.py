import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from typing import List
# from rich import print
import logging

from backend.data_model.models import Message, GitElement, GitFile
from . import github_getter
from . import llm_manager

app = FastAPI()

LOG = logging.getLogger(__name__)
LOG.setLevel(logging.INFO)


origins = [
    "http://localhost:3000",
    "http://localhost:8000",
    "http://localhost:8080",
    "http://localhost:5173",
    "https://portfolio-site-frontend-1042877629487.us-central1.run.app",
    "https://robertgeraghty.com",
    "https://www.robertgeraghty.com"
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

@app.get('/repo/{account}/{repo_name}/branches', response_model=List[str])
def get_branches(account:str, repo_name: str):
    print('ACCOUNT', account)  
    print('REPO', repo_name)
    try:    
        branches = github_getter.get_branches(account, repo_name)
    except Exception as e:
        LOG.error(e)
        LOG.error(repo_name)
        branches = [f'Error {str(e)}']
    return branches

@app.get('/repo/{account}/{repo_name}/{branch}', response_model=GitElement)
def get_repo(account: str, repo_name: str, branch: str):
    try:
        out = github_getter.get_repo(account, repo_name, branch=branch)
    except Exception as e:
        LOG.error(e)
        LOG.error(repo_name)
        out = GitElement(name='Error', is_dir=False, size=0, full_path='Error', error=str(e))
    return out

@app.get('/repo/{account}/{repo_name}/{branch}/{path:path}', response_model=GitFile)
def get_file(account: str, repo_name: str, branch: str, path: str):
    try:
        out = github_getter.get_file(account, repo_name, branch, path)
    except Exception as e:
        LOG.error(e)
        LOG.error(repo_name)
        out = GitFile(name='Error', language='Error', path='Error', size=0, html_url='Error', content=f'Error: {str(e)}')
    return out

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)