from fastapi import FastAPI

import uvicorn 

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/goodmorning/{name}")
def say_good_morning(name: str):
    return {"message": f"very Good morning, {Payal pagar}!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
