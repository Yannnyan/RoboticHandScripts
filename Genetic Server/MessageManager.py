from ast import literal_eval
import matplotlib.pyplot as plt
from fastapi import WebSocket
import numpy as np
import json
import torch
from Genetic import Genetic

class MessageManager:
    def __init__(self) -> None:
        self.ws = None

    async def WaitForMsg(self):
        data = await self.ws.receive_text()

        # 1, 2, 3, 4, 5 rays of the output from unity
        data = literal_eval(data)
        # read the numpy to tensor
        # data = torch.from_numpy(np.array(list(data.values())))
        for key in data:
            data[key] = torch.from_numpy(np.array(list(data[key])))

        return data

    def initWebSocket(self, ws: WebSocket):
        self.ws = ws

    async def SendHand(self, handOutputs: dict):
        """
        Send the generation over web socket to get the rays of contact by index
        """
        # load the numpy array into dict
        # d = {}
        # d["gene_" + str(index)] = {}
        # for i in range(len(handOutputs)):
        #     d["gene_" + str(index)]["object_" + str(i)] = np.array2string(handOutputs[i], separator=',').replace("\n","")
        s = json.dumps(handOutputs)
        # print(f"[Message Manager] Sending {s}")
        print("[Message Manager] Sending Msg")
        # convert the dict into json and send it!
        await self.ws.send_text(s)









