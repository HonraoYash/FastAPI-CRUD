from types import new_class
from fastapi import FastAPI, HTTPException, Request, Response
from collections import defaultdict
from datetime import datetime
from random import randint
from typing import Any

app = FastAPI(root_path="/api/v1")

database = defaultdict(list)
database[1] = {"campaign_id": 1, "name": "Campaign 1", "due_date": datetime.now(), "created_at": datetime.now()}
database[2] = {"campaign_id": 2, "name": "Campaign 2", "due_date": datetime.now(), "created_at": datetime.now()}
database[3] = {"campaign_id": 3, "name": "Campaign 3", "due_date": datetime.now(), "created_at": datetime.now()}

"""
Campaigns:
- campaign_id
- name
- due_date
- created_at
"""

@app.get("/")
async def root():
    return {"message": "Hello There!"}

@app.get("/campaigns")
async def read_campaigns():
    return {'campaigns': database}

@app.get("/campaigns/{id}")
async def read_campaign(id: int):
    if id in database:
       return {'campaign': database[id]}
    raise HTTPException(status_code=404)

@app.post("/campaigns", status_code=201)
async def create_campaign(body: dict[str, Any]):
 
      campaign_id = randint(100,1000)
      new = {
        "campaign_id": campaign_id,
        "name": body.get("name"),
        "due_date": body.get("due_date"),
        "created_at": datetime.now()
      }

      database[campaign_id] = new
      return {"campaign": database[campaign_id]}

@app.put("/campaigns/{id}")
async def update_campaign(id: int, body: dict[str, Any]):
      new_name = body.get("name")
      new_due_date = body.get("due_date")
      database[id]["name"] = new_name
      database[id]["due_date"] = new_due_date
      return {"update campaign": database[id]}

@app.delete("/campaigns/{id}")
async def delete_campaign(id: int):
    if id in database:
       del database[id]
       return Response(status_code=204)
    raise HTTPException(status_code=404)

"""
This was from Caleb Curry's Youtube Playlist, and I did it to learn FastAPI and CRUD operations.
For simplicity, I used a dictonary instead of a database, to focus more on writing API endpoints rather that other complexities.
This is just half the video, and the rest half is using SQL database instead of a dictionary, so do watch it later.
Current focus is only on learning how to write APIs.
"""