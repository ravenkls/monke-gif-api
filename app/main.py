from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os
import random

app = FastAPI()

app.mount("/images", StaticFiles(directory="images"), name="static")


@app.get("/random")
def random_monke_gif():
    """Get a random monke GIF"""
    gif = random.choice(os.listdir("images"))
    url = "/images/" + gif
    return {"message": url, "status": "success"}