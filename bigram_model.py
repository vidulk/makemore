import torch
import torch.nn as nn
import torch.optim as optim

# Small dataset (feel free to expand)
data = "hello world"

# Character set
chars = sorted(list(set(data)))
vocab_size = len(chars)

# Bigram model architecture
class BigramModel(nn.Module):
    def __init__(self, vocab_size):
        super().__init__()
        # Define model layers here (e.g., embedding, linear, etc.)
    
    def forward(self, x):
        # Define forward pass

# Training setup
# Prepare data, loss function, optimizer, etc.

# Training loop (Karpathy style)
# For each batch, update weights using gradients
