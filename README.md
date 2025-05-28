# MCP Python Project

This is a Python project using `python:3.10-slim` as the base image and `pixi` for package management.

## Setup

1. Build the Docker image:
   ```bash
   docker build -t mcp-python .
   ```

2. Run the container:
   ```bash
   docker run -it --rm mcp-python
   ```

## Project Structure

- `Dockerfile`: Defines the development container setup.
- `pyproject.toml`: Manages project dependencies using `pixi`.
- `README.md`: Project documentation.

## Dependencies

Add your dependencies to `pyproject.toml` under `[tool.pixi.dependencies]`.
