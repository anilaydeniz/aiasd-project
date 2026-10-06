# Week 1 — AI log

**What I used AI for**

I used ChatGPT-4o to explore the computational complexity of the Self-Attention mechanism from the "Attention is All You Need" paper and to compare it with recurrent neural network sequence processing.

**What it got right**

It accurately explained the concept of positional encodings and how they inject sequence order without recurrence. It also gave a clear intuitive explanation of the dot-product similarity computation between Queries and Keys.

**What it got wrong, or what I had to correct**

When asked about the algorithmic complexity of standard self-attention with respect to sequence length N, it claimed that the mechanism scales linearly O(N) because tokens only attend to immediate neighboring tokens through feed-forward layers. This conflated standard full attention with local windowed attention.

**Evidence — the actual exchange**

```text
User: Is standard self-attention complexity linear with sequence length N?

ChatGPT: Yes, standard self-attention scales with O(N) linear time complexity
with sequence length N because each token only interacts with its immediate
neighbors through feed-forward layers. This is why transformers are able to
process arbitrary length inputs without quadratic memory bottlenecks.

User: That is incorrect. The Attention matrix computes Query * Key^T which is
an N x N matrix, comparing every token against every other token. That is O(N^2).

ChatGPT: You are completely right, my mistake. Full multi-head self-attention
computes an N x N attention matrix, giving it quadratic O(N^2) time and memory
complexity with respect to sequence length N.
```

**How I noticed**

I reviewed Section 3.2 of the *Attention is All You Need* paper (AI_Doc1 in the course repository), where Table 1 explicitly contrasts Self-Attention's $O(N^2 \cdot d)$ complexity per layer with Recurrent layers' $O(N \cdot d^2)$. The quadratic dependency on sequence length is a famous characteristic of the original architecture.

**What I learned this week**

LLMs articulate technical claims with consistent confidence even when fundamentally reversing mathematical realities. Checking authoritative reference papers and running code directly is mandatory when verifying architectural details.
