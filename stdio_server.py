# stdio_server.py
from mcp.server.fastmcp import FastMCP

mcp = FastMCP('py-stdio-demo')

@mcp.tool()
def add(a: int, b: int) -> str:
    return f'Result: {a + b}'

@mcp.tool()
def hello(name: str) -> str:
    return f"Hello {name}"

if __name__ == '__main__':
    mcp.run(transport="stdio")  # 默认 stdio

