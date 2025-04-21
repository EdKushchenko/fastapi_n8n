from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"greeting": "mazamba!", "message": "zazanva!", "bizimba": "zazoomba"}


@app.get("/reviews")
async def get_reviews():
    return {"review_id": "1", "username": "vasya", "rating": "5", "text": "very boring"}
