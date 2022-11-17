from __future__ import annotations

import uvicorn # For debugging

from fastapi import FastAPI, WebSocket
from fastapi import __version__ as fastapi_version
from fastapi.middleware.cors import CORSMiddleware

from typing import Any, Dict
from pydantic import BaseModel

import json


import logging
_log = logging.getLogger(__name__)
handler = logging.StreamHandler()
formatter = logging.Formatter('{levelname:<9s} {message}', style='{')
handler.setFormatter(formatter)
_log.addHandler(handler)
_log.setLevel(logging.DEBUG)

__author__ = 'Klaus Eckelt'

app = FastAPI()
_log.debug(f"fastapi version: {fastapi_version}")

origins = [
  "http://localhost",
  "http://127.0.0.1",
  "http://localhost:8080",
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

"""
Accepts JSONs that look like:
{
	"filename": "zoink.pdf", 
	"data": {}
}
With anything in data.

converted with: https://jsontopydantic.com/
"""
class SaveData(BaseModel):
  filename: str
  data: Dict[str, Any]


@app.get("/")
def root():
  return {"message": "Hello World"}


@app.post("/")
async def save_json(save_data: SaveData):
  _log.debug(f'Storing data in file: {save_data.filename}')

  with open(f"data/{save_data.filename}", "w") as write_file:
    json.dump(save_data.data, write_file, indent=2)
  return


# When running it locally
if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=9666)
