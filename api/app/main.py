from fastapi import FastAPI
from functools import lru_cache
import uvicorn

from src import db

@lru_cache
def db_init():
    db.global_init()

app = FastAPI()

@app.on_event('startup')
def startup():
    db_init()

@app.get('/foo', response_model=str)
def foo(q: str):
    output = db.Output()
    output.text = q + "bar"
    output.save()
    return output.text

if __name__ == "__main__":
    try:
        uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, root_path="/")
    except KeyboardInterrupt:
        raise
