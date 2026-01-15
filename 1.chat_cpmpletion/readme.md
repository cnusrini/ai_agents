# Azure AI Foundry Chat Agent - Complete Tutorial

A comprehensive tutorial demonstrating how to build AI chat agents using Azure OpenAI service with three different implementation approaches: terminal-based, FastAPI with Swagger, and FastAPI with an intuitive UI interface.

## Azure AI Development Stack Architecture
````text
┌─────────────────────────────────────────────────────────────┐
│ LAYER 5: Your Application                                  │
│ (Your actual chatbot, agent, or AI app)                    │
└──────────────────────┬──────────────────────────────────────┘
                       │
         ┌─────────────┼─────────────┬──────────────┐
         ↓             ↓             ↓              ↓
┌──────────────┐ ┌──────────┐ ┌────────────┐ ┌──────────────┐
│ LAYER 4A:    │ │ LAYER 4B:│ │ LAYER 4C:  │ │ LAYER 4D:    │
│ LangChain    │ │ Semantic │ │ AutoGen    │ │ Direct Code  │
│ (Framework)  │ │ Kernel   │ │ (Multi-    │ │ (No          │
│              │ │ (MS      │ │ Agent)     │ │ Framework)   │
│              │ │ Framework│ │            │ │              │
└──────┬───────┘ └────┬─────┘ └─────┬──────┘ └──────┬───────┘
       │              │              │               │
       └──────────────┴──────────────┴───────────────┘
                       ↓
         ┌─────────────┴─────────────┐
         ↓                           ↓
┌──────────────────────┐   ┌──────────────────────┐
│ LAYER 3A:            │   │ LAYER 3B:            │
│ Azure AI Foundry SDK │   │ Azure OpenAI SDK     │
│ (Platform features)  │   │ (Direct API)         │
└──────────┬───────────┘   └──────────┬───────────┘
           │                          │
           └──────────┬───────────────┘
                      ↓
┌─────────────────────────────────────────────────────────────┐
│ LAYER 2: Azure AI Services (Infrastructure)                │
│ ├─ Azure OpenAI Service (GPT-4, GPT-3.5)                   │
│ ├─ Azure AI Search (Vector DB)                             │
│ ├─ Azure Content Safety                                    │
│ ├─ Azure AI Foundry (Platform/Portal)                      │
│ └─ Azure Storage, Functions, etc.                          │
└──────────────────────┬──────────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────────────────┐
│ LAYER 1: The Actual LLM (Same for all!)                    │
│ GPT-4, GPT-3.5 running on Azure infrastructure             │
│ (96 transformer layers, self-attention, etc.)              │
└─────────────────────────────────────────────────────────────┘
````

### Layer Descriptions

**Layer 5 - Your Application**
- Your custom-built chatbot, AI agent, or intelligent application
- This is where your business logic and user interface live

**Layer 4 - Optional Orchestration Frameworks**
- **4A - LangChain**: Third-party framework with rich ecosystem
- **4B - Semantic Kernel**: Microsoft's AI orchestration framework
- **4C - AutoGen**: Multi-agent conversation framework
- **4D - Direct Code**: Build without any framework

**Layer 3 - Azure SDKs**
- **3A - Azure AI Foundry SDK**: Platform approach with built-in RAG, evaluation, monitoring
- **3B - Azure OpenAI SDK**: Direct API access with full control

**Layer 2 - Azure AI Services**
- Azure OpenAI Service (hosts GPT-4, GPT-3.5)
- Azure AI Search (vector database and hybrid search)
- Azure Content Safety (content moderation)
- Supporting infrastructure (Storage, Functions, etc.)

**Layer 1 - The LLM Core**
- The actual GPT models running on Azure infrastructure
- Same transformer architecture regardless of which layers you use above
````
````

---



---


````

---


## 🎯 Overview

This repository contains three progressively enhanced implementations of an AI chat agent using Azure OpenAI:

1. **Terminal Version** (`with_terminal/`) - Simple command-line chat interface for quick testing
2. **FastAPI Version** (`with_fastapi/`) - RESTful API with Swagger documentation for programmatic access
3. **UI Version** (`with_ui/`) - Full-featured web interface with beautiful, responsive design

## ⚡ Quick Start

```bash
# 1. Clone and navigate
cd azure_foundary_tutorial/1.chat_cpmpletion

# 2. Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create .env file (add your Azure OpenAI credentials)
# See Configuration section below for details

# 5. Run your preferred version:

# Option A: Terminal
cd with_terminal && python main_terminal.py

# Option B: FastAPI (Swagger)
cd with_fastapi && uvicorn main:app --reload --log-level debug
# Visit: http://127.0.0.1:8000/docs

# Option C: Web UI
cd with_ui && uvicorn main:app --reload --port 8000
# Visit: http://127.0.0.1:8000/
```

## ✨ Features

- 🤖 **Azure OpenAI Integration** - Leverages Azure's enterprise-grade AI capabilities
- 🔄 **Multiple Deployment Options** - Choose the interface that fits your needs
- 📝 **Interactive Chat** - Natural conversation flow with AI assistant
- 🎨 **Modern UI** - Clean, gradient-enhanced interface (UI version)
- 📚 **API Documentation** - Auto-generated Swagger docs (FastAPI version)
- 🔒 **Environment-based Configuration** - Secure credential management

## 📁 Repository Structure

```
azure_foundary_tutorial/
├── 1.chat_cpmpletion/
│   ├── .env                           # Environment variables (root level)
│   ├── requirements.txt               # Python dependencies (root level)
│   ├── readme.md                      # This file
│   ├── with_terminal/
│   │   └── main_terminal.py          # Terminal-based chat
│   ├── with_fastapi/
│   │   └── main.py                    # FastAPI with Swagger
│   └── with_ui/
│       ├── main.py                    # FastAPI backend
│       └── ui.html                    # Frontend interface
```

**Important:** `.env` and `requirements.txt` must be placed at the root of `1.chat_cpmpletion/` directory, not inside individual folders.

## 🛠️ Prerequisites

Before you begin, ensure you have:

- **Python 3.8+** installed
- **Azure OpenAI Service** deployed with:
  - An active Azure subscription
  - Azure OpenAI resource created
  - A model deployment (e.g., GPT-4, GPT-3.5-turbo)
- **pip** (Python package manager)

## 📦 Installation

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd azure_foundary_tutorial/1.chat_cpmpletion
```

### 2. Set Up a Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv .venv

# Activate it
# On Windows:
.venv\Scripts\activate

# On macOS/Linux:
source .venv/bin/activate
```

### 3. Install Dependencies

Navigate to the root of the project and install required packages:

```bash
cd azure_foundary_tutorial/1.chat_cpmpletion
pip install -r requirements.txt
```

**Note:** The `requirements.txt` file should be located at `1.chat_cpmpletion/requirements.txt` (root level).

**Required packages:**
```txt
openai
python-dotenv
fastapi
uvicorn
pydantic
```

### 4. Configure Environment Variables

Create a `.env` file **at the root of `1.chat_cpmpletion/` directory** with your Azure OpenAI credentials:

```env
OPENAI_API_BASE=https://your-resource-name.openai.azure.com/
OPENAI_API_KEY=your-api-key-here
AZURE_OPENAI_DEPLOYMENT=your-deployment-name
```

**File location:**
```
1.chat_cpmpletion/
├── .env  ← Create it here (root level)
├── requirements.txt
├── with_terminal/
├── with_fastapi/
└── with_ui/
```

**Where to find these values:**
- **OPENAI_API_BASE**: Azure Portal → Your OpenAI Resource → Keys and Endpoint → Endpoint
- **OPENAI_API_KEY**: Azure Portal → Your OpenAI Resource → Keys and Endpoint → Key 1 or Key 2
- **AZURE_OPENAI_DEPLOYMENT**: Azure Portal → Your OpenAI Resource → Model deployments → Deployment name

## 🚀 Running the Applications

### Option 1: Terminal Version (Simplest)

Perfect for quick testing and command-line enthusiasts.

```bash
# Navigate to the with_terminal directory
cd 1.chat_cpmpletion/with_terminal

# Run the terminal chat
python main_terminal.py
```

**Usage:**
- Type your messages and press Enter
- Type `exit`, `quit`, or `q` to end the conversation

**Example:**
```
You: Hello, who are you?
AI: I'm a helpful AI assistant powered by Azure OpenAI...

You: What's the capital of France?
AI: The capital of France is Paris...

You: exit
```

---

### Option 2: FastAPI with Swagger (API Testing)

Ideal for developers who want to integrate the chat API or test via Swagger UI.

```bash
# Navigate to the with_fastapi directory
cd 1.chat_cpmpletion/with_fastapi

# Run with debug logging
uvicorn main:app --reload --log-level debug
```

**Expected output:**
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [xxxxx] using StatReload
INFO:     Started server process [xxxxx]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

**Access Points:**
- **Swagger UI**: http://127.0.0.1:8000/docs
- **API Endpoint**: http://127.0.0.1:8000/chat (POST)

**Testing via Swagger:**
1. Navigate to http://127.0.0.1:8000/docs
2. Click on **POST /chat**
3. Click **"Try it out"**
4. Enter your message in the request body:
   ```json
   {
     "message": "Hello, how are you?"
   }
   ```
5. Click **"Execute"**
6. View the AI response in the Response body

**Testing via cURL:**
```bash
curl -X POST "http://127.0.0.1:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{"message": "Tell me a joke"}'
```

**Testing via Python:**
```python
import requests

response = requests.post(
    "http://127.0.0.1:8000/chat",
    json={"message": "What's the weather like?"}
)
print(response.json())
```

---

### Option 3: Web UI Version (Best User Experience)

The most user-friendly option with a beautiful, responsive interface.

```bash
# Navigate to the with_ui directory
cd 1.chat_cpmpletion/with_ui

# Run the server
uvicorn main:app --reload --port 8000
```

**Expected output:**
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [xxxxx] using StatReload
INFO:     Started server process [xxxxx]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

**Access:**
- Open your browser and navigate to: **http://127.0.0.1:8000/**

**Features:**
- 💬 **Real-time chat interface** with gradient design
- ⚡ **Keyboard shortcuts**: 
  - `Enter` to send message
  - `Shift + Enter` for new line
- 🎨 **Message bubbles** with distinct styling for user/AI
- 🔄 **Status indicators** (Idle/Thinking)
- 🗑️ **Clear chat** functionality
- 📱 **Responsive design** for mobile and desktop

**Usage:**
1. Type your message in the text area
2. Press Enter or click "Send"
3. Wait for the AI response (status changes to "Thinking...")
4. Continue the conversation
5. Click "Clear" to reset the chat

---

## 🔧 Troubleshooting

### Common Issues

**1. "ModuleNotFoundError: No module named 'openai'"**
```bash
pip install openai python-dotenv fastapi uvicorn
```

**2. "RuntimeError: Set AZURE_OPENAI_DEPLOYMENT in .env"**
- Ensure your `.env` file exists at `1.chat_cpmpletion/.env` (root level, NOT in subfolders)
- Verify all three environment variables are set correctly:
  ```bash
  # Check if .env file exists in the right location
  ls -la 1.chat_cpmpletion/.env
  
  # View the contents (be careful not to expose your API key)
  cat 1.chat_cpmpletion/.env
  ```
- Make sure there are no typos in variable names
- Ensure there are no extra spaces around the `=` sign

**3. "Request failed: TypeError: Failed to fetch" (UI Version)**
- Make sure you're accessing the UI through FastAPI: http://127.0.0.1:8000/
- Do NOT open `ui.html` directly in the browser
- Verify FastAPI server is running on port 8000

**4. Azure OpenAI API Errors**
- Check your API key is valid and not expired
- Verify your deployment name matches exactly (case-sensitive)
- Ensure your Azure subscription is active
- Check Azure OpenAI resource quotas and rate limits

**5. Port Already in Use**

If you see an error that port 8000 is already in use, you need to kill the existing process:

**Check what's using port 8000:**
```bash
# On macOS/Linux:
lsof -i :8000

# Output example:
COMMAND   PID      USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
python3.1 68631 srivrinda   3u  IPv4 0xd2b8bf950056f84b      0t0  TCP localhost:irdmi (LISTEN)
```

**Kill the process:**
```bash
# Replace PID with the actual process ID from lsof output
kill -9 68631

# Verify it's killed
lsof -i :8000
```

**Or use a different port:**
```bash
uvicorn main:app --reload --port 8001
```

**On Windows:**
```powershell
# Check port usage
netstat -ano | findstr :8000

# Kill process (replace PID with actual process ID)
taskkill /PID <PID> /F
```

## 🧪 Testing Guide

### Terminal Version
```bash
cd 1.chat_cpmpletion/with_terminal
python main_terminal.py

# Test various prompts:
# - "Explain quantum computing in simple terms"
# - "Write a Python function to reverse a string"
# - "What's the difference between AI and ML?"
```

### FastAPI Version
```bash
cd 1.chat_cpmpletion/with_fastapi
uvicorn main:app --reload --log-level debug

# In another terminal:
curl -X POST "http://127.0.0.1:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{"message": "Test message"}'
```

### UI Version
```bash
cd 1.chat_cpmpletion/with_ui
uvicorn main:app --reload --port 8000

# Open browser to http://127.0.0.1:8000/
# Test the interactive chat interface
```

## 📚 Technology Stack

- **Azure OpenAI** - AI language model service
- **Python 3.8+** - Programming language
- **FastAPI** - Modern web framework for APIs
- **Uvicorn** - ASGI server
- **Pydantic** - Data validation
- **python-dotenv** - Environment variable management
- **HTML/CSS/JavaScript** - Frontend (UI version)

## 🎓 Learning Path

This tutorial demonstrates:

1. **Basic Azure OpenAI Integration** - Learn how to connect to Azure OpenAI service
2. **REST API Development** - Build production-ready APIs with FastAPI
3. **Web Interface Design** - Create modern, responsive UIs
4. **Best Practices** - Environment management, error handling, CORS configuration

## 📝 API Reference

### POST /chat

**Request Body:**
```json
{
  "message": "string"
}
```

**Response:**
```json
{
  "response": "string"
}
```

**Example:**
```bash
curl -X POST "http://127.0.0.1:8000/chat" \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello, AI!"}'

# Response:
{
  "response": "Hello! How can I assist you today?"
}
```

## 🔐 Security Notes

- ⚠️ **Never commit `.env` files** to version control
- 🔒 **Keep API keys secure** - Use Azure Key Vault in production
- 🌐 **CORS is configured for local development** - Restrict origins in production
- 🛡️ **Rate limiting** - Implement rate limiting for production deployments

## 🚀 Next Steps

Enhance this project by:

- 🧠 Adding conversation memory (chat history)
- 💾 Implementing persistent storage (database)
- 🔐 Adding user authentication
- 🎨 Enhancing the UI with streaming responses
- 📊 Adding analytics and monitoring
- 🌍 Deploying to Azure App Service or Container Apps
- 🔄 Implementing retry logic and circuit breakers

## 📄 License

This project is open source and available for educational purposes.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 📧 Support

If you encounter any issues or have questions:

### 🔍 Troubleshooting Steps:
1. Check the **Troubleshooting** section above
2. Review Azure OpenAI documentation: https://learn.microsoft.com/azure/ai-services/openai/
3. Verify your `.env` file is at the correct location (`1.chat_cpmpletion/.env`)
4. Ensure your virtual environment is activated

### 💬 Community & Discussion:

**Join our Discord community** for:
- 🤝 Real-time help and support
- 💡 Feature discussions and ideas
- 🎓 Learning resources and tips
- 👥 Connect with other developers

**Discord Server:** [discord](https://discord.gg/Q2eDDEU7)

### 🐛 Report Issues:
Open an issue in this repository with:
- Detailed description of the problem
- Error messages (if any)
- Steps to reproduce
- Your environment (OS, Python version)

---

**Built with ❤️ using Azure AI Foundry**

*Last updated: January 2026*