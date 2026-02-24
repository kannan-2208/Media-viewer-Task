from fastapi import FastAPI
from backend.database import engine, Base, SessionLocal
from backend import models
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
Base.metadata.create_all(bind=engine)

app.mount("/media", StaticFiles(directory="backend/media"), name="media")
@app.get("/api/videos")
def get_videos():
    db = SessionLocal()
    videos = db.query(models.Video).all()
    db.close()
    return videos
@app.get("/api/images")
def get_images():
    db = SessionLocal()
    images = db.query(models.Image).all()
    db.close()
    return images
@app.get("/add-data")
def add_data():
    db = SessionLocal()

    if db.query(models.Video).first():
        db.close()
        return {"message": "Data already added"}
    videos = [
        models.Video(title="Video 1", file_path="media/videos/11. frist estaate combator .mp4"),
        models.Video(title="Video 2", file_path="media/videos/29 winworth walkthough  .mp4"),
        models.Video(title="Video 3", file_path="media/videos/31.VBHC interior walkthrough .mp4"),
    ]

    images = [
        models.Image(title="Image 1", file_path="media/images/Aqua suites 2BHK - Living Cam.jpg"),
        models.Image(title="Image 2", file_path="media/images/C02_2 (1).png"),
        models.Image(title="Image 3", file_path="media/images/c11.00180 (1).png"),
        models.Image(title="Image 4", file_path="media/images/c12.00180 (1).png"),
        models.Image(title="Image 5", file_path="media/images/C14-1 (1) (1) (1).png"),
        models.Image(title="Image 6", file_path="media/images/C14-1 (1) (1).png"),
    ]
    db.add_all(videos + images)
    db.commit()
    db.close()
    return {"message": "Data added successfully"}