import asyncio
from mcp.client.stdio import stdio_client
from mcp.client.stdio import c

async def main():
    # 启动子进程作为 MCP server（例如 server.py）
    async with stdio_client(["python", "server.py"]) as (session, stdio):
        print("MCP client connected to server!")

        # 请求调用某个 tool（假设 server 里定义了 hello 工具）
        req = CallRequest(
            method="tools.call",
            params={
                "name": "hello",
                "arguments": {"name": "world"}
            }
        )

        result = await session.call(req)
        print("Server replied:", result)

asyncio.run(main())
