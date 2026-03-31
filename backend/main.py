from pathlib import Path
import sys

from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

def setup_cors(app):
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.append(str(CURRENT_DIR))

from cors import setup_cors

app = FastAPI()
setup_cors(app)

@app.get("/")
def read_root():
    return {"message": "this is a string"}
