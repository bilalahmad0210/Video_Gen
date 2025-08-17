# AI Video Generator

A simple, full-stack web application that generates video clips from text prompts. The app is built with **FastAPI** and uses the **Hugging Face InferenceClient** to connect to the **fal-ai** provider for text-to-video generation.

**Live Demo:** [https://video-gen-vc70.onrender.com](https://video-gen-vc70.onrender.com)

---

## Project Flow

```
User Input (HTML Form)
         ↓
  FastAPI Backend (app.py)
         ↓
Hugging Face InferenceClient
         ↓
   fal-ai Provider
         ↓
`Wan-AI/Wan2.2-T2V-A14B` Model
         ↓
  Generated Video (MP4)
         ↓
  Displayed in Browser
```

---

## Folder Structure

```
video-generator/
├── static/              # Stores generated videos
│   └── output.mp4
├── .env                 # For your secret API key
├── app.py               # The main FastAPI application
└── requirements.txt     # Python dependencies
```

---

## Technology Stack

| Component    | Choice                       | Reason                                         |
|-------------|-------------------------------|-----------------------------------------------|
| Backend      | FastAPI                       | High-performance, asynchronous web framework |
| AI Service   | Hugging Face InferenceClient  | Simple interface for interacting with ML models |
| AI Provider  | fal-ai                        | Provides access to the text-to-video model endpoint |
| Video Model  | Wan-AI/Wan2.2-T2V-A14B       | The specific text-to-video generation model used |
| Deployment   | Render                        | Based on the provided live demo URL          |

---

## How to Run Locally

### 1. Clone and Set Up Environment

```bash
# Clone the repository (example)
git clone <your-repo-url>
cd video-generator

# Create and activate a virtual environment
python -m venv env
env\Scripts\activate  # On Windows
# source env/bin/activate on macOS/Linux

# Install the required packages
pip install -r requirements.txt
```

### 2. Set Up Environment Variables

Create a file named `.env` in the root directory and add your Hugging Face API key:

```env
HF_TOKEN="your-hugging-face-api-key"
```

### 3. Launch the Application

```bash
# Run the FastAPI server
uvicorn app:app --reload
```

- Backend runs at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Usage

1. Open the application in your browser.
2. Enter a text prompt describing the video you want to generate.
3. Submit the form and wait for the video to be generated.
4. The generated video will be displayed in the browser and saved in `static/output.mp4`.

---

## Notes

- Ensure you have a valid Hugging Face API key with access to the fal-ai provider.
- Video generation can take time depending on the model and prompt complexity.

