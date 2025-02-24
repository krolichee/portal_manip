import asyncio
import websockets

async def echo(websocket):
    try:
        async for message in websocket:
            print("recieved "+str(message))
            await websocket.send(message)
    except Exception as e:
        print("error: "+str(e))
    async for message in websocket:
        await websocket.send(message)

async def main():
    async with websockets.serve(echo, 'localhost', 8765):
        print("started on ws://localhost:8765")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())