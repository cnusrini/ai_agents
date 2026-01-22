# Medical Claims Chatbot: Complete Azure Architecture

## Executive Summary

This document provides a comprehensive architectural blueprint for building an intelligent medical claims chatbot using Microsoft's complete AI stack. This is designed for technical architects, solution architects, and IT leaders who need to understand the complete technology landscape.

---

## Table of Contents

1. [Complete Technology Stack Overview](#complete-technology-stack-overview)
2. [High-Level Architecture Diagram](#high-level-architecture-diagram)
3. [Detailed Component Architecture](#detailed-component-architecture)
4. [Azure AI Foundry Integration](#azure-ai-foundry-integration)
5. [Data Flow: End-to-End Journey](#data-flow-end-to-end-journey)
6. [Service-by-Service Breakdown](#service-by-service-breakdown)
7. [Integration Patterns](#integration-patterns)
8. [Deployment Architecture](#deployment-architecture)
9. [Security Architecture](#security-architecture)
10. [Monitoring and Observability](#monitoring-and-observability)

---

## Complete Technology Stack Overview

### The Full Microsoft AI Ecosystem
```
┌─────────────────────────────────────────────────────────────────────┐
│                    PRESENTATION LAYER                               │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │  Microsoft Copilot Studio                                    │  │
│  │  - Web Chat Widget                                           │  │
│  │  - Microsoft Teams Integration                               │  │
│  │  - Voice Channel (Phone)                                     │  │
│  │  - SMS Channel                                               │  │
│  └──────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│                    ORCHESTRATION LAYER                              │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │  Power Platform                                              │  │
│  │  ┌────────────────────────────────────────────────────────┐ │  │
│  │  │  Power Automate (Cloud Flows)                          │ │  │
│  │  │  - Workflow orchestration                              │ │  │
│  │  │  - Data transformation                                 │ │  │
│  │  │  - System integration                                  │ │  │
│  │  └────────────────────────────────────────────────────────┘ │  │
│  │  ┌────────────────────────────────────────────────────────┐ │  │
│  │  │  Dataverse (Optional)                                  │ │  │
│  │  │  - Conversation history storage                        │ │  │
│  │  │  - User preferences                                    │ │  │
│  │  └────────────────────────────────────────────────────────┘ │  │
│  └──────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│                    AI INTELLIGENCE LAYER                            │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │  Azure AI Foundry                                            │  │
│  │  ┌────────────────────────────────────────────────────────┐ │  │
│  │  │  AI Project                                            │ │  │
│  │  │  - Agent configuration                                 │ │  │
│  │  │  - Model deployments                                   │ │  │
│  │  │  - Prompt management                                   │ │  │
│  │  │  - Evaluation & monitoring                             │ │  │
│  │  └────────────────────────────────────────────────────────┘ │  │
│  │  ┌────────────────────────────────────────────────────────┐ │  │
│  │  │  Azure OpenAI Service                                  │ │  │
│  │  │  - GPT-4 deployment                                    │ │  │
│  │  │  - GPT-4o deployment (multi-modal)                     │ │  │
│  │  │  - Embeddings (text-embedding-3-large)                 │ │  │
│  │  └────────────────────────────────────────────────────────┘ │  │
│  └──────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│                    APPLICATION LAYER                                │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │  Azure Functions (Serverless Compute)                        │  │
│  │  ┌────────────────────────────────────────────────────────┐ │  │
│  │  │  Function App: Claims-Processing-API                   │ │  │
│  │  │  ┌──────────────────────────────────────────────────┐ │ │  │
│  │  │  │  Semantic Kernel Framework                       │ │ │  │
│  │  │  │  - Kernel orchestration                          │ │ │  │
│  │  │  │  - Plugin management                             │ │ │  │
│  │  │  │  - Agent execution                               │ │ │  │
│  │  │  │  - Function calling logic                        │ │ │  │
│  │  │  └──────────────────────────────────────────────────┘ │ │  │
│  │  │  ┌──────────────────────────────────────────────────┐ │ │  │
│  │  │  │  Native Plugins                                  │ │ │  │
│  │  │  │  - ClaimsPlugin                                  │ │ │  │
│  │  │  │  - ValidationPlugin                              │ │ │  │
│  │  │  │  - EscalationPlugin                              │ │ │  │
│  │  │  └──────────────────────────────────────────────────┘ │ │  │
│  │  │  ┌──────────────────────────────────────────────────┐ │ │  │
│  │  │  │  Prompt Plugins                                  │ │ │  │
│  │  │  │  - PolicyPlugin (RAG-based)                      │ │ │  │
│  │  │  │  - ExplanationPlugin                             │ │ │  │
│  │  │  └──────────────────────────────────────────────────┘ │ │  │
│  │  └────────────────────────────────────────────────────────┘ │  │
│  └──────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│                    DATA & SEARCH LAYER                              │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │  Azure AI Search (Cognitive Search)                          │  │
│  │  - Policy documents index                                    │  │
│  │  - Vector search enabled                                     │  │
│  │  - Semantic ranking                                          │  │
│  │  - Integrated vectorization                                  │  │
│  └──────────────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │  Azure SQL Database                                          │  │
│  │  - Claims data                                               │  │
│  │  - Patient information                                       │  │
│  │  - Transaction history                                       │  │
│  └──────────────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │  Azure Blob Storage                                          │  │
│  │  - Policy documents (PDFs)                                   │  │
│  │  - Claim attachments                                         │  │
│  │  - Audit logs archive                                        │  │
│  └──────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│                    SECURITY & MANAGEMENT LAYER                      │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────────────────┐ │
│  │  Azure AD    │  │  Key Vault   │  │  Azure Monitor           │ │
│  │  (Entra ID)  │  │  - Secrets   │  │  - Application Insights  │ │
│  │  - Auth      │  │  - API keys  │  │  - Log Analytics         │ │
│  │  - MFA       │  │  - Conn str  │  │  - Alerts                │ │
│  └──────────────┘  └──────────────┘  └──────────────────────────┘ │
└─────────────────────────────────────────────────────────────────────┘
```

---

## High-Level Architecture Diagram

### Complete System Architecture
```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                                                                                 │
│                          PATIENT ACCESS POINTS                                  │
│                                                                                 │
│   ┌──────────────┐    ┌──────────────┐    ┌──────────────┐    ┌────────────┐ │
│   │   Website    │    │  Teams App   │    │    Phone     │    │    SMS     │ │
│   │  Chat Widget │    │   Channel    │    │   (Voice)    │    │  Channel   │ │
│   └──────┬───────┘    └──────┬───────┘    └──────┬───────┘    └─────┬──────┘ │
│          │                   │                   │                   │         │
│          └───────────────────┴───────────────────┴───────────────────┘         │
│                                      ↓                                          │
│   ┌─────────────────────────────────────────────────────────────────────────┐  │
│   │                     MICROSOFT COPILOT STUDIO                            │  │
│   │                        (SaaS - Microsoft Managed)                       │  │
│   │                                                                         │  │
│   │  ┌────────────────────────────────────────────────────────────────┐    │  │
│   │  │  Conversation Manager                                          │    │  │
│   │  │  - Intent Recognition (NLU)                                    │    │  │
│   │  │  - Dialog State Machine                                        │    │  │
│   │  │  - Context & Session Management                                │    │  │
│   │  │  - Entity Extraction                                           │    │  │
│   │  └────────────────────────────────────────────────────────────────┘    │  │
│   │                                                                         │  │
│   │  ┌────────────────────────────────────────────────────────────────┐    │  │
│   │  │  Topics (Conversation Flows)                                   │    │  │
│   │  │                                                                 │    │  │
│   │  │  Built-in Topics:                  Custom Topics:              │    │  │
│   │  │  ├─ Greeting                       ├─ Check Claim Status       │    │  │
│   │  │  ├─ Goodbye                        ├─ Explain Coverage         │    │  │
│   │  │  ├─ Escalate to Agent              ├─ View Claim Details       │    │  │
│   │  │  ├─ Fallback/Confused              ├─ File Appeal              │    │  │
│   │  │  └─ Transfer Handoff               ├─ Find Claims by Date      │    │  │
│   │  │                                     └─ Policy Questions         │    │  │
│   │  └────────────────────────────────────────────────────────────────┘    │  │
│   │                                                                         │  │
│   │  When Complex Logic Needed → Trigger Power Automate                    │  │
│   └─────────────────────────────────────────────────────────────────────────┘  │
│                                      ↓                                          │
└─────────────────────────────────────────────────────────────────────────────────┘
                                       ↓
┌─────────────────────────────────────────────────────────────────────────────────┐
│                                                                                 │
│                           POWER PLATFORM LAYER                                  │
│                                                                                 │
│   ┌─────────────────────────────────────────────────────────────────────────┐  │
│   │                          POWER AUTOMATE                                 │  │
│   │                     (Cloud Flows - SaaS)                                │  │
│   │                                                                         │  │
│   │  Flow 1: ProcessClaimStatusQuery                                       │  │
│   │  ┌──────────────────────────────────────────────────────────────────┐  │  │
│   │  │  Trigger: Called from Copilot Studio                             │  │  │
│   │  │  ↓                                                                │  │  │
│   │  │  Input: { patientId, query, conversationId }                     │  │  │
│   │  │  ↓                                                                │  │  │
│   │  │  Action: Validate patient authentication                         │  │  │
│   │  │  ↓                                                                │  │  │
│   │  │  Action: HTTP POST to Azure Function                             │  │  │
│   │  │          URL: https://claims-api.azurewebsites.net/api/process  │  │  │
│   │  │  ↓                                                                │  │  │
│   │  │  Action: Receive JSON response                                   │  │  │
│   │  │  ↓                                                                │  │  │
│   │  │  Action: Format response for Copilot Studio                      │  │  │
│   │  │  ↓                                                                │  │  │
│   │  │  Return: Structured response with adaptive cards                 │  │  │
│   │  └──────────────────────────────────────────────────────────────────┘  │  │
│   │                                                                         │  │
│   │  Flow 2: PolicyQuestionHandler                                         │  │
│   │  ┌──────────────────────────────────────────────────────────────────┐  │  │
│   │  │  Trigger: Policy-related question detected                       │  │  │
│   │  │  ↓                                                                │  │  │
│   │  │  Action: Call Azure Function (RAG endpoint)                      │  │  │
│   │  │  ↓                                                                │  │  │
│   │  │  Action: Enrich with patient plan details from Dataverse         │  │  │
│   │  │  ↓                                                                │  │  │
│   │  │  Return: Answer with policy citations                            │  │  │
│   │  └──────────────────────────────────────────────────────────────────┘  │  │
│   │                                                                         │  │
│   │  Flow 3: EscalateToHuman                                                │  │
│   │  ┌──────────────────────────────────────────────────────────────────┐  │  │
│   │  │  Trigger: User requests human or bot can't help                  │  │  │
│   │  │  ↓                                                                │  │  │
│   │  │  Action: Create case in Dynamics 365                             │  │  │
│   │  │  ↓                                                                │  │  │
│   │  │  Action: Check agent availability (Omnichannel API)              │  │  │
│   │  │  ↓                                                                │  │  │
│   │  │  Condition: Agent available?                                     │  │  │
│   │  │     Yes → Transfer to agent with context                         │  │  │
│   │  │     No  → Create ticket, notify patient of callback              │  │  │
│   │  └──────────────────────────────────────────────────────────────────┘  │  │
│   └─────────────────────────────────────────────────────────────────────────┘  │
│                                                                                 │
│   ┌─────────────────────────────────────────────────────────────────────────┐  │
│   │                      DATAVERSE (Optional)                               │  │
│   │  - Conversation transcripts                                             │  │
│   │  - Patient preferences                                                  │  │
│   │  - Custom entities for tracking                                         │  │
│   └─────────────────────────────────────────────────────────────────────────┘  │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
                                       ↓
┌─────────────────────────────────────────────────────────────────────────────────┐
│                                                                                 │
│                         AZURE AI FOUNDRY LAYER                                  │
│                                                                                 │
│   ┌─────────────────────────────────────────────────────────────────────────┐  │
│   │                    AZURE AI FOUNDRY PROJECT                             │  │
│   │                   (ai.azure.com - Project Hub)                          │  │
│   │                                                                         │  │
│   │  ┌────────────────────────────────────────────────────────────────┐    │  │
│   │  │  Project: Medical-Claims-Chatbot-Prod                         │    │  │
│   │  │                                                                │    │  │
│   │  │  Components:                                                   │    │  │
│   │  │  ┌──────────────────────────────────────────────────────────┐ │    │  │
│   │  │  │  Model Deployments                                       │ │    │  │
│   │  │  │  ├─ gpt-4 (Latest)                                       │ │    │  │
│   │  │  │  ├─ gpt-4o (Multi-modal for images)                      │ │    │  │
│   │  │  │  └─ text-embedding-3-large (For vectors)                 │ │    │  │
│   │  │  └──────────────────────────────────────────────────────────┘ │    │  │
│   │  │                                                                │    │  │
│   │  │  ┌──────────────────────────────────────────────────────────┐ │    │  │
│   │  │  │  Agent Configuration (Optional)                          │ │    │  │
│   │  │  │  - Agent: ClaimsAssistantAgent                           │ │    │  │
│   │  │  │  - Instructions: System prompt for medical claims        │ │    │  │
│   │  │  │  - Tools: Connected to Semantic Kernel plugins           │ │    │  │
│   │  │  │  - Grounding: Azure AI Search integration                │ │    │  │
│   │  │  └──────────────────────────────────────────────────────────┘ │    │  │
│   │  │                                                                │    │  │
│   │  │  ┌──────────────────────────────────────────────────────────┐ │    │  │
│   │  │  │  Evaluation & Monitoring                                 │ │    │  │
│   │  │  │  - Groundedness evaluations                              │ │    │  │
│   │  │  │  - Relevance scoring                                     │ │    │  │
│   │  │  │  - Response quality metrics                              │ │    │  │
│   │  │  │  - Token usage tracking                                  │ │    │  │
│   │  │  └──────────────────────────────────────────────────────────┘ │    │  │
│   │  │                                                                │    │  │
│   │  │  ┌──────────────────────────────────────────────────────────┐ │    │  │
│   │  │  │  Prompt Flow (Optional)                                  │ │    │  │
│   │  │  │  - Visual prompt orchestration                           │ │    │  │
│   │  │  │  - Testing and debugging                                 │ │    │  │
│   │  │  └──────────────────────────────────────────────────────────┘ │    │  │
│   │  └────────────────────────────────────────────────────────────────┘    │  │
│   └─────────────────────────────────────────────────────────────────────────┘  │
│                                                                                 │
│   ┌─────────────────────────────────────────────────────────────────────────┐  │
│   │               AZURE OPENAI SERVICE                                      │  │
│   │               (Connected to AI Foundry Project)                         │  │
│   │                                                                         │  │
│   │  Resource: claims-chatbot-openai                                       │  │
│   │  Region: East US                                                        │  │
│   │  SKU: Standard                                                          │  │
│   │                                                                         │  │
│   │  Deployments:                                                           │  │
│   │  ├─ gpt-4 (deployment: gpt-4-prod)                                     │  │
│   │  │  Capacity: 30K TPM (tokens per minute)                              │  │
│   │  │  Version: Latest stable                                             │  │
│   │  │                                                                      │  │
│   │  ├─ gpt-4o (deployment: gpt-4o-prod)                                   │  │
│   │  │  Capacity: 20K TPM                                                  │  │
│   │  │  Use: Multi-modal (handle images in claims)                         │  │
│   │  │                                                                      │  │
│   │  └─ text-embedding-3-large (deployment: embeddings-prod)               │  │
│   │     Capacity: 100K TPM                                                 │  │
│   │     Use: Generate vectors for policy documents                         │  │
│   │                                                                         │  │
│   │  Features Enabled:                                                      │  │
│   │  ├─ Content filtering (Moderate)                                       │  │
│   │  ├─ Abuse monitoring                                                   │  │
│   │  ├─ Private endpoint                                                   │  │
│   │  └─ Managed identity authentication                                    │  │
│   └─────────────────────────────────────────────────────────────────────────┘  │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
                                       ↓
┌─────────────────────────────────────────────────────────────────────────────────┐
│                                                                                 │
│                      AZURE FUNCTIONS (COMPUTE LAYER)                            │
│                                                                                 │
│   ┌─────────────────────────────────────────────────────────────────────────┐  │
│   │  Function App: claims-processing-func-prod                              │  │
│   │  Runtime: Python 3.11                                                   │  │
│   │  Plan: Premium (EP1) - Always on, faster cold start                     │  │
│   │  Region: East US (same as Azure OpenAI)                                 │  │
│   │                                                                         │  │
│   │  ┌─────────────────────────────────────────────────────────────────┐   │  │
│   │  │  Function: ProcessClaimsQuery                                   │   │  │
│   │  │  Trigger: HTTP POST                                             │   │  │
│   │  │  Endpoint: /api/process                                         │   │  │
│   │  │  ┌──────────────────────────────────────────────────────────┐  │   │  │
│   │  │  │  SEMANTIC KERNEL ORCHESTRATION                           │  │   │  │
│   │  │  │                                                           │  │   │  │
│   │  │  │  from semantic_kernel import Kernel                      │  │   │  │
│   │  │  │  from semantic_kernel.agents import ChatCompletionAgent │  │   │  │
│   │  │  │                                                           │  │   │  │
│   │  │  │  1. Initialize Kernel                                    │  │   │  │
│   │  │  │     ├─ Add Azure OpenAI service                          │  │   │  │
│   │  │  │     ├─ Load plugins from /plugins directory              │  │   │  │
│   │  │  │     └─ Configure function calling                        │  │   │  │
│   │  │  │                                                           │  │   │  │
│   │  │  │  2. Create Agent                                         │  │   │  │
│   │  │  │     ├─ ChatCompletionAgent or AzureAIAgent               │  │   │  │
│   │  │  │     ├─ Instructions: Medical claims specialist           │  │   │  │
│   │  │  │     └─ Available tools: All registered plugins           │  │   │  │
│   │  │  │                                                           │  │   │  │
│   │  │  │  3. Process Request                                      │  │   │  │
│   │  │  │     ├─ Parse incoming query                              │  │   │  │
│   │  │  │     ├─ Add to chat history                               │  │   │  │
│   │  │  │     ├─ Invoke agent with context                         │  │   │  │
│   │  │  │     └─ Agent orchestrates function calls                 │  │   │  │
│   │  │  │                                                           │  │   │  │
│   │  │  │  4. Return Response                                      │  │   │  │
│   │  │  │     ├─ Format as JSON                                    │  │   │  │
│   │  │  │     ├─ Include structured data + text                    │  │   │  │
│   │  │  │     └─ Add suggested actions                             │  │   │  │
│   │  │  └──────────────────────────────────────────────────────────┘  │   │  │
│   │  └─────────────────────────────────────────────────────────────────┘   │  │
│   │                                                                         │  │
│   │  ┌─────────────────────────────────────────────────────────────────┐   │  │
│   │  │  SEMANTIC KERNEL PLUGINS                                        │   │  │
│   │  │                                                                 │   │  │
│   │  │  /plugins/ClaimsPlugin/ (Native Plugin)                        │   │  │
│   │  │  ├─ __init__.py                                                │   │  │
│   │  │  └─ claims_functions.py                                        │   │  │
│   │  │     @kernel_function                                           │   │  │
│   │  │     def get_claim_status(claim_id: str) -> dict:               │   │  │
│   │  │         # Query Azure SQL for claim                            │   │  │
│   │  │         return claim_data                                       │   │  │
│   │  │                                                                 │   │  │
│   │  │     @kernel_function                                           │   │  │
│   │  │     def search_claims(patient_id: str, date_range: str):       │   │  │
│   │  │         # Complex SQL query with joins                         │   │  │
│   │  │         return claims_list                                      │   │  │
│   │  │                                                                 │   │  │
│   │  │  /plugins/PolicyPlugin/ (Prompt Plugin with RAG)               │   │  │
│   │  │  ├─ CheckCoverage/                                             │   │  │
│   │  │  │  ├─ skprompt.txt                                            │   │  │
│   │  │  │  │  "Based on the policy documents: {{$documents}}         │   │  │
│   │  │  │  │   Does the plan cover: {{$procedure}}?                  │   │  │
│   │  │  │  │   Provide answer with citations."                       │   │  │
│   │  │  │  └─ config.json                                            │   │  │
│   │  │  │     { "temperature": 0.3, "max_tokens": 500 }              │   │  │
│   │  │  │                                                             │   │  │
│   │  │  │  Python code:                                               │   │  │
│   │  │  │  @kernel_function                                           │   │  │
│   │  │  │  async def check_coverage(procedure: str) -> str:           │   │  │
│   │  │  │      # 1. Query Azure AI Search for relevant policy docs   │   │  │
│   │  │  │      # 2. Get top 5 relevant chunks                         │   │  │
│   │  │  │      # 3. Call prompt template with documents               │   │  │
│   │  │  │      # 4. Return answer with citations                      │   │  │
│   │  │                                                                 │   │  │
│   │  │  /plugins/ValidationPlugin/ (Native Plugin)                    │   │  │
│   │  │  └─ validation_functions.py                                    │   │  │
│   │  │     @kernel_function                                           │   │  │
│   │  │     def validate_patient_access(patient_id: str, user_id: str):│   │  │
│   │  │         # Check if logged-in user can access patient data      │   │  │
│   │  │         # Query SQL with row-level security                    │   │  │
│   │  │         return is_authorized                                   │   │  │
│   │  │                                                                 │   │  │
│   │  │  /plugins/EscalationPlugin/ (Native Plugin)                    │   │  │
│   │  │  └─ escalation_functions.py                                    │   │  │
│   │  │     @kernel_function                                           │   │  │
│   │  │     def create_support_ticket(issue: str, context: dict):      │   │  │
│   │  │         # Create ticket in Dynamics 365 via API                │   │  │
│   │  │         return ticket_id                                       │   │  │
│   │  └─────────────────────────────────────────────────────────────────┘   │  │
│   │                                                                         │  │
│   │  Configuration (Environment Variables from Key Vault):                 │  │
│   │  ├─ AZURE_OPENAI_ENDPOINT                                              │  │
│   │  ├─ AZURE_OPENAI_KEY (Managed Identity preferred)                      │  │
│   │  ├─ AZURE_SEARCH_ENDPOINT                                              │  │
│   │  ├─ AZURE_SEARCH_KEY                                                   │  │
│   │  ├─ SQL_CONNECTION_STRING                                              │  │
│   │  └─ APPLICATIONINSIGHTS_CONNECTION_STRING                              │  │
│   └─────────────────────────────────────────────────────────────────────────┘  │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
                                       ↓
┌─────────────────────────────────────────────────────────────────────────────────┐
│                                                                                 │
│                         DATA & SEARCH SERVICES                                  │
│                                                                                 │
│   ┌─────────────────────────────────────────────────────────────────────────┐  │
│   │  AZURE AI SEARCH (Cognitive Search)                                     │  │
│   │  Resource: claims-policy-search-prod                                    │  │
│   │  SKU: Standard S1                                                        │  │
│   │  Region: East US                                                         │  │
│   │                                                                         │  │
│   │  Index: policy-documents-index                                          │  │
│   │  ┌─────────────────────────────────────────────────────────────────┐   │  │
│   │  │  Fields:                                                         │   │  │
│   │  │  ├─ id (Edm.String, Key)                                        │   │  │
│   │  │  ├─ content (Edm.String, Searchable)                            │   │  │
│   │  │  ├─ title (Edm.String, Searchable, Filterable)                  │   │  │
│   │  │  ├─ document_type (Edm.String, Filterable)                      │   │  │
│   │  │  ├─ section (Edm.String, Filterable)                            │   │  │
│   │  │  ├─ chunk_number (Edm.Int32)                                    │   │  │
│   │  │  └─ content_vector (Collection(Edm.Single), Searchable)         │   │  │
│   │  │     Dimensions: 3072 (text-embedding-3-large)                   │   │  │
│   │  └─────────────────────────────────────────────────────────────────┘   │  │
│   │                                                                         │  │
│   │  Indexer: policy-docs-indexer                                           │  │
│   │  ┌─────────────────────────────────────────────────────────────────┐   │  │
│   │  │  Data Source: Azure Blob Storage (policy-docs container)        │   │  │
│   │  │  Schedule: Daily at 2 AM                                        │   │  │
│   │  │  ┌──────────────────────────────────────────────────────────┐  │   │  │
│   │  │  │  Skillset: policy-enrichment-skillset                    │  │   │  │
│   │  │  │  ┌────────────────────────────────────────────────────┐  │  │   │  │
│   │  │  │  │  1. OCR Skill (extract text from PDFs)            │  │  │   │  │
│   │  │  │  │  2. Text Split Skill (chunk into 800-token chunks)│  │  │   │  │
│   │  │  │  │  3. Azure OpenAI Embedding Skill                  │  │  │   │  │
│   │  │  │  │     Model: text-embedding-3-large                  │  │  │   │  │
│   │  │  │  │     Generates vectors for each chunk               │  │  │   │  │
│   │  │  │  └────────────────────────────────────────────────────┘  │  │   │  │
│   │  │  └──────────────────────────────────────────────────────────┘  │   │  │
│   │  └─────────────────────────────────────────────────────────────────┘   │  │
│   │                                                                         │  │
│   │  Search Features Enabled:                                               │  │
│   │  ├─ Vector search (k-NN, HNSW algorithm)                                │  │
│   │  ├─ Semantic ranking (L2 reranking)                                     │  │
│   │  ├─ Integrated vectorization                                            │  │
│   │  └─ Hybrid search (keyword + vector)                                    │  │
│   └─────────────────────────────────────────────────────────────────────────┘  │
│                                                                                 │
│   ┌─────────────────────────────────────────────────────────────────────────┐  │
│   │  AZURE SQL DATABASE                                                     │  │
│   │  Server: claims-sql-server-prod.database.windows.net                   │  │
│   │  Database: ClaimsDB                                                     │  │
│   │  Tier: Standard S3 (100 DTUs)                                           │  │
│   │  Region: East US                                                        │  │
│   │                                                                         │  │
│   │  Tables:                                                                │  │
│   │  ┌─────────────────────────────────────────────────────────────────┐   │  │
│   │  │  Claims                                                          │   │  │
│   │  │  ├─ ClaimID (PK)                                                │   │  │
│   │  │  ├─ PatientID (FK, indexed)                                     │   │  │
│   │  │  ├─ ClaimDate                                                   │   │  │
│   │  │  ├─ ProcedureCode                                               │   │  │
│   │  │  ├─ Status (Submitted/Processing/Paid/Denied)                   │   │  │
│   │  │  ├─ Amount                                                      │   │  │
│   │  │  ├─ DenialReason                                                │   │  │
│   │  │  └─ LastUpdated                                                 │   │  │
│   │  └─────────────────────────────────────────────────────────────────┘   │  │
│   │                                                                         │  │
│   │  ┌─────────────────────────────────────────────────────────────────┐   │  │
│   │  │  Patients                                                        │   │  │
│   │  │  ├─ PatientID (PK)                                              │   │  │
│   │  │  ├─ UserID (from Azure AD, unique)                              │   │  │
│   │  │  ├─ PlanType                                                    │   │  │
│   │  │  ├─ Deductible                                                  │   │  │
│   │  │  └─ EnrollmentDate                                              │   │  │
│   │  └─────────────────────────────────────────────────────────────────┘   │  │
│   │                                                                         │  │
│   │  Security:                                                              │  │
│   │  ├─ Row-Level Security (RLS) enabled                                   │  │
│   │  │  CREATE SECURITY POLICY PatientDataPolicy                           │  │
│   │  │  ADD FILTER PREDICATE dbo.fn_securitypredicate(UserID)              │  │
│   │  │  ON dbo.Claims FOR SELECT                                           │  │
│   │  │                                                                      │  │
│   │  ├─ Always Encrypted for sensitive fields                               │  │
│   │  ├─ Transparent Data Encryption (TDE) enabled                           │  │
│   │  ├─ Auditing to Log Analytics                                           │  │
│   │  └─ Firewall: Allow Azure services + private endpoint                  │  │
│   └─────────────────────────────────────────────────────────────────────────┘  │
│                                                                                 │
│   ┌─────────────────────────────────────────────────────────────────────────┐  │
│   │  AZURE BLOB STORAGE                                                     │  │
│   │  Account: claimsdocsstorageprod                                         │  │
│   │  SKU: Standard LRS                                                      │  │
│   │  Region: East US                                                        │  │
│   │                                                                         │  │
│   │  Containers:                                                            │  │
│   │  ┌─────────────────────────────────────────────────────────────────┐   │  │
│   │  │  policy-documents/                                               │   │  │
│   │  │  ├─ employee-handbook.pdf                                        │   │  │
│   │  │  ├─ coverage-details-2024.pdf                                    │   │  │
│   │  │  ├─ appeal-procedures.pdf                                        │   │  │
│   │  │  └─ ...                                                          │   │  │
│   │  │  (Source for Azure AI Search indexer)                            │   │  │
│   │  └─────────────────────────────────────────────────────────────────┘   │  │
│   │                                                                         │  │
│   │  ┌─────────────────────────────────────────────────────────────────┐   │  │
│   │  │  claim-attachments/                                              │   │  │
│   │  │  ├─ {ClaimID}/receipt.pdf                                       │   │  │
│   │  │  ├─ {ClaimID}/medical-report.pdf                                │   │  │
│   │  │  └─ ...                                                          │   │  │
│   │  └─────────────────────────────────────────────────────────────────┘   │  │
│   │                                                                         │  │
│   │  ┌─────────────────────────────────────────────────────────────────┐   │  │
│   │  │  audit-logs-archive/                                             │   │  │
│   │  │  └─ Archived Application Insights logs (cold storage)            │   │  │
│   │  └─────────────────────────────────────────────────────────────────┘   │  │
│   └─────────────────────────────────────────────────────────────────────────┘  │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
                                       ↓
┌─────────────────────────────────────────────────────────────────────────────────┐
│                                                                                 │
│                     SECURITY & MANAGEMENT SERVICES                              │
│                                                                                 │
│   ┌─────────────────────────────────────────────────────────────────────────┐  │
│   │  AZURE AD (Microsoft Entra ID)                                          │  │
│   │  - User authentication for Copilot Studio                               │  │
│   │  - Managed identities for Azure services                                │  │
│   │  - Multi-factor authentication (MFA)                                    │  │
│   │  - Conditional access policies                                          │  │
│   │  - SSO integration                                                      │  │
│   └─────────────────────────────────────────────────────────────────────────┘  │
│                                                                                 │
│   ┌─────────────────────────────────────────────────────────────────────────┐  │
│   │  AZURE KEY VAULT                                                        │  │
│   │  Resource: claims-keyvault-prod                                         │  │
│   │                                                                         │  │
│   │  Secrets:                                                               │  │
│   │  ├─ AzureOpenAI-APIKey                                                  │  │
│   │  ├─ AzureSearch-APIKey                                                  │  │
│   │  ├─ SQL-ConnectionString                                                │  │
│   │  ├─ BlobStorage-ConnectionString                                        │  │
│   │  └─ Dynamics365-APIKey                                                  │  │
│   │                                                                         │  │
│   │  Access:                                                                │  │
│   │  ├─ Azure Function: Managed Identity with Get/List permissions          │  │
│   │  ├─ Power Automate: Service Principal access                            │  │
│   │  └─ Rotation: Automatic every 90 days                                   │  │
│   └─────────────────────────────────────────────────────────────────────────┘  │
│                                                                                 │
│   ┌─────────────────────────────────────────────────────────────────────────┐  │
│   │  AZURE MONITOR & APPLICATION INSIGHTS                                  │  │
│   │  Workspace: claims-monitoring-workspace                                 │  │
│   │                                                                         │  │
│   │  ┌─────────────────────────────────────────────────────────────────┐   │  │
│   │  │  Application Insights: claims-appinsights-prod                  │   │  │
│   │  │  Connected to: Azure Functions                                  │   │  │
│   │  │                                                                 │   │  │
│   │  │  Metrics Tracked:                                               │   │  │
│   │  │  ├─ Request rate, duration, failures                            │   │  │
│   │  │  ├─ Dependency calls (SQL, Azure OpenAI, Search)                │   │  │
│   │  │  ├─ Custom events (claim queries, policy searches)              │   │  │
│   │  │  ├─ Token usage (OpenAI API)                                    │   │  │
│   │  │  └─ User satisfaction scores                                    │   │  │
│   │  └─────────────────────────────────────────────────────────────────┘   │  │
│   │                                                                         │  │
│   │  ┌─────────────────────────────────────────────────────────────────┐   │  │
│   │  │  Log Analytics Workspace                                        │   │  │
│   │  │  ├─ Azure SQL audit logs                                        │   │  │
│   │  │  ├─ Azure Function execution logs                               │   │  │
│   │  │  ├─ Azure OpenAI request logs                                   │   │  │
│   │  │  └─ Security & compliance logs                                  │   │  │
│   │  └─────────────────────────────────────────────────────────────────┘   │  │
│   │                                                                         │  │
│   │  ┌─────────────────────────────────────────────────────────────────┐   │  │
│   │  │  Alerts Configured:                                             │   │  │
│   │  │  ├─ Function failures > 5 in 5 minutes                          │   │  │
│   │  │  ├─ SQL connection failures                                     │   │  │
│   │  │  ├─ OpenAI API errors or rate limits                            │   │  │
│   │  │  ├─ Response time > 10 seconds                                  │   │  │
│   │  │  └─ Unauthorized access attempts                                │   │  │
│   │  └─────────────────────────────────────────────────────────────────┘   │  │
│   └─────────────────────────────────────────────────────────────────────────┘  │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## Detailed Component Architecture

### Azure AI Foundry Integration

Azure AI Foundry serves as the central hub for AI operations:
```
┌─────────────────────────────────────────────────────────────────────┐
│  AZURE AI FOUNDRY ROLE IN ARCHITECTURE                              │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │  Project Hub: Medical-Claims-Chatbot                        │   │
│  │  URL: ai.azure.com                                          │   │
│  │                                                             │   │
│  │  What It Provides:                                          │   │
│  │  ═══════════════════                                        │   │
│  │                                                             │   │
│  │  1. Unified Model Management                               │   │
│  │     ├─ Deploy models (GPT-4, GPT-4o, embeddings)           │   │
│  │     ├─ Monitor token usage across all deployments          │   │
│  │     ├─ Version control for prompts                         │   │
│  │     └─ A/B testing different model versions                │   │
│  │                                                             │   │
│  │  2. Agent Configuration (Optional Use)                     │   │
│  │     ├─ Define agent behaviors                              │   │
│  │     ├─ Connect to tools (Semantic Kernel plugins)          │   │
│  │     ├─ Configure grounding (Azure AI Search)               │   │
│  │     └─ Set safety & content filtering                      │   │
│  │                                                             │   │
│  │  3. Evaluation & Quality Assurance                         │   │
│  │     ├─ Groundedness: Are responses based on facts?         │   │
│  │     ├─ Relevance: Does answer match the question?          │   │
│  │     ├─ Coherence: Is response well-structured?             │   │
│  │     ├─ Fluency: Is language natural?                       │   │
│  │     └─ Custom metrics: Claims-specific evaluations         │   │
│  │                                                             │   │
│  │  4. Prompt Flow (Visual Orchestration)                     │   │
│  │     ├─ Visual design of AI workflows                       │   │
│  │     ├─ Testing with sample data                            │   │
│  │     ├─ Debugging conversation flows                        │   │
│  │     └─ Export to production code                           │   │
│  │                                                             │   │
│  │  5. Built-in RAG Capabilities                              │   │
│  │     ├─ Automatic grounding with Azure AI Search            │   │
│  │     ├─ Citation tracking                                   │   │
│  │     ├─ Source attribution                                  │   │
│  │     └─ Context management                                  │   │
│  │                                                             │   │
│  │  6. Monitoring Dashboard                                   │   │
│  │     ├─ Real-time token consumption                         │   │
│  │     ├─ Cost tracking per conversation                      │   │
│  │     ├─ Response quality metrics                            │   │
│  │     └─ User interaction patterns                           │   │
│  └─────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
```

**Integration Pattern with Semantic Kernel:**
```
Option A: Azure AI Foundry Agent + Semantic Kernel Plugins
┌──────────────────────────────────────────────────────────┐
│  Azure AI Foundry Agent                                  │
│  (Configured in AI Foundry Portal)                       │
│                                                          │
│  Uses Semantic Kernel plugins as "tools":                │
│  ├─ Tool 1: ClaimsPlugin.search_claims                   │
│  ├─ Tool 2: PolicyPlugin.check_coverage                  │
│  └─ Tool 3: ValidationPlugin.validate_patient            │
│                                                          │
│  Benefit: AI Foundry handles evaluation & monitoring    │
└──────────────────────────────────────────────────────────┘

Option B: Semantic Kernel Agent + Azure AI Foundry Models
┌──────────────────────────────────────────────────────────┐
│  Semantic Kernel ChatCompletionAgent                     │
│  (Defined in Python code)                                │
│                                                          │
│  Connects to models deployed in AI Foundry:              │
│  ├─ Azure OpenAI endpoint from AI Foundry project        │
│  ├─ Full control over agent logic                        │
│  └─ Manually send metrics to AI Foundry for evaluation   │
│                                                          │
│  Benefit: Maximum flexibility and customization         │
└──────────────────────────────────────────────────────────┘

Recommended: Hybrid Approach
- Use AI Foundry for model deployment & monitoring
- Use Semantic Kernel for agent logic & plugins
- Send evaluation data from SK to AI Foundry
```

---

## Data Flow: End-to-End Journey

### Complete Request/Response Cycle
```
Patient Query: "What's the status of my knee surgery claim?"

┌─────────────────────────────────────────────────────────────────────┐
│ STEP 1: USER INTERACTION                                           │
│ Location: Patient's Device (Teams/Web/Phone)                       │
│ ─────────────────────────────────────────────────────────────────  │
│                                                                     │
│ Patient authenticated via Azure AD (OAuth 2.0)                     │
│ Message sent to Copilot Studio endpoint                            │
│                                                                     │
│ Data Transmitted:                                                  │
│ {                                                                   │
│   "message": "What's the status of my knee surgery claim?",        │
│   "userId": "sarah.johnson@patient.com",                           │
│   "sessionId": "session-12345",                                    │
│   "channel": "teams"                                               │
│ }                                                                   │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│ STEP 2: COPILOT STUDIO PROCESSING                                  │
│ Location: Microsoft Cloud (Copilot Studio Service)                 │
│ ─────────────────────────────────────────────────────────────────  │
│                                                                     │
│ A. Intent Recognition (Built-in NLU)                               │
│    ├─ Analyzes: "status" + "claim" + "knee surgery"                │
│    ├─ Confidence: 95%                                              │
│    └─ Matched Topic: "CheckClaimStatus"                            │
│                                                                     │
│ B. Entity Extraction                                               │
│    ├─ Procedure: "knee surgery"                                    │
│    └─ Intent: lookup claim status                                  │
│                                                                     │
│ C. Decision: Complex Query Detected                                │
│    ├─ Requires database lookup (can't answer with pre-set text)    │
│    └─ Action: Trigger Power Automate Flow                          │
│                                                                     │
│ Outbound to Power Automate:                                        │
│ {                                                                   │
│   "triggerFlow": "ProcessClaimStatusQuery",                        │
│   "userId": "sarah.johnson@patient.com",                           │
│   "query": "knee surgery claim status",                            │
│   "conversationContext": {...}                                     │
│ }                                                                   │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│ STEP 3: POWER AUTOMATE ORCHESTRATION                               │
│ Location: Power Platform Cloud                                     │
│ ─────────────────────────────────────────────────────────────────  │
│                                                                     │
│ Flow: ProcessClaimStatusQuery                                      │
│                                                                     │
│ Action 1: Validate User                                            │
│   ├─ Lookup user in Azure AD                                       │
│   ├─ Get patient ID from Dataverse                                 │
│   └─ Result: PatientID = "PAT-78945"                               │
│                                                                     │
│ Action 2: Call Azure Function                                      │
│   ├─ Endpoint: https://claims-api.azurewebsites.net/api/process   │
│   ├─ Method: POST                                                  │
│   ├─ Authentication: Managed Identity                              │
│   │                                                                │
│   └─ Request Body:                                                 │
│       {                                                            │
│         "patientId": "PAT-78945",                                  │
│         "query": "knee surgery claim status",                      │
│         "userId": "sarah.johnson@patient.com",                     │
│         "context": {                                               │
│           "channel": "teams",                                      │
│           "sessionId": "session-12345",                            │
│           "requestTime": "2025-01-20T14:35:22Z"                    │
│         }                                                          │
│       }                                                            │
│                                                                     │
│ Waiting for Azure Function response...                             │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│ STEP 4: AZURE FUNCTION EXECUTION                                   │
│ Location: Azure Functions (East US)                                │
│ Runtime: Python 3.11                                               │
│ ─────────────────────────────────────────────────────────────────  │
│                                                                     │
│ Function: ProcessClaimsQuery                                       │
│                                                                     │
│ [A] Initialize Semantic Kernel                                     │
│     ├─ Load Kernel instance                                        │
│     ├─ Add Azure OpenAI service connector                          │
│     │   Endpoint: From AI Foundry project                          │
│     │   Model: gpt-4-prod deployment                               │
│     │   API Key: Retrieved from Key Vault                          │
│     │                                                               │
│     ├─ Register Plugins:                                           │
│     │   ├─ ClaimsPlugin (Native - SQL queries)                     │
│     │   ├─ PolicyPlugin (Prompt - RAG with Azure AI Search)        │
│     │   ├─ ValidationPlugin (Native - security checks)             │
│     │   └─ EscalationPlugin (Native - ticket creation)             │
│     │                                                               │
│     └─ Create ChatCompletionAgent:                                 │
│         Name: "ClaimsSpecialist"                                   │
│         Instructions: "You are a medical claims assistant..."      │
│         Available Functions: All registered plugins                │
│                                                                     │
│ [B] Process Request                                                │
│     ├─ Create ChatHistory object                                   │
│     ├─ Add system message (agent instructions)                     │
│     ├─ Add user message: "knee surgery claim status for PAT-78945" │
│     │                                                               │
│     └─ Invoke Agent:                                               │
│         agent.invoke(chat_history)                                 │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│ STEP 5: SEMANTIC KERNEL → AZURE OPENAI (First Call)                │
│ Location: Communication between Function and OpenAI Service        │
│ ─────────────────────────────────────────────────────────────────  │
│                                                                     │
│ SK Connector formats request for Azure OpenAI:                     │
│                                                                     │
│ POST https://claims-chatbot-openai.openai.azure.com/openai/        │
│      deployments/gpt-4-prod/chat/completions?api-version=2024-08-01│
│                                                                     │
│ Headers:                                                            │
│   api-key: {from-key-vault}                                        │
│   Content-Type: application/json                                   │
│                                                                     │
│ Request Body:                                                       │
│ {                                                                   │
│   "messages": [                                                     │
│     {                                                               │
│       "role": "system",                                             │
│       "content": "You are a medical claims specialist assistant..." │
│     },                                                              │
│     {                                                               │
│       "role": "user",                                               │
│       "content": "Find knee surgery claim status for patient       │
│                   PAT-78945"                                        │
│     }                                                               │
│   ],                                                                │
│   "tools": [                                                        │
│     {                                                               │
│       "type": "function",                                           │
│       "function": {                                                 │
│         "name": "ClaimsPlugin-search_claims",                      │
│         "description": "Search patient claims by criteria",         │
│         "parameters": {                                             │
│           "type": "object",                                         │
│           "properties": {                                           │
│             "patient_id": {"type": "string"},                       │
│             "search_term": {"type": "string"},                      │
│             "date_range": {"type": "string"}                        │
│           },                                                        │
│           "required": ["patient_id"]                                │
│         }                                                           │
│       }                                                             │
│     },                                                              │
│     {                                                               │
│       "type": "function",                                           │
│       "function": {                                                 │
│         "name": "ClaimsPlugin-get_claim_details",                  │
│         "description": "Get detailed info for specific claim",      │
│         "parameters": {...}                                         │
│       }                                                             │
│     }                                                               │
│   ],                                                                │
│   "temperature": 0.7,                                               │
│   "max_tokens": 800                                                 │
│ }                                                                   │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│ STEP 6: AZURE OPENAI PROCESSING                                    │
│ Location: Azure OpenAI Service (East US)                           │
│ Model: GPT-4 (deployed via AI Foundry)                             │
│ ─────────────────────────────────────────────────────────────────  │
│                                                                     │
│ GPT-4 Reasoning:                                                    │
│ "I need to find claims for patient PAT-78945 related to            │
│  knee surgery. I should call the search_claims function with        │
│  patient_id and search_term='knee surgery'"                        │
│                                                                     │
│ GPT-4 Decision: FUNCTION CALL                                       │
│                                                                     │
│ Response from Azure OpenAI:                                         │
│ {                                                                   │
│   "choices": [{                                                     │
│     "message": {                                                    │
│       "role": "assistant",                                          │
│       "content": null,                                              │
│       "tool_calls": [{                                              │
│         "id": "call_abc123xyz",                                     │
│         "type": "function",                                         │
│         "function": {                                               │
│           "name": "ClaimsPlugin-search_claims",                    │
│           "arguments": "{                                           │
│             \"patient_id\": \"PAT-78945\",                          │
│             \"search_term\": \"knee surgery\",                      │
│             \"date_range\": \"last_6_months\"                       │
│           }"                                                        │
│         }                                                           │
│       }]                                                            │
│     },                                                              │
│     "finish_reason": "tool_calls"                                   │
│   }],                                                               │
│   "usage": {                                                        │
│     "prompt_tokens": 487,                                           │
│     "completion_tokens": 45,                                        │
│     "total_tokens": 532                                             │
│   }                                                                 │
│ }                                                                   │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│ STEP 7: SEMANTIC KERNEL EXECUTES NATIVE PLUGIN                     │
│ Location: Azure Function (still running)                           │
│ ─────────────────────────────────────────────────────────────────  │
│                                                                     │
│ SK sees function call request from GPT-4                            │
│                                                                     │
│ SK invokes: ClaimsPlugin.search_claims()                           │
│                                                                     │
│ Parameters:                                                         │
│   - patient_id: "PAT-78945"                                         │
│   - search_term: "knee surgery"                                     │
│   - date_range: "last_6_months"                                     │
│                                                                     │
│ ClaimsPlugin Python code executes:                                 │
│ ┌─────────────────────────────────────────────────────────────┐    │
│ │ @kernel_function                                            │    │
│ │ def search_claims(patient_id: str, search_term: str, ...): │    │
│ │                                                             │    │
│ │     # Connect to Azure SQL                                  │    │
│ │     conn = pyodbc.connect(SQL_CONNECTION_STRING)            │    │
│ │                                                             │    │
│ │     # Execute query with row-level security                 │    │
│ │     # (SQL automatically filters to this patient only)      │    │
│ │     query = """                                             │    │
│ │         SELECT ClaimID, ProcedureCode, Status,              │    │
│ │                Amount, ClaimDate, DenialReason              │    │
│ │         FROM Claims                                         │    │
│ │         WHERE PatientID = ?                                 │    │
│ │         AND (ProcedureDescription LIKE ?                    │    │
│ │              OR ProcedureCode IN (                          │    │
│ │                 SELECT Code FROM Procedures                 │    │
│ │                 WHERE Category = 'Orthopedic'               │    │
│ │              ))                                             │    │
│ │         AND ClaimDate >= DATEADD(month, -6, GETDATE())      │    │
│ │         ORDER BY ClaimDate DESC                             │    │
│ │     """                                                     │    │
│ │                                                             │    │
│ │     cursor.execute(query, (patient_id, f"%{search_term}%")) │    │
│ │     results = cursor.fetchall()                             │    │
│ │                                                             │    │
│ │     return json.dumps([{                                    │    │
│ │         "claimId": row.ClaimID,                             │    │
│ │         "procedure": row.ProcedureCode,                     │    │
│ │         "status": row.Status,                               │    │
│ │         "amount": str(row.Amount),                          │    │
│ │         "date": row.ClaimDate.isoformat()                   │    │
│ │     } for row in results])                                  │    │
│ └─────────────────────────────────────────────────────────────┘    │
│                                                                     │
│ Function returns:                                                   │
│ [                                                                   │
│   {                                                                 │
│     "claimId": "CLM-2024-8873",                                     │
│     "procedure": "27447 (Knee Arthroplasty)",                       │
│     "status": "Processing",                                         │
│     "amount": "45250.00",                                           │
│     "date": "2024-12-18",                                           │
│     "denialReason": null                                            │
│   },                                                                │
│   {                                                                 │
│     "claimId": "CLM-2024-8801",                                     │
│     "procedure": "29881 (Knee Arthroscopy)",                        │
│     "status": "Paid",                                               │
│     "amount": "3200.00",                                            │
│     "date": "2024-11-05",                                           │
│     "denialReason": null                                            │
│   }                                                                 │
│ ]                                                                   │
│                                                                     │
│ Execution logged to Application Insights:                          │
│   - Duration: 245ms                                                 │
│   - SQL query executed                                              │
│   - Records returned: 2                                             │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│ STEP 8: SEMANTIC KERNEL → AZURE OPENAI (Second Call)               │
│ Location: Function sends function result back to GPT-4             │
│ ─────────────────────────────────────────────────────────────────  │
│                                                                     │
│ SK adds function result to conversation history                    │
│                                                                     │
│ POST to Azure OpenAI (same endpoint):                               │
│                                                                     │
│ {                                                                   │
│   "messages": [                                                     │
│     {"role": "system", "content": "You are a medical claims..."},   │
│     {"role": "user", "content": "Find knee surgery claim..."},      │
│     {                                                               │
│       "role": "assistant",                                          │
│       "content": null,                                              │
│       "tool_calls": [...]  // The function call from before         │
│     },                                                              │
│     {                                                               │
│       "role": "tool",                                               │
│       "tool_call_id": "call_abc123xyz",                             │
│       "content": "[{\"claimId\":\"CLM-2024-8873\",...}]"            │
│     }                                                               │
│   ],                                                                │
│   "tools": [...],  // Same tools definition                         │
│   "temperature": 0.7                                                │
│ }                                                                   │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│ STEP 9: AZURE OPENAI FINAL RESPONSE                                │
│ Location: Azure OpenAI Service                                     │
│ ─────────────────────────────────────────────────────────────────  │
│                                                                     │
│ GPT-4 sees function results and generates natural language:        │
│                                                                     │
│ Response:                                                           │
│ {                                                                   │
│   "choices": [{                                                     │
│     "message": {                                                    │
│       "role": "assistant",                                          │
│       "content": "I found 2 claims related to your knee surgery:\n\n│
│                   1. **Claim CLM-2024-8873** (Knee Replacement)\n   │
│                      - Status: Currently Processing\n               │
│                      - Amount: $45,250.00\n                         │
│                      - Date: December 18, 2024\n                    │
│                      - This is your recent knee arthroplasty claim. │
│                        It's being reviewed and should be processed  │
│                        within 10-15 business days.\n\n              │
│                   2. **Claim CLM-2024-8801** (Knee Arthroscopy)\n   │
│                      - Status: Paid\n                               │
│                      - Amount: $3,200.00\n                          │
│                      - Date: November 5, 2024\n                     │
│                      - This diagnostic procedure claim has been     │
│                        fully processed and paid.\n\n                │
│                   Would you like more details about either claim?"  │
│     },                                                              │
│     "finish_reason": "stop"                                         │
│   }],                                                               │
│   "usage": {                                                        │
│     "prompt_tokens": 612,                                           │
│     "completion_tokens": 156,                                       │
│     "total_tokens": 768                                             │
│   }                                                                 │
│ }                                                                   │
│                                                                     │
│ Total tokens for this conversation: 532 + 768 = 1,300 tokens       │
│ Cost: ~$0.039 (at $0.03 per 1K tokens for GPT-4)                   │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│ STEP 10: AZURE FUNCTION FORMATS RESPONSE                           │
│ Location: Azure Function                                           │
│ ─────────────────────────────────────────────────────────────────  │
│                                                                     │
│ Function packages response for Power Automate:                     │
│                                                                     │
│ {                                                                   │
│   "success": true,                                                  │
│   "responseText": "I found 2 claims related to your knee...",       │
│   "structuredData": {                                               │
│     "claims": [                                                     │
│       {                                                             │
│         "claimId": "CLM-2024-8873",                                 │
│         "status": "Processing",                                     │
│         "amount": "45250.00",                                       │
│         "displayStatus": "⏳ Processing",                           │
│         "actionable": true                                          │
│       },                                                            │
│       {                                                             │
│         "claimId": "CLM-2024-8801",                                 │
│         "status": "Paid",                                           │
│         "amount": "3200.00",                                        │
│         "displayStatus": "✓ Paid",                                 │
│         "actionable": false                                         │
│       }                                                             │
│     ]                                                               │
│   },                                                                │
│   "suggestedActions": [                                             │
│     {                                                               │
│       "label": "View Details: CLM-2024-8873",                       │
│       "action": "get_claim_details",                                │
│       "parameters": {"claimId": "CLM-2024-8873"}                    │
│     },                                                              │
│     {                                                               │
│       "label": "Check Processing Timeline",                         │
│       "action": "explain_processing"                                │
│     }                                                               │
│   ],                                                                │
│   "metadata": {                                                     │
│     "tokensUsed": 1300,                                             │
│     "executionTimeMs": 3450,                                        │
│     "model": "gpt-4"                                                │
│   }                                                                 │
│ }                                                                   │
│                                                                     │
│ HTTP 200 response sent back to Power Automate                      │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│ STEP 11: POWER AUTOMATE FORMATS FOR COPILOT STUDIO                 │
│ Location: Power Automate Flow                                      │
│ ─────────────────────────────────────────────────────────────────  │
│                                                                     │
│ Action: Transform response                                         │
│   ├─ Extract structured data                                       │
│   ├─ Create Adaptive Card JSON for Teams                           │
│   └─ Format suggested actions as buttons                           │
│                                                                     │
│ Output to Copilot Studio:                                          │
│ {                                                                   │
│   "message": "I found 2 claims related to your knee surgery...",    │
│   "adaptiveCard": {                                                 │
│     "type": "AdaptiveCard",                                         │
│     "body": [                                                       │
│       {                                                             │
│         "type": "TextBlock",                                        │
│         "text": "I found 2 claims related to your knee surgery:",   │
│         "weight": "bolder"                                          │
│       },                                                            │
│       {                                                             │
│         "type": "FactSet",                                          │
│         "facts": [                                                  │
│           {                                                         │
│             "title": "Claim CLM-2024-8873",                         │
│             "value": "⏳ Processing - $45,250.00 (Dec 18)"         │
│           },                                                        │
│           {                                                         │
│             "title": "Claim CLM-2024-8801",                         │
│             "value": "✓ Paid - $3,200.00 (Nov 5)"                  │
│           }                                                         │
│         ]                                                           │
│       }                                                             │
│     ],                                                              │
│     "actions": [                                                    │
│       {                                                             │
│         "type": "Action.Submit",                                    │
│         "title": "View Details: CLM-2024-8873",                     │
│         "data": {"action": "details", "claimId": "CLM-2024-8873"}  │
│       }                                                             │
│     ]                                                               │
│   }                                                                 │
│ }                                                                   │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────────────┐
│ STEP 12: COPILOT STUDIO DISPLAYS TO USER                           │
│ Location: Copilot Studio → Teams Client                            │
│ ─────────────────────────────────────────────────────────────────  │
│                                                                     │
│ Sarah sees in Teams:                                                │
│                                                                     │
│ ┌─────────────────────────────────────────────────────────────┐    │
│ │ ClaimBot (2:35 PM)                                          │    │
│ │                                                             │    │
│ │ I found 2 claims related to your knee surgery:              │    │
│ │                                                             │    │
│ │ ╔═══════════════════════════════════════════════════════╗  │    │
│ │ ║ Claim CLM-2024-8873                                   ║  │    │
│ │ ║ ⏳ Processing - $45,250.00                            ║  │    │
│ │ ║ Knee Replacement (Dec 18, 2024)                      ║  │    │
│ │ ║                                                       ║  │    │
│ │ ║ This claim is being reviewed and should be           ║  │    │
│ │ ║ processed within 10-15 business days.                ║  │    │
│ │ ║                                                       ║  │    │
│ │ ║ [View Details] [Track Progress]                      ║  │    │
│ │ ╚═══════════════════════════════════════════════════════╝  │    │
│ │                                                             │    │
│ │ ╔═══════════════════════════════════════════════════════╗  │    │
│ │ ║ Claim CLM-2024-8801                                   ║  │    │
│ │ ║ ✓ Paid - $3,200.00                                    ║  │    │
│ │ ║ Knee Arthroscopy (Nov 5, 2024)                       ║  │    │
│ │ ╚═══════════════════════════════════════════════════════╝  │    │
│ │                                                             │    │
│ │ Would you like more details about either claim?             │    │
│ └─────────────────────────────────────────────────────────────┘    │
│                                                                     │
│ Total time: ~3.5 seconds from question to answer                   │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Service-by-Service Breakdown

### Microsoft Copilot Studio

**Purpose:** Conversation management and multi-channel deployment

**What It Does:**
- Natural language understanding (intent recognition)
- Dialog flow management
- Multi-channel support (Web, Teams, SMS, Voice)
- Authentication integration
- Pre-built conversation components
- Analytics and monitoring dashboard

**What It Doesn't Do:**
- Complex database queries
- Advanced AI reasoning
- Custom business logic
- RAG over documents

**Cost:** ~$200-400/month based on sessions

**When to Use:** For all user-facing conversation handling

---

### Power Platform (Power Automate + Dataverse)

**Purpose:** Workflow orchestration and data management

**Power Automate:**
- Connects Copilot Studio to Azure Functions
- Workflow orchestration (if-then logic)
- Data transformation
- Integration hub (400+ connectors)
- Error handling and retries

**Dataverse (Optional):**
- Store conversation transcripts
- Patient preferences
- Custom business entities
- Relational data model

**Cost:** 
- Power Automate: Included in M365 or ~$15/user/month
- Dataverse: ~$40/user/month (if used)

**When to Use:** 
- Connecting Copilot Studio to backends
- Simple workflow automation
- Data enrichment

---

### Azure AI Foundry

**Purpose:** AI project management and governance

**What It Provides:**
- Centralized AI project hub
- Model deployment management
- Prompt versioning and testing
- Agent configuration (optional)
- Built-in RAG capabilities
- Evaluation and quality metrics
- Cost tracking and monitoring

**Key Features:**
- **Prompt Flow:** Visual design of AI workflows
- **Evaluation:** Groundedness, relevance, coherence metrics
- **Monitoring:** Token usage, costs, quality scores
- **Integration:** Connects Azure OpenAI, AI Search, and custom tools

**Cost:** Free (pay for underlying services like Azure OpenAI)

**When to Use:**
- Deploying and managing AI models
- Monitoring AI quality
- Evaluating agent performance
- Team collaboration on AI projects

---

### Azure OpenAI Service

**Purpose:** Large language model inference

**Models Deployed:**
1. **GPT-4 (gpt-4-prod)**
   - Use: Main conversational AI
   - Capacity: 30K TPM
   - Cost: ~$0.03 per 1K tokens

2. **GPT-4o (gpt-4o-prod)**
   - Use: Multi-modal (text + images)
   - Example: Analyze claim document images
   - Capacity: 20K TPM
   - Cost: ~$0.015 per 1K tokens

3. **text-embedding-3-large (embeddings-prod)**
   - Use: Generate vectors for Azure AI Search
   - Dimensions: 3072
   - Capacity: 100K TPM
   - Cost: ~$0.00013 per 1K tokens

**Features:**
- Content filtering (hate, violence, self-harm, sexual)
- Abuse monitoring
- Private endpoint (network isolation)
- Managed identity authentication

**Cost:** Pay-per-token (usage-based)

**When to Use:** Every AI inference request goes here

---

### Azure Functions

**Purpose:** Serverless compute for Semantic Kernel code

**Configuration:**
- Runtime: Python 3.11
- Plan: Premium EP1 (always-on, faster cold start)
- Memory: 3.5 GB
- Region: East US (collocated with Azure OpenAI)

**Functions:**
1. **ProcessClaimsQuery**
   - Trigger: HTTP POST
   - Purpose: Main entry point for claim queries

2. **PolicyQuestionHandler**
   - Trigger: HTTP POST
   - Purpose: RAG-based policy questions

3. **ScheduledIndexing** (optional)
   - Trigger: Timer (daily)
   - Purpose: Keep Azure AI Search index updated

**Cost:** ~$10-50/month (consumption-based)

**When to Use:** All Semantic Kernel agent logic runs here

---

### Semantic Kernel Framework

**Purpose:** AI orchestration and plugin management

**Components:**

1. **Kernel**
   - Central coordinator
   - Service registry
   - Plugin management

2. **Plugins:**
   - **ClaimsPlugin (Native):** SQL database queries
   - **PolicyPlugin (Prompt + RAG):** Policy document search
   - **ValidationPlugin (Native):** Security checks
   - **EscalationPlugin (Native):** Ticket creation

3. **Agents:**
   - ChatCompletionAgent: Stateful conversation handling
   - AzureAIAgent (optional): Integration with AI Foundry agents

**Cost:** Free (open-source framework)

**When to Use:** All custom AI logic and business rules

---

### Azure AI Search (Cognitive Search)

**Purpose:** Vector search and RAG for policy documents

**Index Structure:**
```
policy-documents-index
├─ id: Unique chunk identifier
├─ content: Text content
├─ title: Document title
├─ section: Document section
├─ chunk_number: Chunk sequence
└─ content_vector: 3072-dimensional embedding
```

**Capabilities:**
- **Vector search:** k-NN similarity search
- **Hybrid search:** Combines keyword + vector
- **Semantic ranking:** L2 reranking for better results
- **Integrated vectorization:** Auto-generates embeddings

**Indexer:**
- Source: Azure Blob Storage (policy-docs container)
- Schedule: Daily at 2 AM
- Skillset: OCR → Text Split → Embedding generation

**Cost:** ~$250-300/month (Standard S1 tier)

**When to Use:** All policy-related questions requiring document search

---

### Azure SQL Database

**Purpose:** Structured data storage for claims

**Configuration:**
- Tier: Standard S3 (100 DTUs)
- Storage: 250 GB
- Backup: Geo-redundant, 7-day retention

**Key Tables:**
1. **Claims:** All claim records
2. **Patients:** Patient demographics
3. **Procedures:** Procedure code lookup
4. **AuditLog:** Access tracking

**Security:**
- Row-level security (patients see only their data)
- Always Encrypted (sensitive fields)
- Transparent Data Encryption
- Private endpoint
- Firewall rules

**Cost:** ~$100/month

**When to Use:** All claim data queries

---

### Azure Blob Storage

**Purpose:** Unstructured data storage

**Containers:**

1. **policy-documents/**
   - Store: PDF policy documents
   - Access: Azure AI Search indexer reads from here

2. **claim-attachments/**
   - Store: Claim receipts, medical reports
   - Access: Referenced in claim details

3. **audit-logs-archive/**
   - Store: Cold storage for old logs
   - Access: Compliance retrieval

**Cost:** ~$20/month

**When to Use:** Document storage and archival

---

### Azure Key Vault

**Purpose:** Secrets management

**Stored Secrets:**
- Azure OpenAI API keys
- Azure AI Search API keys
- SQL connection strings
- Blob storage connection strings
- Third-party API keys (Dynamics 365, etc.)

**Access:**
- Azure Function: Managed Identity with Get/List permissions
- Power Automate: Service Principal
- Automatic rotation: Every 90 days

**Cost:** ~$5/month

**When to Use:** All credential storage

---

### Azure Monitor & Application Insights

**Purpose:** Observability and monitoring

**Application Insights Tracks:**
- Request rate, duration, failures
- Dependency calls (SQL, Azure OpenAI, Azure AI Search)
- Custom events (claim queries, policy searches)
- Token usage
- User satisfaction scores

**Alerts:**
- Function failures > 5 in 5 minutes
- SQL connection failures
- OpenAI API errors or rate limits
- Response time > 10 seconds
- Unauthorized access attempts

**Cost:** ~$100/month (based on data ingestion)

**When to Use:** Continuous monitoring and troubleshooting

---

## Integration Patterns

### Pattern 1: Copilot Studio → Power Automate → Azure Function
```
User Query
    ↓
Copilot Studio (Intent Recognition)
    ↓
Power Automate (Orchestration)
    ↓
Azure Function (Semantic Kernel Logic)
    ↓
Azure OpenAI + Plugins
    ↓
Return Response
```

**Use Case:** Complex queries requiring AI + database

---

### Pattern 2: Direct RAG Flow
```
Policy Question
    ↓
Semantic Kernel Agent
    ↓
PolicyPlugin.check_coverage()
    ↓
Azure AI Search (Vector Search)
    ↓
Retrieve Relevant Chunks
    ↓
Azure OpenAI (Generate Answer with Citations)
    ↓
Return Answer
```

**Use Case:** Policy coverage questions

---

### Pattern 3: Simple FAQ (No Backend)
```
User: "What are your hours?"
    ↓
Copilot Studio (Direct Response)
    ↓
Return: "8 AM - 6 PM EST"
```

**Use Case:** Pre-configured FAQs

---

## Deployment Architecture

---

### Network Architecture


---



## Monitoring and Observability

---

## Deployment Architecture

### Azure Resource Organization
```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  AZURE SUBSCRIPTION: Healthcare-Production                          │
│                                                                     │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │                                                               │ │
│  │  RESOURCE GROUP: rg-claims-chatbot-prod                      │ │
│  │  Region: East US                                             │ │
│  │                                                               │ │
│  │  ┌─────────────────────────────────────────────────────────┐ │ │
│  │  │                                                         │ │ │
│  │  │  AI & ML SERVICES                                       │ │ │
│  │  │                                                         │ │ │
│  │  │  ┌───────────────────────────────────────────────────┐ │ │ │
│  │  │  │  Azure OpenAI Service                             │ │ │ │
│  │  │  │  Name: claims-chatbot-openai                      │ │ │ │
│  │  │  │  SKU: Standard                                    │ │ │ │
│  │  │  │  Region: East US                                  │ │ │ │
│  │  │  │                                                   │ │ │ │
│  │  │  │  Deployments:                                     │ │ │ │
│  │  │  │  • gpt-4-prod (30K TPM)                           │ │ │ │
│  │  │  │  • gpt-4o-prod (20K TPM)                          │ │ │ │
│  │  │  │  • embeddings-prod (100K TPM)                     │ │ │ │
│  │  │  └───────────────────────────────────────────────────┘ │ │ │
│  │  │                                                         │ │ │
│  │  │  ┌───────────────────────────────────────────────────┐ │ │ │
│  │  │  │  Azure AI Search (Cognitive Search)               │ │ │ │
│  │  │  │  Name: claims-policy-search-prod                  │ │ │ │
│  │  │  │  SKU: Standard S1                                 │ │ │ │
│  │  │  │  Region: East US                                  │ │ │ │
│  │  │  │                                                   │ │ │ │
│  │  │  │  Indexes:                                         │ │ │ │
│  │  │  │  • policy-documents-index                         │ │ │ │
│  │  │  │                                                   │ │ │ │
│  │  │  │  Indexers:                                        │ │ │ │
│  │  │  │  • policy-docs-indexer (Daily 2 AM)              │ │ │ │
│  │  │  └───────────────────────────────────────────────────┘ │ │ │
│  │  │                                                         │ │ │
│  │  └─────────────────────────────────────────────────────────┘ │ │
│  │                                                               │ │
│  │  ┌─────────────────────────────────────────────────────────┐ │ │
│  │  │                                                         │ │ │
│  │  │  COMPUTE SERVICES                                       │ │ │
│  │  │                                                         │ │ │
│  │  │  ┌───────────────────────────────────────────────────┐ │ │ │
│  │  │  │  Azure Function App                               │ │ │ │
│  │  │  │  Name: claims-processing-func-prod                │ │ │ │
│  │  │  │  Runtime: Python 3.11                             │ │ │ │
│  │  │  │  Plan: Premium EP1                                │ │ │ │
│  │  │  │  Region: East US                                  │ │ │ │
│  │  │  │                                                   │ │ │ │
│  │  │  │  Functions:                                       │ │ │ │
│  │  │  │  • ProcessClaimsQuery (HTTP Trigger)             │ │ │ │
│  │  │  │  • PolicyQuestionHandler (HTTP Trigger)          │ │ │ │
│  │  │  │  • ScheduledIndexing (Timer Trigger)             │ │ │ │
│  │  │  │                                                   │ │ │ │
│  │  │  │  Contains:                                        │ │ │ │
│  │  │  │  • Semantic Kernel Framework                     │ │ │ │
│  │  │  │  • Native Plugins (ClaimsPlugin, etc.)           │ │ │ │
│  │  │  │  • Prompt Plugins (PolicyPlugin, etc.)           │ │ │ │
│  │  │  └───────────────────────────────────────────────────┘ │ │ │
│  │  │                                                         │ │ │
│  │  └─────────────────────────────────────────────────────────┘ │ │
│  │                                                               │ │
│  │  ┌─────────────────────────────────────────────────────────┐ │ │
│  │  │                                                         │ │ │
│  │  │  DATA SERVICES                                          │ │ │
│  │  │                                                         │ │ │
│  │  │  ┌───────────────────────────────────────────────────┐ │ │ │
│  │  │  │  Azure SQL Server                                 │ │ │ │
│  │  │  │  Name: claims-sql-server-prod                     │ │ │ │
│  │  │  │  Region: East US                                  │ │ │ │
│  │  │  │                                                   │ │ │ │
│  │  │  │  Database: ClaimsDB                               │ │ │ │
│  │  │  │  Tier: Standard S3 (100 DTUs)                     │ │ │ │
│  │  │  │  Storage: 250 GB                                  │ │ │ │
│  │  │  │                                                   │ │ │ │
│  │  │  │  Tables:                                          │ │ │ │
│  │  │  │  • Claims                                         │ │ │ │
│  │  │  │  • Patients                                       │ │ │ │
│  │  │  │  • Procedures                                     │ │ │ │
│  │  │  │  • AuditLog                                       │ │ │ │
│  │  │  └───────────────────────────────────────────────────┘ │ │ │
│  │  │                                                         │ │ │
│  │  │  ┌───────────────────────────────────────────────────┐ │ │ │
│  │  │  │  Storage Account                                  │ │ │ │
│  │  │  │  Name: claimsdocsstorageprod                      │ │ │ │
│  │  │  │  SKU: Standard LRS                                │ │ │ │
│  │  │  │  Region: East US                                  │ │ │ │
│  │  │  │                                                   │ │ │ │
│  │  │  │  Containers:                                      │ │ │ │
│  │  │  │  • policy-documents                               │ │ │ │
│  │  │  │  • claim-attachments                              │ │ │ │
│  │  │  │  • audit-logs-archive                             │ │ │ │
│  │  │  └───────────────────────────────────────────────────┘ │ │ │
│  │  │                                                         │ │ │
│  │  └─────────────────────────────────────────────────────────┘ │ │
│  │                                                               │ │
│  │  ┌─────────────────────────────────────────────────────────┐ │ │
│  │  │                                                         │ │ │
│  │  │  SECURITY SERVICES                                      │ │ │
│  │  │                                                         │ │ │
│  │  │  ┌───────────────────────────────────────────────────┐ │ │ │
│  │  │  │  Azure Key Vault                                  │ │ │ │
│  │  │  │  Name: claims-keyvault-prod                       │ │ │ │
│  │  │  │  Region: East US                                  │ │ │ │
│  │  │  │                                                   │ │ │ │
│  │  │  │  Secrets:                                         │ │ │ │
│  │  │  │  • AzureOpenAI-APIKey                             │ │ │ │
│  │  │  │  • AzureSearch-APIKey                             │ │ │ │
│  │  │  │  • SQL-ConnectionString                           │ │ │ │
│  │  │  │  • BlobStorage-ConnectionString                   │ │ │ │
│  │  │  └───────────────────────────────────────────────────┘ │ │ │
│  │  │                                                         │ │ │
│  │  └─────────────────────────────────────────────────────────┘ │ │
│  │                                                               │ │
│  │  ┌─────────────────────────────────────────────────────────┐ │ │
│  │  │                                                         │ │ │
│  │  │  MONITORING SERVICES                                    │ │ │
│  │  │                                                         │ │ │
│  │  │  ┌───────────────────────────────────────────────────┐ │ │ │
│  │  │  │  Application Insights                             │ │ │ │
│  │  │  │  Name: claims-appinsights-prod                    │ │ │ │
│  │  │  │  Region: East US                                  │ │ │ │
│  │  │  │                                                   │ │ │ │
│  │  │  │  Connected to:                                    │ │ │ │
│  │  │  │  • Azure Functions                                │ │ │ │
│  │  │  └───────────────────────────────────────────────────┘ │ │ │
│  │  │                                                         │ │ │
│  │  │  ┌───────────────────────────────────────────────────┐ │ │ │
│  │  │  │  Log Analytics Workspace                          │ │ │ │
│  │  │  │  Name: claims-monitoring-workspace                │ │ │ │
│  │  │  │  Region: East US                                  │ │ │ │
│  │  │  │                                                   │ │ │ │
│  │  │  │  Data Sources:                                    │ │ │ │
│  │  │  │  • Azure SQL audit logs                           │ │ │ │
│  │  │  │  • Function execution logs                        │ │ │ │
│  │  │  │  • Security logs                                  │ │ │ │
│  │  │  └───────────────────────────────────────────────────┘ │ │ │
│  │  │                                                         │ │ │
│  │  └─────────────────────────────────────────────────────────┘ │ │
│  │                                                               │ │
│  └───────────────────────────────────────────────────────────────┘ │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  EXTERNAL SERVICES (SaaS - Not in Resource Group)                  │
│                                                                     │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │  Microsoft Copilot Studio                                     │ │
│  │  • Web chat channel                                           │ │
│  │  • Microsoft Teams channel                                    │ │
│  │  • Voice/Phone channel                                        │ │
│  │  • SMS channel                                                │ │
│  └───────────────────────────────────────────────────────────────┘ │
│                                                                     │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │  Power Automate (Cloud Flows)                                 │ │
│  │  • ProcessClaimStatusQuery flow                               │ │
│  │  • PolicyQuestionHandler flow                                 │ │
│  │  • EscalateToHuman flow                                       │ │
│  └───────────────────────────────────────────────────────────────┘ │
│                                                                     │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │  Dataverse (Optional)                                         │ │
│  │  • Conversation history                                       │ │
│  │  • User preferences                                           │ │
│  └───────────────────────────────────────────────────────────────┘ │
│                                                                     │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │  Azure AI Foundry                                             │ │
│  │  • Project: Medical-Claims-Chatbot                            │ │
│  │  • Model management                                           │ │
│  │  • Evaluation & monitoring                                    │ │
│  └───────────────────────────────────────────────────────────────┘ │
│                                                                     │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │  Azure AD (Microsoft Entra ID)                                │ │
│  │  • User authentication                                        │ │
│  │  • Managed identities                                         │ │
│  │  • MFA enforcement                                            │ │
│  └───────────────────────────────────────────────────────────────┘ │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

### Network Architecture
```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  INTERNET / PUBLIC ACCESS                                          │
│                                                                     │
│  ┌──────────────┐   ┌──────────────┐   ┌──────────────┐          │
│  │   Patients   │   │  Copilot     │   │    Power     │          │
│  │   (Users)    │   │   Studio     │   │  Automate    │          │
│  └──────┬───────┘   └──────┬───────┘   └──────┬───────┘          │
│         │                  │                  │                    │
│         └──────────────────┴──────────────────┘                    │
│                            │                                        │
│                            │ HTTPS                                  │
│                            ↓                                        │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  AZURE CLOUD (East US Region)                                      │
│                                                                     │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │                                                               │ │
│  │  PUBLIC ZONE (Internet-Accessible)                            │ │
│  │                                                               │ │
│  │  ┌─────────────────────────────────────────────────────────┐ │ │
│  │  │  Azure Function App                                     │ │ │
│  │  │  • Public endpoint: claims-processing-func-prod.        │ │ │
│  │  │    azurewebsites.net                                    │ │ │
│  │  │  • HTTPS only                                           │ │ │
│  │  │  • Authentication: Azure AD + Managed Identity          │ │ │
│  │  │                                                         │ │ │
│  │  │  Firewall Rules:                                        │ │ │
│  │  │  • Allow: Power Automate IP ranges                     │ │ │
│  │  │  • Allow: Azure services                               │ │ │
│  │  │  • Deny: All other traffic                             │ │ │
│  │  └─────────────────────────────────────────────────────────┘ │ │
│  │                                                               │ │
│  └───────────────────────────────────────────────────────────────┘ │
│                    │                                                │
│                    │ Private Network                                │
│                    ↓                                                │
│  ┌───────────────────────────────────────────────────────────────┐ │
│  │                                                               │ │
│  │  PRIVATE ZONE (VNet - No Internet Access)                    │ │
│  │  VNet: claims-chatbot-vnet                                   │ │
│  │  Address Space: 10.0.0.0/16                                  │ │
│  │                                                               │ │
│  │  ┌─────────────────────────────────────────────────────────┐ │ │
│  │  │  Subnet: backend-services (10.0.1.0/24)                 │ │ │
│  │  │                                                         │ │ │
│  │  │  Private Endpoints:                                     │ │ │
│  │  │                                                         │ │ │
│  │  │  ┌───────────────────────────────────────────────────┐ │ │ │
│  │  │  │  Azure SQL Database                               │ │ │ │
│  │  │  │  • Private endpoint: 10.0.1.10                    │ │ │ │
│  │  │  │  • No public access                               │ │ │ │
│  │  │  │  • Only accessible from Function App              │ │ │ │
│  │  │  └───────────────────────────────────────────────────┘ │ │ │
│  │  │                                                         │ │ │
│  │  │  ┌───────────────────────────────────────────────────┐ │ │ │
│  │  │  │  Azure OpenAI Service                             │ │ │ │
│  │  │  │  • Private endpoint: 10.0.1.20                    │ │ │ │
│  │  │  │  • No public access                               │ │ │ │
│  │  │  │  • Only accessible from Function App              │ │ │ │
│  │  │  └───────────────────────────────────────────────────┘ │ │ │
│  │  │                                                         │ │ │
│  │  │  ┌───────────────────────────────────────────────────┐ │ │ │
│  │  │  │  Azure AI Search                                  │ │ │ │
│  │  │  │  • Private endpoint: 10.0.1.30                    │ │ │ │
│  │  │  │  • No public access                               │ │ │ │
│  │  │  │  • Only accessible from Function App              │ │ │ │
│  │  │  └───────────────────────────────────────────────────┘ │ │ │
│  │  │                                                         │ │ │
│  │  │  ┌───────────────────────────────────────────────────┐ │ │ │
│  │  │  │  Storage Account                                  │ │ │ │
│  │  │  │  • Private endpoint: 10.0.1.40                    │ │ │ │
│  │  │  │  • No public access                               │ │ │ │
│  │  │  │  • Only accessible from Function App & AI Search  │ │ │ │
│  │  │  └───────────────────────────────────────────────────┘ │ │ │
│  │  │                                                         │ │ │
│  │  └─────────────────────────────────────────────────────────┘ │ │
│  │                                                               │ │
│  │  Network Security Group (NSG):                                │ │
│  │  • Inbound: Allow from Function App subnet only              │ │
│  │  • Outbound: Allow to Azure services only                    │ │
│  │                                                               │ │
│  └───────────────────────────────────────────────────────────────┘ │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

### Data Flow Architecture
```
┌─────────────────────────────────────────────────────────────────────┐
│  STEP 1: USER INTERACTION                                          │
└─────────────────────────────────────────────────────────────────────┘
Patient → Teams/Web → Azure AD Authentication
                             ↓
┌─────────────────────────────────────────────────────────────────────┐
│  STEP 2: COPILOT STUDIO                                            │
│  • Intent recognition                                              │
│  • Dialog management                                               │
│  • Decision: Complex query → Trigger Power Automate                │
└─────────────────────────────────────────────────────────────────────┘
                             ↓
┌─────────────────────────────────────────────────────────────────────┐
│  STEP 3: POWER AUTOMATE                                            │
│  Flow: ProcessClaimStatusQuery                                     │
│  • Validate user                                                   │
│  • Call Azure Function (HTTPS POST)                                │
└─────────────────────────────────────────────────────────────────────┘
                             ↓
┌─────────────────────────────────────────────────────────────────────┐
│  STEP 4: AZURE FUNCTION                                            │
│  claims-processing-func-prod.azurewebsites.net                     │
│  Function: ProcessClaimsQuery                                      │
│  ┌─────────────────────────────────────────────────────────────┐  │
│  │  Semantic Kernel Execution:                                 │  │
│  │  1. Initialize Kernel                                       │  │
│  │  2. Load plugins (Native + Prompt)                          │  │
│  │  3. Create ChatCompletionAgent                              │  │
│  │  4. Invoke agent                                            │  │
│  └─────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────┘
                             ↓
┌─────────────────────────────────────────────────────────────────────┐
│  STEP 5: AZURE OPENAI SERVICE                                      │
│  claims-chatbot-openai.openai.azure.com                            │
│  • Connection: Via private endpoint (10.0.1.20)                    │
│  • Model: gpt-4-prod deployment                                    │
│  • Action: Analyze query, decide to call function                  │
└─────────────────────────────────────────────────────────────────────┘
                             ↓
┌─────────────────────────────────────────────────────────────────────┐
│  STEP 6: PLUGIN EXECUTION                                          │
│  Native Plugin: ClaimsPlugin.search_claims()                       │
│  ┌─────────────────────────────────────────────────────────────┐  │
│  │  Azure SQL Database Query                                   │  │
│  │  • Connection: Via private endpoint (10.0.1.10)             │  │
│  │  • Query: SELECT * FROM Claims WHERE...                     │  │
│  │  • Row-level security enforced                              │  │
│  │  • Return: Claim records                                    │  │
│  └─────────────────────────────────────────────────────────────┘  │
│                          OR                                         │
│  Prompt Plugin: PolicyPlugin.check_coverage()                      │
│  ┌─────────────────────────────────────────────────────────────┐  │
│  │  Azure AI Search Query                                      │  │
│  │  • Connection: Via private endpoint (10.0.1.30)             │  │
│  │  • Vector search: Find relevant policy sections             │  │
│  │  • Return: Top 5 relevant chunks                            │  │
│  │  ↓                                                           │  │
│  │  Call Azure OpenAI with retrieved context                   │  │
│  │  • Generate answer with citations                           │  │
│  └─────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────┘
                             ↓
┌─────────────────────────────────────────────────────────────────────┐
│  STEP 7: AZURE OPENAI (SECOND CALL)                                │
│  • Receive function results                                        │
│  • Generate natural language response                              │
│  • Return formatted answer                                         │
└─────────────────────────────────────────────────────────────────────┘
                             ↓
┌─────────────────────────────────────────────────────────────────────┐
│  STEP 8: AZURE FUNCTION RESPONSE                                   │
│  • Format response as JSON                                         │
│  • Include structured data + text                                  │
│  • Add suggested actions                                           │
│  • Return to Power Automate                                        │
└─────────────────────────────────────────────────────────────────────┘
                             ↓
┌─────────────────────────────────────────────────────────────────────┐
│  STEP 9: POWER AUTOMATE FORMATTING                                 │
│  • Transform response                                              │
│  • Create Adaptive Card for Teams                                  │
│  • Return to Copilot Studio                                        │
└─────────────────────────────────────────────────────────────────────┘
                             ↓
┌─────────────────────────────────────────────────────────────────────┐
│  STEP 10: COPILOT STUDIO DISPLAY                                   │
│  • Render response in chat interface                               │
│  • Display to patient                                              │
│  • Maintain conversation context                                   │
└─────────────────────────────────────────────────────────────────────┘
```

---

### Cost Breakdown by Service
```
┌─────────────────────────────────────────────────────────────────────┐
│  MONTHLY COST ESTIMATE (Medium Scale: 1,000 inquiries/day)         │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  AI & ML Services                                                   │
│  ├─ Azure OpenAI Service                                           │
│  │  • GPT-4: ~40M tokens/month @ $0.03/1K = $1,200                 │
│  │  • Embeddings: ~5M tokens/month @ $0.00013/1K = $0.65           │
│  │  Subtotal: $1,200/month                                         │
│  │                                                                  │
│  ├─ Azure AI Search (Standard S1)                                  │
│  │  • Base cost: $250/month                                        │
│  │  • Storage: 25 GB @ $0.40/GB = $10                              │
│  │  Subtotal: $260/month                                           │
│  │                                                                  │
│  Compute Services                                                   │
│  ├─ Azure Functions (Premium EP1)                                  │
│  │  • Base: $172/month (730 hours × $0.2354/hour)                  │
│  │  • Execution: 30K executions × $0.20/million = $6               │
│  │  Subtotal: $178/month                                           │
│  │                                                                  │
│  Data Services                                                      │
│  ├─ Azure SQL Database (Standard S3)                               │
│  │  • Compute: 100 DTUs = $200/month                               │
│  │  • Storage: 250 GB = $62.50/month                               │
│  │  • Backup: Included                                             │
│  │  Subtotal: $262.50/month                                        │
│  │                                                                  │
│  ├─ Azure Blob Storage (Standard LRS)                              │
│  │  • Storage: 100 GB @ $0.018/GB = $1.80                          │
│  │  • Operations: ~100K @ $0.004/10K = $0.04                       │
│  │  Subtotal: $2/month                                             │
│  │                                                                  │
│  Security & Management                                              │
│  ├─ Azure Key Vault                                                │
│  │  • Secrets: 10 @ $0.03 = $0.30                                  │
│  │  • Operations: 100K @ $0.03/10K = $0.30                         │
│  │  Subtotal: $1/month                                             │
│  │                                                                  │
│  ├─ Application Insights                                           │
│  │  • Data ingestion: 5 GB @ $2.30/GB = $11.50                     │
│  │  • Data retention: Included (90 days)                           │
│  │  Subtotal: $12/month                                            │
│  │                                                                  │
│  ├─ Log Analytics Workspace                                        │
│  │  • Data ingestion: 10 GB @ $2.76/GB = $27.60                    │
│  │  Subtotal: $28/month                                            │
│  │                                                                  │
│  External SaaS Services                                             │
│  ├─ Microsoft Copilot Studio                                       │
│  │  • Based on sessions: ~$300-400/month                           │
│  │  Subtotal: $350/month                                           │
│  │                                                                  │
│  ├─ Power Automate                                                 │
│  │  • Runs: 30K @ $0.60/1000 = $18                                 │
│  │  OR included in M365 license                                    │
│  │  Subtotal: $20/month (if standalone)                            │
│  │                                                                  │
│  ├─ Azure AI Foundry                                               │
│  │  • Free (pay for underlying services)                           │
│  │  Subtotal: $0/month                                             │
│  │                                                                  │
├─────────────────────────────────────────────────────────────────────┤
│  TOTAL MONTHLY COST: ~$2,313.50/month                              │
│                                                                     │
│  Breakdown:                                                         │
│  • AI Services (OpenAI + Search): $1,460 (63%)                     │
│  • Compute (Functions): $178 (8%)                                  │
│  • Data (SQL + Storage): $264.50 (11%)                             │
│  • Monitoring: $40 (2%)                                            │
│  • SaaS (Copilot + Power Automate): $370 (16%)                     │
│  • Security: $1 (<1%)                                              │
│                                                                     │
│  Cost per inquiry: ~$2.31                                          │
│  vs. Call center cost: $30.00                                      │
│  Savings per inquiry: $27.69                                       │
│                                                                     │
│  Monthly savings (if 70% automated):                               │
│  700 calls × $27.69 = $19,383/month                                │
│  Annual savings: $232,596/year                                     │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

### Disaster Recovery Architecture
```
┌─────────────────────────────────────────────────────────────────────┐
│  PRIMARY REGION: EAST US                                           │
│                                                                     │
│  Active-Active Services:                                           │
│  ├─ Azure Function App                                             │
│  ├─ Azure OpenAI Service                                           │
│  ├─ Azure AI Search                                                │
│  ├─ Application Insights                                           │
│  └─ Key Vault                                                      │
│                                                                     │
│  Replicated Data:                                                  │
│  ├─ Azure SQL Database → Geo-replication to West US 2             │
│  ├─ Blob Storage → GRS (Geo-redundant storage)                     │
│  └─ Log Analytics → Multi-region retention                         │
│                                                                     │
│  RTO (Recovery Time Objective): 2 hours                            │
│  RPO (Recovery Point Objective): 5 minutes                         │
└─────────────────────────────────────────────────────────────────────┘
                             ↓ Failover
┌─────────────────────────────────────────────────────────────────────┐
│  SECONDARY REGION: WEST US 2                                       │
│                                                                     │
│  Standby Services (activated during failover):                     │
│  ├─ Azure Function App (auto-scale from 0)                         │
│  ├─ Azure OpenAI Service (separate deployment)                     │
│  ├─ Azure AI Search (replicated index)                             │
│  └─ Azure SQL Database (read-replica promoted to primary)          │
│                                                                     │
│  Failover Process:                                                 │
│  1. Azure Traffic Manager detects primary region failure           │
│  2. Routes traffic to West US 2 Function App                       │
│  3. SQL read-replica promoted to read-write                        │
│  4. Blob Storage fails over to secondary (automatic with GRS)      │
│  5. Copilot Studio automatically uses new endpoint                 │
│                                                                     │
│  Total Failover Time: ~1-2 hours                                   │
└─────────────────────────────────────────────────────────────────────┘
```

---

### Scaling Architecture
```
┌─────────────────────────────────────────────────────────────────────┐
│  AUTO-SCALING CONFIGURATION                                        │
│                                                                     │
│  Azure Function App (Premium Plan)                                 │
│  ├─ Minimum instances: 1                                           │
│  ├─ Maximum instances: 10                                          │
│  ├─ Scale-out trigger: CPU > 70% or Queue depth > 100             │
│  └─ Scale-in trigger: CPU < 40% for 10 minutes                    │
│                                                                     │
│  Scaling Behavior:                                                 │
│                                                                     │
│  Normal Load (< 50 requests/minute):                               │
│  • 1 instance running                                              │
│  • Average response time: 3 seconds                                │
│  • Cost: Base premium plan                                         │
│                                                                     │
│  Medium Load (50-200 requests/minute):                             │
│  • 2-3 instances running                                           │
│  • Average response time: 3.5 seconds                              │
│  • Cost: Base + (2 × $0.2354/hour)                                 │
│                                                                     │
│  High Load (200-500 requests/minute):                              │
│  • 4-7 instances running                                           │
│  • Average response time: 4 seconds                                │
│  • Cost: Base + (6 × $0.2354/hour)                                 │
│                                                                     │
│  Peak Load (> 500 requests/minute):                                │
│  • 10 instances running (max)                                      │
│  • Average response time: 5 seconds                                │
│  • Cost: Base + (9 × $0.2354/hour)                                 │
│  • If still overloaded: Queue requests                             │
│                                                                     │
│  Azure OpenAI Rate Limits:                                         │
│  ├─ GPT-4: 30,000 tokens/minute                                   │
│  ├─ If exceeded: Automatic retry with exponential backoff          │
│  └─ Option: Request quota increase from Microsoft                  │
│                                                                     │
│  Azure SQL Database:                                               │
│  ├─ Current: Standard S3 (100 DTUs)                                │
│  ├─ Can scale up to: S12 (3000 DTUs) without downtime             │
│  └─ Auto-pause disabled (always available)                         │
│                                                                     │
│  Azure AI Search:                                                  │
│  ├─ Current: Standard S1 (1 replica, 1 partition)                 │
│  ├─ Can scale to: S3 (12 replicas, 12 partitions)                 │
│  └─ Query performance: ~50-100ms at current scale                  │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

---

### Deployment Pipeline
```
┌─────────────────────────────────────────────────────────────────────┐
│  CI/CD PIPELINE (Azure DevOps or GitHub Actions)                   │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐  │
│  │  STAGE 1: BUILD                                             │  │
│  │  ├─ Checkout code from Git repository                       │  │
│  │  ├─ Install Python dependencies (requirements.txt)          │  │
│  │  ├─ Install Semantic Kernel package                         │  │
│  │  ├─ Run unit tests (pytest)                                 │  │
│  │  ├─ Run linting (flake8, black)                             │  │
│  │  └─ Package Function App                                    │  │
│  └─────────────────────────────────────────────────────────────┘  │
│                             ↓                                       │
│  ┌─────────────────────────────────────────────────────────────┐  │
│  │  STAGE 2: DEV DEPLOYMENT                                    │  │
│  │  ├─ Deploy to: claims-processing-func-dev                   │  │
│  │  ├─ Environment: Development                                │  │
│  │  ├─ Run integration tests                                   │  │
│  │  ├─ Run Semantic Kernel plugin tests                        │  │
│  │  └─ Validate: All tests pass                                │  │
│  └─────────────────────────────────────────────────────────────┘  │
│                             ↓                                       │
│  ┌─────────────────────────────────────────────────────────────┐  │
│  │  STAGE 3: STAGING DEPLOYMENT                                │  │
│  │  ├─ Deploy to: claims-processing-func-staging               │  │
│  │  ├─ Environment: Staging (production-like)                  │  │
│  │  ├─ Run smoke tests                                         │  │
│  │  ├─ Manual approval required                                │  │
│  │  └─ Validate: QA team sign-off                              │  │
│  └─────────────────────────────────────────────────────────────┘  │
│                             ↓                                       │
│  ┌─────────────────────────────────────────────────────────────┐  │
│  │  STAGE 4: PRODUCTION DEPLOYMENT                             │  │
│  │  ├─ Deploy to: claims-processing-func-prod                  │  │
│  │  ├─ Deployment strategy: Blue-Green                         │  │
│  │  │  • Deploy to "green" slot                                │  │
│  │  │  • Run health checks                                     │  │
│  │  │  • Swap slots (green becomes production)                 │  │
│  │  │  • Monitor for 15 minutes                                │  │
│  │  │  • Rollback if errors detected                           │  │
│  │  ├─ Update configuration                                    │  │
│  │  │  • Retrieve secrets from Key Vault                       │  │
│  │  │  • Set environment variables                             │  │
│  │  └─ Post-deployment                                         │  │
│  │     • Send notification to Slack/Teams                      │  │
│  │     • Update documentation                                  │  │
│  │     • Create deployment tag in Git                          │  │
│  └─────────────────────────────────────────────────────────────┘  │
│                                                                     │
│  Rollback Process (if deployment fails):                           │
│  ├─ Swap slots back to previous version                            │
│  ├─ Duration: < 30 seconds                                         │
│  └─ No data loss (using slot swapping)                             │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```
## Summary

This architecture leverages the complete Microsoft AI stack to create an enterprise-grade medical claims chatbot:

**Frontend:** Copilot Studio (multi-channel, conversation management)  
**Orchestration:** Power Automate (workflow automation)  
**AI Hub:** Azure AI Foundry (model management, evaluation)  
**Intelligence:** Semantic Kernel (custom logic, plugins)  
**Compute:** Azure Functions (serverless execution)  
**AI Models:** Azure OpenAI (GPT-4, embeddings)  
**Search:** Azure AI Search (RAG for policies)  
**Data:** Azure SQL + Blob Storage  
**Security:** Azure AD, Key Vault, Private Endpoints  
**Monitoring:** Application Insights, Log Analytics  

**Total Monthly Cost:** ~$1,200-1,500  
**Development Time:** 6-8 weeks  
**Scalability:** 10 to 10,000+ users with no code changes  
**ROI:** 2-3 months payback, $200K+ annual savings  
---

*Last Updated: January 2025*  
*Architecture Version: 2.0*  
*Document Owner: Solutions Architecture Team*