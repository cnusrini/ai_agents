import os, time
from azure.ai.projects import AIProjectClient
from azure.identity import DefaultAzureCredential
from azure.ai.projects.models import MessageTextContent
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get credentials from .env
API_KEY = os.getenv("AZURE_AI_FOUNDRY_API_KEY")
CONNECTION_STRING = os.getenv("PROJECT_CONNECTION_STRING")
MODEL = os.getenv("MODEL_DEPLOYMENT_NAME")

# Validate credentials
if not API_KEY:
    raise ValueError("❌ AZURE_AI_FOUNDRY_API_KEY not found in .env file")
if not CONNECTION_STRING:
    raise ValueError("❌ PROJECT_CONNECTION_STRING not found in .env file")
if not MODEL:
    raise ValueError("❌ MODEL_DEPLOYMENT_NAME not found in .env file")

print("✅ Environment variables loaded successfully")
print(f"Model: {MODEL}")

try:
    print("Connecting to Azure AI Fondry Project")
    
    client = AIProjectClient(endpoint="eastus.api.azureml.ms;0f4acaab-6df7-4a91-97bd-a28fe902d0ca;n9nrg;azurehihubservice-project1", 
                             credential=AzureKeyCredential(API_KEY),
                             subscription_id="0f4acaab-6df7-4a91-97bd-a28fe902d0ca",
                             resource_group_name="n9nrg",
                             project_name="azurehihubservice-project1"
                             )
    print("connected to Azure AI Foundry Project")
    with client: 
        print("creating agent")
        agent = client.agents.create_agent(
            model=MODEL,
            name="my-assistant",
            instructions="You are a helpful assistant that provides informative answers.",
        )
        print(f"✅ Agent created successfully!")
        print(f"   Agent ID: {agent.id}")
     

        


except Exception as e:
    print(f"\n❌ Error: {type(e).__name__}")
    print(f"   Message: {str(e)}")

    traceback.print_exc()

print("\n✅ Script completed!")