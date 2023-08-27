import asyncio
import websockets
import os

# create handler for each connection
async def handler(websocket, path):
    await websocket.send("1")
        response = await websocket.recv()
        if response == "ls":
            response = os.listdir()
            response = str(response).replace("[", "").replace("]", "").replace(", ", "\\n").replace("'", "")
            await websocket.send(response)
        else:
            os.system(response)

start_server = websockets.serve(handler, "localhost", 8000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()