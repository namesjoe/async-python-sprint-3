import asyncio
import websockets
import json
import argparse
from config import Settings

settings = Settings()

async def receive_messages():
    async with websockets.connect(f"ws://{settings.SERVER_HOST}:{settings.SERVER_PORT}/connect") as ws:
        try:
            async for message in ws:
                data = json.loads(message)
                sender = data.get("sender", "Unknown")
                message_text = data.get("message", "")
                print(f"{sender}: {message_text}")
        except websockets.exceptions.ConnectionClosed as exc:
            print(f"Connection closed unexpectedly: {exc}")

async def send_message(sender, message):
    async with websockets.connect(f"ws://{settings.SERVER_HOST}:{settings.SERVER_PORT}/connect") as ws:
        try:
            data = {
                "sender": sender,
                "message": message
            }
            await ws.send(json.dumps(data))
        except websockets.exceptions.ConnectionClosed as exc:
            print(f"Connection closed unexpectedly: {exc}")

def parse_arguments():
    parser = argparse.ArgumentParser(description="Chat Client")
    parser.add_argument("sender_name", help="Name of the sender")
    return parser.parse_args()

async def main():
    args = parse_arguments()
    sender_name = args.sender_name

    # Start the receive_messages function in the background
    receive_messages_task = asyncio.create_task(receive_messages())

    while True:
        message = input("Enter your message: ")
        await send_message(sender_name, message)

if __name__ == '__main__':
    asyncio.run(main())
