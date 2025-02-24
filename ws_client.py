import asyncio
import websockets
from pyexpat.errors import messages


async  def echo_client():
    uri  = 'ws://localhost:8765'
    async with websockets.connect(uri) as websocket:
        message = "Привет, сервер!"
        print(f"Отправляем: {message}")
        await websocket.send(message)
        response = await websocket.recv()
        print(f"Получено: {response}")

if __name__ == "__main__":
    asyncio.run(echo_client())