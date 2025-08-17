import os
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from huggingface_hub import InferenceClient

app = FastAPI()

# Mount a static directory to serve generated videos
if not os.path.exists("static"):
    os.makedirs("static")
app.mount("/static", StaticFiles(directory="static"), name="static")

# Hugging Face API key
HF_TOKEN = os.getenv("HF_TOKEN")

# Use InferenceClient with fal-ai provider
client = InferenceClient(
    provider="fal-ai",
    api_key=HF_TOKEN,
)

def text_to_video(prompt: str) -> str:
    """Generate video from text using fal-ai provider"""
    video = client.text_to_video(
        prompt,
        model="Wan-AI/Wan2.2-T2V-A14B",
    )
    video_path = os.path.join("static", "output.mp4")
    with open(video_path, "wb") as f:
        f.write(video)
    return video_path


@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <html>
        <head><title>AI Video Generator</title></head>
        <body style="font-family: sans-serif; margin: 2rem;">
            <h2>AI Video Generator </h2>
            <form action="/generate" method="post">
                <input type="text" name="prompt" placeholder="Enter your prompt" size="60" required>
                <button type="submit">Generate Video</button>
            </form>
        </body>
    </html>
    """


@app.post("/generate", response_class=HTMLResponse)
async def generate(prompt: str = Form(...)):
    try:
        video_path = text_to_video(prompt)

        # Return HTML with embedded video
        return f"""
        <html>
            <head><title>Generated Video</title></head>
            <body style="font-family: sans-serif; margin: 2rem;">
                <h2>Generated Video 🎥</h2>
                <video width="640" height="360" controls autoplay>
                    <source src="/{video_path}" type="video/mp4">
                    Your browser does not support the video tag.
                </video>
                <br><br>
                <a href="/"> Generate another</a>
            </body>
        </html>
        """
    except Exception as e:
        return f"<p>Error: {str(e)}</p>"
