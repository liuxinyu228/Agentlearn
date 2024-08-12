# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     server
   Description :
   Author :        xiao_liu
   date：          2024/8/12 22:10
-------------------------------------------------
"""
__author__ = 'xiao_liu'

import uvicorn
from fastapi import FastAPI, WebSocket
from chatModel import Master

app = FastAPI()


@app.post("/chat")
def chat(query: str):
    master = Master()
    return master.run(query)


@app.post("/add_urls")
def add_urls():
    return "test"


@app.post("/add_pdfs")
def add_pdfs():
    return "test"


@app.post("add_texts")
def add_texts():
    return "test"


# @app.webhooks("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     pass


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
