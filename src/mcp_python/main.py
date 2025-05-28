"""Main module for MCP Python project.

This module defines tools for MCP and runs the MCP server.
"""

import requests
from fastmcp import FastMCP

mcp = FastMCP("Demo 🚀")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


@mcp.tool()
def fetch_gitignore_template(template: str) -> str:
    """Fetch a specific gitignore template for a specified language.

    Args:
        template (str): The name of the gitignore template to fetch.

    Returns:
        str: The content of the gitignore template.
    """

    # First retrieve the list of available templates and check if the template exists
    url = "https://www.toptal.com/developers/gitignore/api/list"
    params = {"format": "lines"}
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    # Reponse has this format: vcpkg,venv,vercel,vertx,video\nvim,virtualenv,...
    response = response.text.splitlines()
    response = set(
        item.strip().lower() for line in response for item in line.split(",")
    )
    available_templates = response

    template = template.lower()

    if template not in available_templates:
        raise ValueError(
            f"Template '{template}' not found in available templates."
        )

    url = f"https://www.toptal.com/developers/gitignore/api/{template}"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.text


if __name__ == "__main__":
    mcp.run(
        transport="streamable-http", host="localhost", port=8000, path="/mcp/"
    )
