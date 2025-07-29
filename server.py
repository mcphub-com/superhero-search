import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/jakash1997/api/superhero-search'

mcp = FastMCP('superhero-search')

@mcp.tool()
def heroes() -> dict: 
    '''Return a list of 20 random heroes'''
    url = 'https://superhero-search.p.rapidapi.com/api/heroes'
    headers = {'x-rapidapi-host': 'superhero-search.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def villains() -> dict: 
    '''Return 20 random Villains'''
    url = 'https://superhero-search.p.rapidapi.com/api/villains'
    headers = {'x-rapidapi-host': 'superhero-search.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def search(hero: Annotated[Union[str, None], Field(description='The name or superhero name of the hero')] = None,
           regex: Annotated[Union[str, None], Field(description='')] = None) -> dict: 
    '''This endpoint searches through our superhero database'''
    url = 'https://superhero-search.p.rapidapi.com/api/'
    headers = {'x-rapidapi-host': 'superhero-search.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'hero': hero,
        'regex': regex,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
