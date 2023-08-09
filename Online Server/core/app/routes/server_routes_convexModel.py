
from fastapi import Request
from ..controllers.server_controller_convexModel import convexController
from ..models.server_models_Data import Data


def initRoutes(app):
    @app.get("/convexmodel")
    async def root(message: str):
        pass

    @app.post("/convexmodel")
    async def root(message: Data):
        # print(message)
        body = message
        prediction = convexController.HandleData(body)
        return {"message": prediction}











