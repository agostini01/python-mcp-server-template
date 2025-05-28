# MCP Python Template

Implements an HTTP MCP server using FastMCP, enabling local GitHub Copilot instances to connect and interact with the server for code completion and related features.

[`.vscode/mcp.json`](.vscode/mcp.json) registers the URL to query the MCP server. Servers can be re-started with in the file.

[`src/mcp_python/main.py`](src/mcp_python/main.py) implements the MCP tools and the server logic.

This is a Python project using `python:3.10-slim` as the base image and `pixi` for package management.

## Supported MCP Tools

- `fetch_gitignore_template_content`: Fetches a `.gitignore` template based on the provided language or framework. Uses `https://docs.gitignore.io/` api to retrieve the template content.


## Starting the MCP Server

After setting up your environment, start the MCP server by running the following command in your terminal:

```bash
cd src/mcp_python
python main.py
```


## Sample interaction

Create a new `test.gitignore` file. Using agent mode type in the copilot chat window:

```
Update this git ignore file with contents with Node information derived from tools
```

GitHub reply Copilot: 
```
Ran fetch_gitignore_template_content - my-mcp-server...


Made changes.

I’ve updated the .ts.gitignore file with Node.js-specific ignore rules to handle common files and directories. Let me know if you need further adjustments!
```


## Development

This project provides a vscode development container setup using Docker. 


## Dependencies Management

Add your dependencies using `pixi add <package>` command or `pixi pypi add <package>` 
for Python packages. The `pyproject.toml` file will be updated automatically.
