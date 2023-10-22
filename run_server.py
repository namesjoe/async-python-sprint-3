import asyncio

import websockets

from config import Settings
from server import Chat

settings = Settings()

async def main():
    server = Chat()

    async with websockets.serve(
            server.handle_client, host=settings.SERVER_HOST, port=settings.SERVER_PORT
    ):
        print(f"WebSocket server started on {settings.SERVER_HOST}:{settings.SERVER_PORT}")

        await asyncio.Future()  # Keep the server running


if __name__ == '__main__':
    asyncio.run(main())
