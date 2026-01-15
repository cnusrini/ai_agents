# Layer 1: LLM/Transformer Architecture Deep Dive

## Overview

This document provides a comprehensive deep dive into the GPT-4 transformer architecture (Layer 1 - The Brain), which is the foundation that ALL frameworks and tools ultimately use.

---

## Table of Contents

- [High-Level Architecture](#high-level-architecture)
- [Stage-by-Stage Breakdown](#stage-by-stage-breakdown)
- [Single Transformer Layer Details](#single-transformer-layer-details)
- [Self-Attention Mechanism](#self-attention-mechanism)
- [Model Parameters](#model-parameters)
- [Autoregressive Generation](#autoregressive-generation)
- [Data Flow Pipeline](#data-flow-pipeline)
- [GPU Memory Layout](#gpu-memory-layout)
- [Key Characteristics Summary](#key-characteristics-summary)

---

## High-Level Architecture
```text
┌─────────────────────────────────────────────────────────────────────┐
│                    GPT-4 TRANSFORMER ARCHITECTURE                    │
│                         (Layer 1 - The Brain)                        │
└─────────────────────────────────────────────────────────────────────┘

INPUT: "What is the capital of France?"
   ↓
┌─────────────────────────────────────────────────────────────────────┐
│ STAGE 1: TOKENIZATION                                               │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│ Text → Token IDs                                                     │
│ "What is the capital of France?"                                    │
│    ↓                                                                │
│ [2061, 318, 262, 3139, 286, 4881, 30]                             │
│                                                                      │
│ (Each number represents a token from vocabulary ~100k tokens)       │
└──────────────────────────────────┬──────────────────────────────────┘
                                   ↓
┌─────────────────────────────────────────────────────────────────────┐
│ STAGE 2: EMBEDDING LAYER                                            │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│ Token IDs → Dense Vectors                                           │
│                                                                      │
│ [2061] → [0.234, -0.567, 0.123, ..., 0.891]  (12,288 dimensions)  │
│ [318]  → [0.445, -0.221, 0.778, ..., 0.334]                       │
│ [262]  → [-0.112, 0.889, -0.445, ..., 0.667]                      │
│  ...                                                                │
│                                                                      │
│ + Positional Encoding (where each token is in sequence)            │
│   Position 0: [0.000, 1.000, 0.000, ...]                          │
│   Position 1: [0.841, 0.540, 0.014, ...]                          │
│   Position 2: [0.909, -0.416, 0.028, ...]                         │
│                                                                      │
│ Result: Embedded Tokens (7 vectors × 12,288 dimensions each)       │
└──────────────────────────────────┬──────────────────────────────────┘
                                   ↓
┌─────────────────────────────────────────────────────────────────────┐
│ STAGE 3: TRANSFORMER LAYERS (Repeat 96 times!)                      │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌────────────────────────────────────────────────────────────┐   │
│  │ TRANSFORMER LAYER 1                                        │   │
│  ├────────────────────────────────────────────────────────────┤   │
│  │                                                            │   │
│  │  ┌──────────────────────────────────────────────────┐     │   │
│  │  │ Multi-Head Self-Attention                        │     │   │
│  │  │ • Every token looks at every other token        │     │   │
│  │  │ • Complexity: O(n²) where n = sequence length    │     │   │
│  │  │ • 96 attention heads in parallel                 │     │   │
│  │  └────────────────────┬─────────────────────────────┘     │   │
│  │                       ↓                                    │   │
│  │  ┌──────────────────────────────────────────────────┐     │   │
│  │  │ Add & Normalize                                  │     │   │
│  │  │ (Residual connection + Layer normalization)      │     │   │
│  │  └────────────────────┬─────────────────────────────┘     │   │
│  │                       ↓                                    │   │
│  │  ┌──────────────────────────────────────────────────┐     │   │
│  │  │ Feed-Forward Network (MLP)                       │     │   │
│  │  │ • Two linear transformations                     │     │   │
│  │  │ • Expand dimensions then contract back           │     │   │
│  │  │ • Activation: GELU                               │     │   │
│  │  └────────────────────┬─────────────────────────────┘     │   │
│  │                       ↓                                    │   │
│  │  ┌──────────────────────────────────────────────────┐     │   │
│  │  │ Add & Normalize                                  │     │   │
│  │  │ (Residual connection + Layer normalization)      │     │   │
│  │  └──────────────────────────────────────────────────┘     │   │
│  └────────────────────────────────────────────────────────────┘   │
│                               ↓                                    │
│  ┌────────────────────────────────────────────────────────────┐   │
│  │ TRANSFORMER LAYER 2 (identical structure)                 │   │
│  └──────────────────────────────┬─────────────────────────────┘   │
│                                 ↓                                  │
│                               ...                                  │
│                                 ↓                                  │
│  ┌────────────────────────────────────────────────────────────┐   │
│  │ TRANSFORMER LAYER 96 (identical structure)                │   │
│  └──────────────────────────────┬─────────────────────────────┘   │
│                                                                     │
│  Each layer progressively refines the representations:             │
│  • Early layers: Syntax, grammar, simple patterns                  │
│  • Middle layers: Semantics, context, meaning                      │
│  • Deep layers: Reasoning, complex relationships                   │
└──────────────────────────────────┬──────────────────────────────────┘
                                   ↓
┌─────────────────────────────────────────────────────────────────────┐
│ STAGE 4: OUTPUT PROJECTION (Language Modeling Head)                 │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│ Final Hidden State → Probability Distribution over Vocabulary       │
│                                                                      │
│ [12,288 dimensions] → [~100,000 probabilities]                      │
│                                                                      │
│ Example output for next token:                                      │
│ Token 5434 ("The"):     0.0234  (2.34%)                            │
│ Token 7273 ("Paris"):   0.4521  (45.21%) ← Highest!                │
│ Token 1892 ("France"):  0.0156  (1.56%)                            │
│ Token 3421 ("London"):  0.0089  (0.89%)                            │
│ ... (rest of vocabulary with lower probabilities)                   │
│                                                                      │
│ Apply softmax to convert logits to probabilities                    │
└──────────────────────────────────┬──────────────────────────────────┘
                                   ↓
┌─────────────────────────────────────────────────────────────────────┐
│ STAGE 5: SAMPLING / TOKEN SELECTION                                 │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│ Choose next token based on:                                         │
│ • Temperature (controls randomness)                                 │
│ • Top-p / nucleus sampling                                          │
│ • Top-k sampling                                                    │
│                                                                      │
│ Selected: Token 7273 ("Paris")                                      │
│                                                                      │
│ Append to sequence: [..., 7273]                                     │
└──────────────────────────────────┬──────────────────────────────────┘
                                   ↓
┌─────────────────────────────────────────────────────────────────────┐
│ STAGE 6: AUTOREGRESSIVE LOOP                                        │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│ Repeat Stages 2-5 with expanded sequence until:                    │
│                                                                      │
│ Iteration 1:                                                        │
│ Input:  [What, is, the, capital, of, France, ?]                    │
│ Output: [Paris] ← Generated                                         │
│                                                                      │
│ Iteration 2:                                                        │
│ Input:  [What, is, the, capital, of, France, ?, Paris]            │
│ Output: [.] ← Generated                                             │
│                                                                      │
│ Iteration 3:                                                        │
│ Input:  [What, is, the, capital, of, France, ?, Paris, .]         │
│ Output: [<EOS>] ← End of sequence token                            │
│                                                                      │
│ STOP CONDITIONS:                                                    │
│ ✓ End-of-sequence token generated                                  │
│ ✓ Max token limit reached                                          │
│ ✓ Stop sequence encountered                                        │
└──────────────────────────────────┬──────────────────────────────────┘
                                   ↓
┌─────────────────────────────────────────────────────────────────────┐
│ STAGE 7: DETOKENIZATION                                             │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│ Token IDs → Text                                                    │
│ [7273, 13] → "Paris."                                              │
│                                                                      │
│ Final Output: "Paris."                                              │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Stage-by-Stage Breakdown

### Stage 1: Tokenization

Converts raw text into numerical token IDs that the model can process.

**Process:**
- Text is split into subwords/tokens using a tokenizer (e.g., BPE, WordPiece)
- Each token is mapped to a unique ID from the vocabulary (~100,000 tokens)
- Special tokens may be added (e.g., `<BOS>`, `<EOS>`)

**Example:**
```
Input:  "What is the capital of France?"
Output: [2061, 318, 262, 3139, 286, 4881, 30]
```

### Stage 2: Embedding Layer

Converts sparse token IDs into dense, meaningful vector representations.

**Components:**
1. **Token Embeddings**: Each token ID → 12,288-dimensional vector
2. **Positional Encodings**: Adds position information (where token appears in sequence)

**Why Positional Encoding?**
- Transformers process all tokens in parallel (unlike RNNs)
- Without position info, "cat eats mouse" = "mouse eats cat"
- Position embeddings preserve sequence order

### Stage 3: Transformer Layers (96 layers)

Each layer contains two main sub-blocks:
1. Multi-Head Self-Attention
2. Feed-Forward Network (MLP)

Both use **residual connections** and **layer normalization**.

### Stage 4: Output Projection

Converts final hidden states into probability distribution over vocabulary.

**Process:**
```
[12,288 dims] → Linear Layer → [100,000 logits] → Softmax → [100,000 probabilities]
```

### Stage 5: Sampling

Selects the next token based on the probability distribution.

**Methods:**
- **Greedy**: Pick highest probability token (deterministic)
- **Temperature**: Adjust randomness (higher = more random)
- **Top-p (Nucleus)**: Sample from top X% probability mass
- **Top-k**: Sample from top k most likely tokens

### Stage 6: Autoregressive Loop

Repeats generation process until stopping condition is met.

**Key Insight**: Each iteration processes the ENTIRE sequence from scratch, but with one more token added!

### Stage 7: Detokenization

Converts token IDs back to human-readable text.

---

## Single Transformer Layer Details
```text
┌─────────────────────────────────────────────────────────────────────┐
│              ONE TRANSFORMER LAYER (of 96 total)                     │
└─────────────────────────────────────────────────────────────────────┘

Input: Hidden states from previous layer
[batch_size, sequence_length, 12288]

│
├─────────────────────────────────────────────────────────────────────┐
│ BLOCK 1: MULTI-HEAD SELF-ATTENTION                                  │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  Input Vectors                                                      │
│       ↓                                                             │
│  ┌────────────────────────────────────────────────┐                │
│  │ Linear Projections (Create Q, K, V)            │                │
│  │                                                 │                │
│  │ Query  (Q) = Input × W_Q                       │                │
│  │ Key    (K) = Input × W_K                       │                │
│  │ Value  (V) = Input × W_V                       │                │
│  └──────────────────┬──────────────────────────────┘                │
│                     ↓                                               │
│  ┌────────────────────────────────────────────────┐                │
│  │ Split into 96 Attention Heads                  │                │
│  │                                                 │                │
│  │ Each head: [batch, seq_len, 128 dimensions]    │                │
│  │                                                 │                │
│  │ Head 1 | Head 2 | ... | Head 96                │                │
│  └──────────────────┬──────────────────────────────┘                │
│                     ↓                                               │
│  ┌────────────────────────────────────────────────┐                │
│  │ For Each Head in Parallel:                     │                │
│  │                                                 │                │
│  │ 1. Compute Attention Scores:                   │                │
│  │    Scores = Q × K^T / √(d_k)                  │                │
│  │                                                 │                │
│  │    Example (3 tokens):                         │                │
│  │    Token 1 attends to: [0.7, 0.2, 0.1]        │                │
│  │    Token 2 attends to: [0.1, 0.8, 0.1]        │                │
│  │    Token 3 attends to: [0.2, 0.3, 0.5]        │                │
│  │                                                 │                │
│  │ 2. Apply Softmax (normalize to probabilities)  │                │
│  │                                                 │                │
│  │ 3. Weighted Sum of Values:                     │                │
│  │    Output = Attention_Scores × V               │                │
│  └──────────────────┬──────────────────────────────┘                │
│                     ↓                                               │
│  ┌────────────────────────────────────────────────┐                │
│  │ Concatenate All Heads                          │                │
│  │ [batch, seq_len, 96 × 128 = 12,288]           │                │
│  └──────────────────┬──────────────────────────────┘                │
│                     ↓                                               │
│  ┌────────────────────────────────────────────────┐                │
│  │ Output Projection                              │                │
│  │ Linear: [12,288] → [12,288]                    │                │
│  └──────────────────┬──────────────────────────────┘                │
│                     ↓                                               │
│  Attention Output                                                   │
└─────────────────────┼───────────────────────────────────────────────┘
                      ↓
                      │←─────────────┐
                      ↓              │ Residual Connection
┌─────────────────────────────────────────────────────────────────────┐
│                     Add & Normalize                                 │
│                                                                     │
│  output = LayerNorm(input + attention_output)                      │
└──────────────────────┬──────────────────────────────────────────────┘
                       ↓
┌─────────────────────────────────────────────────────────────────────┐
│ BLOCK 2: FEED-FORWARD NETWORK (MLP)                                │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────────────────────────────────────────┐                 │
│  │ First Linear Transformation (Expansion)      │                 │
│  │                                               │                 │
│  │ [12,288] → [49,152]  (4x expansion)          │                 │
│  │                                               │                 │
│  │ Dense layer with weights                     │                 │
│  └────────────────┬─────────────────────────────┘                 │
│                   ↓                                                │
│  ┌──────────────────────────────────────────────┐                 │
│  │ Activation Function: GELU                    │                 │
│  │                                               │                 │
│  │ Non-linear transformation                    │                 │
│  └────────────────┬─────────────────────────────┘                 │
│                   ↓                                                │
│  ┌──────────────────────────────────────────────┐                 │
│  │ Second Linear Transformation (Contraction)   │                 │
│  │                                               │                 │
│  │ [49,152] → [12,288]  (back to original size) │                 │
│  │                                               │                 │
│  │ Dense layer with weights                     │                 │
│  └────────────────┬─────────────────────────────┘                 │
│                   ↓                                                │
│  FFN Output                                                        │
└───────────────────┼─────────────────────────────────────────────────┘
                    ↓
                    │←─────────────┐
                    ↓              │ Residual Connection
┌─────────────────────────────────────────────────────────────────────┐
│                   Add & Normalize                                   │
│                                                                     │
│  output = LayerNorm(input + ffn_output)                            │
└──────────────────────┬──────────────────────────────────────────────┘
                       ↓
              Output to Next Layer
```

### Key Components Explained

#### Multi-Head Self-Attention
- **Purpose**: Allows each token to "look at" and gather information from all other tokens
- **Multi-Head**: 96 parallel attention mechanisms, each learning different patterns
- **Complexity**: O(n²) - every token attends to every other token

#### Feed-Forward Network (FFN)
- **Purpose**: Non-linear transformations applied independently to each position
- **Architecture**: Two linear layers with GELU activation in between
- **Expansion**: Temporarily expands dimensions (12,288 → 49,152 → 12,288)

#### Residual Connections
- **Purpose**: Helps gradients flow through deep networks
- **Formula**: `output = input + transformation(input)`

#### Layer Normalization
- **Purpose**: Stabilizes training by normalizing activations
- **Applied**: After each sub-block (attention and FFN)

---

## Self-Attention Mechanism

### How Tokens Look at Each Other
```text
┌─────────────────────────────────────────────────────────────────────┐
│           SELF-ATTENTION: How Tokens Look at Each Other             │
└─────────────────────────────────────────────────────────────────────┘

Example Sentence: "The cat sat on the mat"

STEP 1: Create Q, K, V for each token
┌─────────────────────────────────────────────────────────────────────┐
│ Token    │ Query (Q)      │ Key (K)        │ Value (V)             │
├──────────┼────────────────┼────────────────┼───────────────────────┤
│ "The"    │ [0.2, 0.3,...] │ [0.1, 0.5,...] │ [0.4, 0.2,...]       │
│ "cat"    │ [0.5, 0.1,...] │ [0.3, 0.2,...] │ [0.1, 0.6,...]       │
│ "sat"    │ [0.1, 0.4,...] │ [0.2, 0.4,...] │ [0.3, 0.1,...]       │
│ "on"     │ [0.3, 0.2,...] │ [0.4, 0.1,...] │ [0.2, 0.4,...]       │
│ "the"    │ [0.2, 0.5,...] │ [0.1, 0.3,...] │ [0.5, 0.3,...]       │
│ "mat"    │ [0.4, 0.1,...] │ [0.5, 0.2,...] │ [0.1, 0.5,...]       │
└─────────────────────────────────────────────────────────────────────┘

STEP 2: Compute Attention Scores (Q × K^T)
┌─────────────────────────────────────────────────────────────────────┐
│                    How much each token attends to others            │
│                                                                     │
│         The    cat    sat    on     the    mat                     │
│  The  │ 0.15 │ 0.20 │ 0.10 │ 0.05 │ 0.40 │ 0.10 │                 │
│  cat  │ 0.10 │ 0.60 │ 0.15 │ 0.05 │ 0.05 │ 0.05 │                 │
│  sat  │ 0.05 │ 0.30 │ 0.40 │ 0.15 │ 0.05 │ 0.05 │                 │
│  on   │ 0.05 │ 0.10 │ 0.20 │ 0.15 │ 0.10 │ 0.40 │                 │
│  the  │ 0.40 │ 0.05 │ 0.05 │ 0.10 │ 0.15 │ 0.25 │                 │
│  mat  │ 0.10 │ 0.05 │ 0.05 │ 0.35 │ 0.20 │ 0.25 │                 │
│                                                                     │
│  Interpretation:                                                    │
│  • "cat" attends strongly to itself (0.60)                         │
│  • "cat" attends to "The" (0.10) - article-noun relationship       │
│  • "sat" attends to "cat" (0.30) - subject-verb relationship       │
│  • "on" attends to "mat" (0.40) - prepositional relationship       │
│                                                                     │
│  This is how the model learns grammar and relationships!           │
└─────────────────────────────────────────────────────────────────────┘

STEP 3: Apply Attention Weights to Values
┌─────────────────────────────────────────────────────────────────────┐
│ For "cat" token:                                                    │
│                                                                     │
│ Output = 0.10×V("The") + 0.60×V("cat") + 0.15×V("sat") +          │
│          0.05×V("on") + 0.05×V("the") + 0.05×V("mat")             │
│                                                                     │
│ Result: A new representation of "cat" that incorporates            │
│         context from all other tokens in the sequence              │
└─────────────────────────────────────────────────────────────────────┘
```

### Why O(n²) Complexity?
```text
┌─────────────────────────────────────────────────────────────────────┐
│ For n tokens, must compute n × n attention scores                  │
│                                                                     │
│ 10 tokens    → 100 computations                                    │
│ 100 tokens   → 10,000 computations                                 │
│ 1,000 tokens → 1,000,000 computations                              │
│ 8,000 tokens → 64,000,000 computations (GPT-4 context window)      │
│                                                                     │
│ This is why long contexts are expensive!                            │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Model Parameters

### GPT-4 Specifications

| Parameter | Value (GPT-4 estimated) |
|-----------|------------------------|
| Number of Layers | 96 |
| Hidden Size (d_model) | 12,288 |
| Number of Attention Heads | 96 |
| Head Dimension | 128 (12,288 / 96) |
| FFN Inner Dimension | 49,152 (4x hidden size) |
| Vocabulary Size | ~100,000 tokens |
| Context Window | 8,192 - 128,000 tokens |
| Total Parameters | ~1.76 Trillion (estimated) |

### Parameter Count Breakdown
```text
┌─────────────────────────────────────────────────────────────────────┐
│ Component                        │ Parameters                       │
├──────────────────────────────────┼──────────────────────────────────┤
│ Embedding Layer                  │ 100K × 12,288 = ~1.2B           │
│ Each Transformer Layer:          │                                  │
│   • Attention (Q,K,V,O)         │ 4 × (12,288 × 12,288) = ~604M   │
│   • FFN (2 linear layers)       │ 2 × (12,288 × 49,152) = ~1.2B   │
│   • Total per layer             │ ~1.8B                            │
│ All 96 Layers                    │ 96 × 1.8B = ~173B                │
│ Output Head                      │ 12,288 × 100K = ~1.2B           │
│                                  │                                  │
│ TOTAL (estimated)                │ ~1.76 Trillion                   │
└──────────────────────────────────┴──────────────────────────────────┘
```

### Memory Requirements

**FP16 Precision:**
- **Model Weights**: ~3.5 TB
- **Activations** (per forward pass): ~50-100 GB
- **KV Cache** (8K context): ~1-2 GB

**GPU Requirements:**
- **Training**: Thousands of A100/H100 GPUs
- **Inference**: 8-16x A100 (80GB) or H100 GPUs in parallel

---

## Autoregressive Generation

### Token-by-Token Generation Loop
```text
┌─────────────────────────────────────────────────────────────────────┐
│         HOW GPT-4 GENERATES TEXT TOKEN BY TOKEN                     │
└─────────────────────────────────────────────────────────────────────┘

Initial Prompt: "The capital of France is"

┌─────────────────────────────────────────────────────────────────────┐
│ ITERATION 1                                                          │
├─────────────────────────────────────────────────────────────────────┤
│ Input Sequence:  [The, capital, of, France, is]                    │
│                                                                     │
│ Pass through all 96 layers                                          │
│ ↓ ↓ ↓                                                               │
│                                                                     │
│ Output Logits: [vocab_size] probabilities                           │
│ • Token 7273 "Paris": 0.78 ← Highest!                              │
│ • Token 5501 "Lyon":  0.05                                          │
│ • Token 3429 "the":   0.03                                          │
│ • ...                                                               │
│                                                                     │
│ Sample: Choose "Paris"                                              │
└─────────────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────────────┐
│ ITERATION 2                                                          │
├─────────────────────────────────────────────────────────────────────┤
│ Input Sequence:  [The, capital, of, France, is, Paris]             │
│                                     ↑                                │
│                      Added token from previous iteration            │
│                                                                     │
│ Pass through all 96 layers (with NEW attention patterns!)          │
│ ↓ ↓ ↓                                                               │
│                                                                     │
│ Output Logits: [vocab_size] probabilities                           │
│ • Token 13 ".":      0.65 ← Highest!                               │
│ • Token 11 ",":      0.20                                           │
│ • Token 290 "and":   0.08                                           │
│ • ...                                                               │
│                                                                     │
│ Sample: Choose "."                                                  │
└─────────────────────────────────────────────────────────────────────┘
                            ↓
┌─────────────────────────────────────────────────────────────────────┐
│ ITERATION 3                                                          │
├─────────────────────────────────────────────────────────────────────┤
│ Input Sequence:  [The, capital, of, France, is, Paris, .]          │
│                                                  ↑                   │
│                      Added token from previous iteration            │
│                                                                     │
│ Pass through all 96 layers                                          │
│ ↓ ↓ ↓                                                               │
│                                                                     │
│ Output Logits: [vocab_size] probabilities                           │
│ • Token <EOS>: 0.92 ← End of sequence!                             │
│ • ...                                                               │
│                                                                     │
│ STOP: End-of-sequence token generated                               │
└─────────────────────────────────────────────────────────────────────┘

Final Output: "Paris."
```

### Key Insight

**Each iteration processes the ENTIRE sequence from scratch, but with one more token added!**

This is why:
- Generation gets slower as output gets longer
- Long outputs are more expensive
- Context window limits matter

---

## Data Flow Pipeline

### Complete Transformation Through the Model
```text
┌─────────────────────────────────────────────────────────────────────┐
│              COMPLETE DATA TRANSFORMATION PIPELINE                   │
└─────────────────────────────────────────────────────────────────────┘

Input Text
    ↓
[String: "Hello world"]
    ↓
┌────────────────────────┐
│ Tokenizer              │
│ BPE/WordPiece         │
└───────────┬────────────┘
            ↓
[Token IDs: [15496, 995]]
[Shape: (2,)]
    ↓
┌────────────────────────┐
│ Embedding Lookup       │
│ + Positional Encoding  │
└───────────┬────────────┘
            ↓
[Embeddings: (2, 12288)]
[2 tokens × 12,288 dimensions]
    ↓
┌────────────────────────┐
│ Layer 1: Transformer   │
│ • Self-Attention       │
│ • Feed-Forward         │
└───────────┬────────────┘
            ↓
[Hidden States: (2, 12288)]
    ↓
┌────────────────────────┐
│ Layer 2: Transformer   │
└───────────┬────────────┘
            ↓
[Hidden States: (2, 12288)]
    ↓
        ... (94 more layers)
    ↓
┌────────────────────────┐
│ Layer 96: Transformer  │
└───────────┬────────────┘
            ↓
[Final Hidden States: (2, 12288)]
    ↓
┌────────────────────────┐
│ Output Projection      │
│ (LM Head)              │
└───────────┬────────────┘
            ↓
[Logits: (2, 100000)]
[2 positions × 100K vocab]
    ↓
┌────────────────────────┐
│ Softmax (last position)│
└───────────┬────────────┘
            ↓
[Probabilities: (100000,)]
[Distribution over vocab]
    ↓
┌────────────────────────┐
│ Sampling               │
│ (argmax/temperature)   │
└───────────┬────────────┘
            ↓
[Next Token ID: 345]
    ↓
┌────────────────────────┐
│ Detokenizer            │
└───────────┬────────────┘
            ↓
[String: "!"]
    ↓
Append to sequence and repeat!
```

---

## GPU Memory Layout

### Memory Allocation During Inference
```text
┌─────────────────────────────────────────────────────────────────────┐
│                    GPU VRAM ALLOCATION                               │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│ MODEL WEIGHTS (Static - Loaded Once)                     ~3.5 TB    │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │ Embedding Layer:         100K × 12,288    = 1.2B params     │ │
│  └──────────────────────────────────────────────────────────────┘ │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │ Transformer Layer 1:     ~1.8B params                        │ │
│  │   • Q,K,V,O Weights:     4 × (12K × 12K)                    │ │
│  │   • FFN Weights:         2 × (12K × 49K)                    │ │
│  └──────────────────────────────────────────────────────────────┘ │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │ Transformer Layer 2:     ~1.8B params                        │ │
│  └──────────────────────────────────────────────────────────────┘ │
│                           ...                                      │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │ Transformer Layer 96:    ~1.8B params                        │ │
│  └──────────────────────────────────────────────────────────────┘ │
│  ┌──────────────────────────────────────────────────────────────┐ │
│  │ Output Head:             100K × 12,288    = 1.2B params     │ │
│  └──────────────────────────────────────────────────────────────┘ │
│                                                                     │
│  Total: ~1.76 Trillion parameters × 2 bytes (FP16) = ~3.5 TB      │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│ KV CACHE (Per Request - Dynamic)                     ~1-2 GB        │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  For each layer (96 total):                                        │
│  • Key vectors:   [batch, num_heads, seq_len, head_dim]           │
│  • Value vectors: [batch, num_heads, seq_len, head_dim]           │
│                                                                     │
│  Example (8K context):                                             │
│  • 96 layers × 2 (K+V) × 96 heads × 8192 tokens × 128 dims        │
│  • ~1.5 GB for one request                                         │
│                                                                     │
│  Why needed: Avoid recomputing attention for previous tokens      │
└─────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────┐
│ ACTIVATION MEMORY (Per Forward Pass)                 ~50-100 GB     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Temporary memory for intermediate computations:                   │
│  • Attention scores                                                │
│  • FFN intermediate activations                                    │
│  • Layer normalization statistics                                 │
│  • Gradient buffers (if training)                                 │
└─────────────────────────────────────────────────────────────────────┘
```

### KV Cache Explained

**What is KV Cache?**
- Stores Key and Value vectors from previous tokens
- Avoids recomputing attention for tokens already processed
- Critical optimization for autoregressive generation

**Without KV Cache:**
```
Iteration 1: Process tokens [1]
Iteration 2: Process tokens [1, 2]        ← Recompute token 1
Iteration 3: Process tokens [1, 2, 3]     ← Recompute tokens 1, 2
Iteration 4: Process tokens [1, 2, 3, 4]  ← Recompute tokens 1, 2, 3
```

**With KV Cache:**
```
Iteration 1: Process tokens [1], cache K,V for token 1
Iteration 2: Process token [2], use cached K,V for token 1
Iteration 3: Process token [3], use cached K,V for tokens 1, 2
Iteration 4: Process token [4], use cached K,V for tokens 1, 2, 3
```

**Speed Improvement**: ~10-100x faster generation!

---

## Key Characteristics Summary
```text
┌─────────────────────────────────────────────────────────────────────┐
│                        GPT-4 KEY FACTS                               │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  Architecture Type:      Decoder-only Transformer                   │
│  Number of Layers:       96                                         │
│  Parameters:             ~1.76 Trillion (estimated)                 │
│  Context Window:         8K - 128K tokens                           │
│  Attention Type:         Causal (masked) self-attention             │
│  Attention Complexity:   O(n²) where n = sequence length            │
│  Generation Method:      Autoregressive (token-by-token)            │
│  Parallelization:        Layers process sequentially                │
│                          Attention heads process in parallel        │
│  Memory:                 ~3.5 TB for weights (FP16)                 │
│  Training Hardware:      Thousands of GPUs/TPUs                     │
│  Inference Hardware:     8-16 high-end GPUs                         │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Why These Details Matter

1. **O(n²) Complexity**: Explains why longer contexts are expensive
2. **Autoregressive Generation**: Why generation is slower than processing input
3. **96 Layers**: Why the model can capture complex patterns and reasoning
4. **KV Cache**: Why memory usage grows with context length
5. **Token-by-token**: Why you see "typewriter effect" in streaming mode

---

## Important Notes

### Universal Truth

**This transformer architecture (Layer 1) is what ALL the following ultimately use:**
- Azure OpenAI SDK
- Azure AI Foundry SDK
- Semantic Kernel
- Copilot Studio
- LangChain
- AutoGen

**The frameworks are just different ways to:**
- Format requests to this architecture
- Manage conversation state
- Orchestrate multiple calls
- Integrate with other services

**But the core 96-layer transformer doing the actual "thinking" is always the same!**

---

## References

- [Attention Is All You Need (Original Transformer Paper)](https://arxiv.org/abs/1706.03762)
- [GPT-3 Paper](https://arxiv.org/abs/2005.14165)
- [Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)
- [The Annotated Transformer](http://nlp.seas.harvard.edu/2018/04/03/attention.html)

---

## License

[Your License Here]

## Contributing

[Your Contributing Guidelines Here]