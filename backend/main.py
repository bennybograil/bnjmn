from pathlib import Path
import sys

from fastapi import FastAPI
from cors import setup_cors


from fastapi.middleware.cors import CORSMiddleware

def setup_cors(app):
   app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app = FastAPI()
setup_cors(app)

@app.get("/")
def read_root():
    return {"message": "this is a string"}
