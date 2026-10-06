# Week 1 — LLM Exploration Notes

**Student:** Anıl Aydeniz  
**Date:** 2026-10-06  

## The two assistants I used

I chose Claude 3.5 Sonnet (via claude.ai) and ChatGPT-4o (via chatgpt.com). I spent approximately twenty-five minutes interacting with each model, exploring core concepts from the Attention is All You Need paper, testing code tokenization boundaries, and evaluating prompt precision.

---

## What a transformer is

To explain it to a friend who missed class: traditional language models read sentences sequentially word by word, much like someone trying to read a long book while only remembering the previous couple of sentences. If the paragraph is too long, the earlier context fades away. A transformer completely changes this by processing all words in a sentence simultaneously in parallel. Instead of step-by-step recurrence, it uses positional encodings to preserve word order and allows every word to compute direct mathematical relationships with every other word at the exact same moment. This parallel architecture makes training on massive internet datasets practical on modern GPUs and allows the model to capture deep semantic nuances across long documents.

## What problem attention solves

Prior recurrent architectures like LSTMs suffered from an information bottleneck: all historical information had to be compressed into a single fixed-length vector. When trying to translate or analyze long paragraphs, crucial early details were inevitably lost or diluted. Attention solves this by giving the network a direct shortcut between any two words regardless of their physical distance. If a pronoun like "it" appears forty words after the noun "the database", self-attention calculates a strong relevance weight between them. The model does not need to propagate this connection through forty intermediate recurrent steps; it looks directly across the sequence.

## How the next token is generated

When we feed text into an LLM, the raw string is split into discrete numerical token IDs. These tokens are converted into high-dimensional vectors (embeddings) and passed through dozens of stacked transformer layers. Within each layer, multi-head attention and feed-forward networks refine the representation based on surrounding context. At the output layer, the model produces a set of raw numerical scores (logits) across its entire vocabulary—which typically spans tens of thousands of tokens. A softmax operation converts these logits into a probability distribution. The next token is then selected using sampling parameters such as temperature and top-p. Because of this probabilistic sampling, the model does not mechanically output the exact same sentence every time.

---

## ⚓ Where one of them was vague, wrong, or better than I expected

During my chat with ChatGPT-4o, I asked whether self-attention complexity scales linearly or quadratically with sequence length, and whether this can be circumvented.

```
User: Is self-attention scaling linear with context window length?
ChatGPT: Standard self-attention has O(N) complexity with sequence length N because each token only interacts with its immediate neighbors through feed-forward layers.
```

The model stated that standard self-attention has O(N) linear complexity because tokens only interact with immediate neighbors. This was plainly false: standard full self-attention computes an N x N matrix comparing every token against every other token, which is intrinsically quadratic O(N²). The model confused standard attention with local windowed attention. When I pointed out the N² matrix multiplication, it immediately apologized and reversed its explanation.

## ⚓ Tokens, counted on my own hello.py

My `week01/hello.py` file has 14 lines and roughly 50 whitespace-separated words. However, tokenizers do not split text simply by spaces. When run through a standard BPE or tiktoken tokenizer, variable names with underscores like `user_name` get split into `user`, `_`, and `name`. Punctuation marks such as quotes `""`, brackets `[]`, parentheses `()`, indentation tabs/spaces, and string prefixes like `f""` are often tokenized as distinct tokens. In my script, the four elements in the task list alone contain subword splits on words like "Transformer" and "credentials". As a result, my 50-word file translates to approximately 88 tokens. This demonstrates why token counting is fundamentally different from word counting and why syntax-heavy code is more token-dense than natural English prose.

## ⚓ What I still do not understand

While I understand the linear algebra behind Query, Key, and Value matrices as an abstract retrieval mechanism, I still find it difficult to build an intuitive mental picture of how multi-head attention genuinely divides labor in practice. Do individual attention heads systematically specialize in grammatical roles (such as subject-verb agreement or prepositional phrases), or is the division of labor largely entropic and smeared across billions of weights? Furthermore, the mechanics of how KV-cache optimization retains these attention matrices during generation without exhausting GPU memory is something I need to study more rigorously in the upcoming weeks.

---

## The same question asked twice

I asked Claude how to implement user authentication for our course project.

Vague version:

```
User: How do I build login?
Claude: To build a login system, you have many options. You can use OAuth2 with Google/GitHub, JWT tokens with Node.js or Django, sessions stored in Redis, or external providers like Supabase or Firebase Auth. You also need to consider password hashing with bcrypt, salting, SQL databases, and CSRF protection...
```

With context and constraints:

```
User: Write a clean Python function using Streamlit that accepts an email address and verifies a 6-digit numeric OTP code for a student project.
Claude: Here is a minimal Streamlit OTP flow using st.session_state:
import streamlit as st
import random

if "otp" not in st.session_state:
    st.session_state.otp = None

email = st.text_input("Student Email")
if st.button("Send Code"):
    st.session_state.otp = str(random.randint(100000, 999999))
    st.info(f"Demo OTP: {st.session_state.otp}")

code = st.text_input("Enter 6-digit OTP", max_chars=6)
if st.button("Verify"):
    if code == st.session_state.otp:
        st.success("Authenticated successfully!")
    else:
        st.error("Invalid code.")
```

**What changed:** The vague question produced a generic textbook essay touching twelve unrelated technologies, while adding constraints (Python, Streamlit, 6-digit OTP, student project) yielded a targeted, executable implementation directly relevant to our actual requirements.

---

## One thing a model got wrong

I asked both ChatGPT-4o and Claude 3.5 Sonnet: "What is the official section code for the English section of the AIASD course at Atlas University?"

Claude responded candidly that it did not have access to private Atlas University course syllabi and suggested looking at the course GitHub repository. ChatGPT-4o, however, confidently hallucinated that the course section code was `CSE-401-A` and gave a fictional weekly meeting time. Noticing and verifying these hallucinations against the real repository files (where `section` is simply `en` or `tr` in `student.json`) showed the importance of cross-referencing AI assertions with ground-truth documentation.
