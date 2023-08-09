import sys
import numpy as np
from fastapi import FastAPI, Request, WebSocket
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from ast import literal_eval
import json
import matplotlib.pyplot as plt
import numpy as np
import cv2 
import io
from PIL import Image
import GeneticManager
import asyncio
import threading
from GeneticManager import msgManager
from ConcurencyManager import semaph_boss, finish_lst, tasks_lst

boss_thread = threading.Thread(target=GeneticManager.run)
app = FastAPI()

@app.get("/")
async def root(message: str):
    arr = np.fromstring(message,dtype=np.float64,sep="\t")
    return {}

@app.websocket("/ws")
async def root(websocket: WebSocket):
    global tasks_lst, finish_lst
    await websocket.accept()

    while True:
        # recieve and parse the data into dict
        data = await websocket.receive_text()
        data = literal_eval(data)
        
        # send the paths to init genetic manager, and init the web socket for communication later on
        GeneticManager.initGenetic(data)

        GeneticManager.initWebSocket(websocket)

        boss_thread.start()
        while True:
            # print("[Server] waiting for acquire ")
            
            # get hand and index
            population = await tasks_lst.get()
            # send the hand to unity
            print("[Fitness_wrapper] sending output to unity")
            await msgManager.SendHand(population)
            # recieve rays feedback
            print("[Fitness_wrapper] waiting to recieve feedback")
            data = await msgManager.WaitForMsg()
            # print(data)
            # append the result feedback
            await finish_lst.put(data)
            semaph_boss.release()



