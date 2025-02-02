# Verify AI - Misinformation Detection & Fact Checking 📢

### 📌 Theme: Misinformation Detection & Fact Checking on Social Media
False information spreads rapidly on social media, affecting public trust and decision-making. Our project, **Verify AI**, uses advanced AI models to analyze **images, texts, and videos** for fake or manipulated content in real-time.

![image](https://github.com/user-attachments/assets/ec16e6d5-478b-4fc4-baea-3960634207ab)
## 🚀 Features
✅ **Real-time detection** of misinformation in **text, images, and videos**  
✅ **Cross-referencing with trusted databases** and fact-checking APIs  
✅ **Visual representation** of flagged content with credibility scores  
✅ **Prebunking system** to warn users about misinformation trends  
✅ **Trust-building reports** to validate sources  
![image](https://github.com/user-attachments/assets/0a71532f-babf-4cea-a90c-1c260c3e5212)

### 📊 How It Works

Our **Fake News Detector** is designed to classify news articles as **fake or real** using a **Passive Aggressive Classifier**. The system follows a structured pipeline:

1️⃣ **User Input**: The system receives a news article as input.  
2️⃣ **Text Pre-Processing**: The text undergoes cleaning, including stopword removal, tokenization, and stemming.  
3️⃣ **Feature Extraction**: The pre-processed text is converted into numerical features using **TF-IDF (Term Frequency-Inverse Document Frequency)**.  
4️⃣ **Model Training**: A **Passive Aggressive Classifier** is used to learn patterns from labeled news data.  
5️⃣ **Prediction**: The trained model predicts whether the input news article is **fake** or **real**.  
6️⃣ **Output**: The system provides a final classification result to the user.
### 🖼 Flowchart Representation

![image](https://github.com/user-attachments/assets/77abc39b-6858-4295-ba54-d1408bfa702b)

This structured pipeline ensures efficient and accurate fake news detection. 🚀

## 🛠 Tech Stack  

Our **Fake News Detector** utilizes the following technologies:  

- **Frontend**: React  
- **Backend**: Node.js, Flask  
- **Hosting**: Render  
- **APIs**: OpenCV, Google Fact Check API, NLP  
- **Database**: MySQL  
![image](https://github.com/user-attachments/assets/4f4aae50-cbec-4c47-9d28-e25c0933ab2f)
### 1️⃣ **Video Analysis - Extracting Frames for Deepfake Detection**
To analyze fake videos, we split them into individual frames for image-based deepfake detection.

**🔹 Steps to Extract Frames from a Video:**
```python
import cv2
import os

# Load video
video_path = "video.mp4"
output_folder = "frames"
os.makedirs(output_folder, exist_ok=True)

cap = cv2.VideoCapture(video_path)
frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
    cv2.imwrite(frame_filename, frame)
    frame_count += 1

cap.release()
print(f"Extracted {frame_count} frames and saved to '{output_folder}'")


🎨 USER INTERFACE
Our Fake News Detector provides two detection options for users:

🔹 1. Video Fake Detection
Users can upload a video for analysis.
The system extracts frames from the video and analyzes them using AI-based techniques.
It detects fake elements and provides a detailed explanation of why the video is classified as real or fake.
🔹 2. Text News Detection
Users can enter or upload a news article for verification.
The system processes the text, checks it against fact-checking databases, and applies NLP techniques.
It returns a real or fake classification along with a justification for the decision.






















