from fastapi import FastAPI

app = FastAPI()

# Homepage endpoint
@app.get("/")
def homepage():
    return {"message": "Welcome to the Game Recommendation API"}