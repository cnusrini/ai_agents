import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

AZURE_ENDPOINT = os.getenv("OPENAI_API_BASE")
AZURE_API_KEY = os.getenv("OPENAI_API_KEY")
DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT")

if not AZURE_ENDPOINT or not AZURE_API_KEY:
    raise RuntimeError("Set OPENAI_API_BASE and OPENAI_API_KEY in .env")
if not DEPLOYMENT:
    raise RuntimeError("Set AZURE_OPENAI_DEPLOYMENT in .env (your Azure deployment name).")

client = AzureOpenAI(
    azure_endpoint=AZURE_ENDPOINT,
    api_key=AZURE_API_KEY,
    api_version="2025-01-01-preview",
)

client.completions.

response = client.chat.completions.create(
    model=DEPLOYMENT,
    messages=[
        {"role": "system", "content": "You are a helpful AI assistant."},
        {"role": "user", "content": "whats the titanic journey about?"}
    ],
)

print("the information is:", response.choices[0].message.content, "\n")
