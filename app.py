import streamlit as st
from txtai.pipeline import Summary
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi
from PyPDF2 import PdfReader
import os

st.set_page_config(layout="wide")


@st.cache_resource
def text_summary(text, maxlength=None):
    # create summary instance
    summary = Summary()
    text = (text)
    result = summary(text)
    return result


def extract_text_from_pdf(file_path):
    # Open the PDF file using PyPDF2
    with open(file_path, "rb") as f:
        pdf_reader = PdfReader(f)
        text = ""
        for page_number in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_number].extract_text()
    return text


def download_youtube_video(video_url):
    st.info("Downloading video...")
    yt = YouTube(video_url)
    video_stream = yt.streams.filter(file_extension="mp4").first()
    video_path = os.path.join("videos", f"{yt.title}.mp4")
    video_stream.download(output_path="videos", filename=yt.title)
    st.success("Video downloaded successfully!")
    return video_path


def extract_transcript(video_url, language="en"):
    st.info("Fetching transcript...")

    try:
        video_id = None
        if "v=" in video_url:
            video_id = video_url.split("v=")[1].split("&")[0]
        elif "youtu.be" in video_url:
            video_id = video_url.split("/")[-1]

        if video_id:
            # Fetch transcript using YouTubeTranscriptApi
            transcript = YouTubeTranscriptApi.get_transcript(
                video_id, languages=[language])
            text = " ".join([entry['text'] for entry in transcript])
            return text
        else:
            st.warning(
                "Failed to extract video ID. Please check the video URL.")
            return None
    except Exception as e:
        st.error(f"Error fetching transcript: {e}")
        return None


# Sidebar
choice = st.sidebar.selectbox(
    "Select your choice", ["Summarize Text", "Summarize Document", "Summarize YouTube Video"])

if choice == "Summarize Text":
    st.subheader("Summarize Text")
    input_text = st.text_area("Enter your text here")
    if input_text is not None:
        if st.button("Summarize Text"):
            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown("**Your Input Text**")
                st.info(input_text)
            with col2:
                st.markdown("**Summary Result**")
                result = text_summary(input_text)
                st.success(result)

elif choice == "Summarize Document":
    st.subheader("Summarize Document")
    input_file = st.file_uploader("Upload your document here", type=['pdf'])
    if input_file is not None:
        if st.button("Summarize Document"):
            with open("doc_file.pdf", "wb") as f:
                f.write(input_file.getbuffer())
            col1, col2 = st.columns([1, 1])
            with col1:
                st.info("File uploaded successfully")
                extracted_text = extract_text_from_pdf("doc_file.pdf")
                st.markdown("**Extracted Text is Below:**")
                st.info(extracted_text)
            with col2:
                st.markdown("**Summary Result**")
                text = extract_text_from_pdf("doc_file.pdf")
                doc_summary = text_summary(text)
                st.success(doc_summary)

elif choice == "Summarize YouTube Video":
    st.subheader("Summarize YouTube Video")
    video_url = st.text_input("Enter YouTube Video URL")
    language = st.selectbox("Select language", ["en", "mr", "hi"])

    if video_url:
        if st.button("Summarize YouTube Video"):
            st.info("Downloading video...")
            video_path = download_youtube_video(video_url)
            st.info("Extracting transcript...")
            transcript = extract_transcript(video_url, language)

            if transcript:
                st.info("Summarizing video...")
                summary = Summary()
                video_summary = summary(transcript)

                st.markdown("**Summary Result**")
                st.success(video_summary)
            else:
                st.warning(
                    "Failed to fetch transcript. Please check the video URL.")
