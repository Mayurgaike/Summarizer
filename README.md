# Summarizer

![Your App Logo](assets/logo.png)

Summarizer is a versatile web application designed for creating summaries from various formats, including PDF documents, research papers, and YouTube videos using streamlit. Whether the content is in Marathi, Hindi, or English, Summarizer intelligently processes the information to generate concise and meaningful summaries.

## Getting Started

To get started with Summarizer, simply visit the website, upload your content, and let the application handle the rest. Follow the intuitive steps to generate summaries tailored to your preferences.

Summarizer is the go-to tool for anyone looking to extract the essence of information efficiently and accurately.

### Prerequisites

- Python 3.6 minimum
- txtai
- streamlit
- PyPDF2
- YouTube API Key (Optional)

### Installation

1. Clone the repository:

   bash
   git clone https://github.com/Mayurgaike/Summarizer.git
   cd Summarizer

   

2. Set up a virtual environment:

   bash
   python -m venv venv
   source venv/bin/activate
   On Windows, use `venv\Scripts\activate`
   

3. Install dependencies:

   bash
   pip install -r requirements.txt
   

### Usage

bash
streamlit run app.py


Open your web browser and visit http://localhost:8501 to access the Summarizer interface.

Upload your desired content, whether it's a PDF document, research paper, or YouTube video, and let Summarizer intelligently generate concise summaries for you.
