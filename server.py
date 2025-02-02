from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
from typing import List
import cv2
import numpy as np
import base64
import io

app = FastAPI()

# Fake News Detection (For example, use some external API or model)
fake_news_model = "model_real_fake.h5"  # Placeholder, integrate your model here

class NewsRequest(BaseModel):
    news: str

class FakeNewsResponse(BaseModel):
    verification_result: str
    news_title: str
    news_content: str

class DeepfakeResponse(BaseModel):
    result: str
    flagged_frames: List[dict]

@app.post("/verify-news", response_model=FakeNewsResponse)
async def verify_news(news: NewsRequest):
    # Fake news detection logic (can use external API or ML model here)
    # Placeholder logic for demonstration
    verification_result = "True" if "fake" in news.news.lower() else "False"
    return FakeNewsResponse(
        verification_result=verification_result,
        news_title="Sample News Title",
        news_content="This is a sample content for the fake news headline."
    )

@app.post("/upload", response_model=DeepfakeResponse)
async def upload_video(file: UploadFile = File(...)):
    try:
        # Read the video file
        video_data = await file.read()
        video_array = np.asarray(bytearray(video_data), dtype=np.uint8)
        video = cv2.imdecode(video_array, cv2.IMREAD_COLOR)

        # OpenCV to capture video frames
        cap = cv2.VideoCapture(io.BytesIO(video_data))
        
        if not cap.isOpened():
            raise HTTPException(status_code=400, detail="Could not open video file")

        flagged_frames = []  # Placeholder for flagged frames

        frame_count = 0
        while True:
            ret, frame = cap.read()  # Read each frame
            if not ret:
                break

            frame_count += 1
            # Mock flagging of deepfake frames (for demo purposes, flag first 3 frames)
            if frame_count <= 3:  # Limiting to first 3 frames for demo
                _, buffer = cv2.imencode('.jpg', frame)
                frame_base64 = base64.b64encode(buffer).decode('utf-8')

                flagged_frames.append({
                    "frame_number": frame_count,
                    "image_base64": frame_base64
                })

        cap.release()  # Release the video capture object

        return DeepfakeResponse(result="Not Fake", flagged_frames=flagged_frames)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing video: {str(e)}")
