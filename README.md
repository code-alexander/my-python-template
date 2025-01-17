# my-python-template

[Copier](https://github.com/copier-org/copier) template my Python projects.

## 🚀 Features

- [`uv`](https://github.com/astral-sh/uv) set up as the package manager.
- [`pre-commit`](https://pre-commit.com/) hooks configured.

## 📖 How to use it

### Installation

Install [uv](https://github.com/astral-sh/uv) and Python:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
uv python install 3.12
```

Install [Copier](https://github.com/copier-org/copier):

```bash
uv tool install copier
```

And generate a project:

```bash
uvx copier copy "gh:code-alexander/my-python-template" /path/to/your/new/project
```
