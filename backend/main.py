from fastapi import FastAPI

app = FastAPI()
setup_cors = (app)

@app.get("/")
def read_root():
    return "this is a string"
