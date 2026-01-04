import os
from dotenv import load_dotenv

load_dotenv()

MODEL_ID = "stabilityai/stable-diffusion-xl-base-1.0"
HF_TOKEN = os.getenv("HF_TOKEN")
