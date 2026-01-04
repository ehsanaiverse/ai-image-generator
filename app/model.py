from huggingface_hub import InferenceClient
from app.config import MODEL_ID, HF_TOKEN

client = InferenceClient(
    model=MODEL_ID,
    token=HF_TOKEN
)
