from pathlib import Path

import torch

DATASET = Path(__file__).parent.parent / "input.txt"


def test_dataset_is_present():
    text = DATASET.read_text(encoding="utf-8")
    assert len(text) == 1_115_394
    assert len(set(text)) == 65


def test_attention_gradients_flow():
    x = torch.randn(2, 8, 16, requires_grad=True)
    attention = torch.nn.MultiheadAttention(16, 2, batch_first=True)
    output, _ = attention(x, x, x)
    output.sum().backward()
    assert output.shape == x.shape
    assert x.grad is not None
