# local_client.py
import asyncio, os, sys
from stdio_server import mcp
from mcp.client import Client

async def main():
    client = Client(mcp)
    await client.__aenter__()  # 等价于 async with，但写明流程更直观

    # 调用同步工具（通过 await，Client 的 call_tool 通常是异步接口）
    resp = await client.call_tool("hello", {"name": "MCP"})
    print("hello ->", resp)
    await client.__aexit__(None, None, None)

if __name__ == '__main__':
    asyncio.run(main())

