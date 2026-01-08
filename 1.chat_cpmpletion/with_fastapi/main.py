import os
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from openai import AzureOpenAI

load_dotenv()

client = AzureOpenAI(
    azure_endpoint=os.getenv("OPENAI_API_BASE"),
    api_key=os.getenv("OPENAI_API_KEY"),
    api_version="2025-01-01-preview",
)

DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT")
if not DEPLOYMENT:
    raise RuntimeError("Set AZURE_OPENAI_DEPLOYMENT in .env (this is your Azure deployment name).")

app = FastAPI()

class ChatReq(BaseModel):
    message: str

@app.post("/chat")
def chat(req: ChatReq):
    resp = client.chat.completions.create(
        model=DEPLOYMENT,  # REQUIRED: deployment name
        messages=[
            {"role": "system", "content": "You are a helpful AI assistant."},
            {"role": "user", "content": req.message},
        ],
    )
    return {"response": resp.choices[0].message.content}
