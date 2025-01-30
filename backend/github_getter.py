from github import Github
from github import Auth
from pydantic import BaseModel
from rich import print
from typing import Self
import os
import sys
import getpass

from backend.data_model.models import GitElement, GitFile


if "GITHUB_API_TOKEN" not in os.environ:
    os.environ["GITHUB_API_TOKEN"] = getpass.getpass(prompt="Enter your Github API key: ")

auth = Auth.Token(os.environ["GITHUB_API_TOKEN"])
g = Github(auth=auth)

def get_branches(account:str, repo_name: str):
    repo = g.get_repo(f'{account}/{repo_name}')
    branches = repo.get_branches()
    return [branch.name for branch in branches]

def get_repo(account:str, repo_name: str, branch: str = 'master'):
    try:
        repo = g.get_repo(f'{account}/{repo_name}')
    except Exception as e:
        print(e)
        return GitElement(name='Error', is_dir=False, size=0, full_path='Error', error=str(e))
    contents = repo.get_contents('')
    tree = repo.get_git_tree(branch, recursive=True)
    root = GitElement(full_path='/', name='/', is_dir=True, size=0)
    for file in tree.tree:
        element = GitElement(is_dir=file.type == 'tree', size=file.size if file.size else 100, full_path=file.path)
        root.add_child(element)
    return root



def get_file(account:str, repo_name: str, branch: str, path: str):
    try:
        repo = g.get_repo(f'{account}/{repo_name}')
    except Exception as e:
        print(e)
        return GitElement(name='Error', is_dir=False, size=0, full_path='Error', error=str(e))
    contents = repo.get_contents(path)
    langauge = 'unknown'
    if contents.name.startswith('.') or '.' not in contents.name:
        langauge = 'txt'
    else:
        split_name = contents.name.split('.')
        if len(split_name) > 1:
            langauge = split_name[-1]
    decoded = 'Cannot Decode File'
    try:
        decoded = contents.decoded_content.decode()
    except:
        pass
    
    return GitFile(name=contents.name, language=langauge ,path=contents.path, size=contents.size, html_url=contents.html_url, content=decoded)
    

if __name__ == "__main__":
    print(get_file('robger98', 'portfolio_site', 'main', 'backend/llm_manager.py'))
    
