from pathlib import Path
import sys

from fastapi import FastAPI

CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.append(str(CURRENT_DIR))

from cors import setup_cors

app = FastAPI()
setup_cors(app)

@app.get("/")
def read_root():
    return {"message": "this is a string"}
