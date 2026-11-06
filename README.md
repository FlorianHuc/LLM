# LLM

Personal LLM training lab.

## Required tools

- [Git](https://git-scm.com/)
- [uv](https://docs.astral.sh/uv/): installs Python 3.13+ if needed, and all packages

Installed by uv, with versions locked in `uv.lock`:

- PyTorch (CPU build)
- JupyterLab and ipykernel
- NumPy
- Weights & Biases (`uv run wandb login` to log runs)

## Setup

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
git clone git@github.com:FlorianHuc/LLM.git
cd LLM
uv sync
uv run jupyter lab
```
