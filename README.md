# Qwen3.5-2B Local Chatbot – Assignment 1A

**Student ID**: [p2303298,p2303422]  
**Project Title**: Qwen3.5-2B Local Chatbot

---

## 1. Overview

This project implements a lightweight, local chatbot powered by the **Qwen3.5-2B** quantised language model (GGUF format). It uses the `llama-cpp-python` inference engine for efficient CPU‑based execution and **Streamlit** for a clean web interface. The application demonstrates:

- Loading a pre‑trained quantised LLM locally.
- Building an interactive web UI without external API calls.
- Unit testing for model accuracy, performance, memory usage, and auxiliary functions (pre‑/post‑processing).

All components run offline on a standard Windows laptop, making it a practical showcase of on‑device LLM deployment.

---

## 2. Prerequisites

- **Python** 3.10 or later (3.13 is compatible, but 3.10 is recommended for fewer dependency issues)  
- **Git** (for cloning the repository)  
- **At least 4 GB of free RAM** (the model uses ~1.2 GB after loading)  
- **~2 GB of free disk space** (for the model file and environment)

---

## 3. Installation Guide

Run the following commands **sequentially** in your terminal (PowerShell or CMD):

```bash
# 1. Clone the repository and enter the project folder
git clone https://github.com/krishnaik06/Complete-Langchain-Tutorials.git
cd "Complete-Langchain-Tutorials/Blog Generation"

# 2. Create and activate a Python virtual environment
python -m venv llm_env
# For Windows:
llm_env\Scripts\activate
# For macOS / Linux (uncomment the line below):
# source llm_env/bin/activate

# 3. Upgrade pip and install all dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install llama-cpp-python --extra-index-url https://abetlen.github.io/llama-cpp-python/whl/cpu
pip install pytest psutil

# 4. (Optional) Verify installation
pip list | findstr llama
Important: Download the quantised model file Qwen3.5-2B-Q4_K_M.gguf (approx. 1.2 GB) from Hugging Face and place it directly inside the Blog Generation folder before running the app.

4. Running the Application
Launch the Streamlit web interface with:

bash
streamlit run app.py
Once the server starts, open your browser and go to:

text
http://localhost:8501
You will see a simple chat page. Type your question and click Send to receive a reply from the Qwen model.

5. Testing
The project includes two test suites:

5.1 Model Tests (Accuracy, Performance, Memory)
Run these to verify the model’s behaviour:

bash
pytest test_model.py -v -s
Accuracy: Asks for the capital of China and checks that the response contains “Beijing” or “北京”.

Performance: Measures the response time for a simple prompt (must be under 30 seconds).

Memory: Reports the current memory usage of the Python process.

5.2 Utility Tests (Pre‑/Post‑processing)
These test the helper functions defined in utils.py:

bash
pytest test_utils.py -v
They verify:

Removal of <think>...</think> tags and extra whitespace.

Truncation of over‑long user inputs (beyond 500 characters).

All tests should pass with green PASSED results.

6. Video Demonstrations
Three videos are provided to document the entire workflow. They are stored in the videos/ folder.

1 – Installation

2 – Implementation

3 – Testing

7. Project Structure
text
Blog Generation/
├── app.py                 # Main Streamlit application
├── test.py                # Simple script for direct model testing (optional)
├── test_model.py          # Pytest suite for model accuracy/performance/memory
├── test_utils.py          # Pytest suite for preprocessing/postprocessing
├── utils.py               # Helper functions (clean_response, preprocess_prompt)
├── requirements.txt       # Base Python dependencies
├── Qwen3.5-2B-Q4_K_M.gguf # Quantised model file (not included in repo)
├── videos/                # Contains the three demonstration videos
│   ├── ...1-installation.mp4
│   ├── ...2-implementation.mp4
│   └── ...3-testing.mp4
├── README.md              # This file
└── RESULTS.md             # Qualitative analysis and challenges encountered
8. Key Technical Decisions
Inference engine: llama-cpp-python used directly (instead of LangChain’s wrapper) to avoid asynchronous conflicts with Streamlit.

Quantisation: Q4_K_M – a good balance between model quality and resource consumption.

Frontend: Streamlit – minimal code required, quick prototyping.

Testing: Pytest with -s flag to reveal detailed print() outputs for clarity.

9. Acknowledgements
Model: Qwen3.5-2B by Alibaba Cloud, quantised by Unsloth.

Tools: llama-cpp-python, Streamlit, Pytest, psutil.

The LangChain community for initial integration ideas.

10. Contact
For any questions regarding this submission, please refer to the video demonstrations or the RESULTS.md file for troubleshooting notes.