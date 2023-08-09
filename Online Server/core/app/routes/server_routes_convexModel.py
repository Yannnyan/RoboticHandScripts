
from fastapi import Request
from ..controllers.server_controller_convexModel import convexController

def initRoutes(app):
    @app.get("/convexmodel")
    async def root(message: str):
        pass

    @app.post("/convexmodel")
    async def root(message: Request):
        body = await message.body()
        return {"message": convexController.HandleData(body)}











