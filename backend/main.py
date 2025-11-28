from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def initial():
    return {"message":"Welcome to the server"}