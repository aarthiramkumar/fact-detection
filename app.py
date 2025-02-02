import streamlit as st
import requests
import io
from PIL import Image
import base64

# FastAPI backend URL (update if hosted elsewhere)
BACKEND_URL = "http://127.0.0.1:8000"  # Placeholder, change as needed

st.title("📰 Fake News & Deepfake Video Detection")

st.markdown("### Detect Fake News or Deepfake Videos with AI")

# Sidebar for navigation
option = st.sidebar.radio("Choose an option:", ["Deepfake Video Detection", "Fake News Detection"])

# 🟢 Deepfake Video Detection
if option == "Deepfake Video Detection":
    st.subheader("🎥 Upload a Video to Detect Deepfake")
    
    uploaded_video = st.file_uploader("Choose a video file...", type=["mp4", "avi", "mov", "mkv"])

    if uploaded_video:
        # Display the uploaded video below the uploader
        st.video(uploaded_video)

        # Convert uploaded video to a file-like object
        video_bytes = uploaded_video.read()

        if st.button("Analyze Video"):
            st.info("🔍 Analyzing... Please wait!")
            
            # Display running status with a spinner
            with st.spinner("Processing video..."):
                try:
                    # Send video to FastAPI backend as in-memory data
                    files = {"file": (uploaded_video.name, io.BytesIO(video_bytes), "video/mp4")}
                    response = requests.post(f"{BACKEND_URL}/upload", files=files)

                    if response.status_code == 200:
                        result = response.json().get("result", "Error")
                        flagged_frames = response.json().get("flagged_frames", [])

                        st.success(f"🧐 Analysis Result: **{result}**")

                        # Display flagged frames if any
                        if flagged_frames:
                            st.subheader("🚨 Flagged Frames")
                            for i, flagged_frame in enumerate(flagged_frames):
                                # Decode base64 image data and display it
                                image_data = flagged_frame["image_base64"]
                                image_bytes = base64.b64decode(image_data)
                                image = Image.open(io.BytesIO(image_bytes))
                                st.image(image, caption=f"Flagged Frame {i + 1}")
                    else:
                        st.error("🚨 Error processing the video.")
                except Exception as e:
                    st.error(f"🚨 An error occurred: {str(e)}")
                
# 🟢 Fake News Detection
elif option == "Fake News Detection":
    st.subheader("📰 Enter a News Headline to Verify")

    news_text = st.text_area("Type or paste the news headline here...")

    if st.button("Verify News"):
        if not news_text:
            st.warning("⚠ Please enter a news headline.")
        else:
            st.info("🔍 Checking for fake news... Please wait!")

            # Send request to FastAPI backend for fake news detection
            response = requests.post(f"{BACKEND_URL}/verify-news", json={"news": news_text})

            if response.status_code == 200:
                data = response.json()
                st.success(f"🧐 News Result: **{data['verification_result']}**")
                st.write(f"🔎 **Matched News Title:** {data['news_title']}")
                st.write(f"📰 **News Snippet:** {data['news_content']}")
            else:
                st.error("🚨 Error processing the news verification.")
